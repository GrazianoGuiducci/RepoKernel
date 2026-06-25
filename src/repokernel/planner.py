"""Deterministic GenerationPlan creation for RepoKernel Phase 1."""
from __future__ import annotations

import hashlib
from pathlib import Path
from typing import Any, Iterable

from .canonical import canonical_hash
from .models import validate_seed_spec, validate_target_snapshot
from .paths import normalize_relative_path
from .snapshot import snapshot_entries, snapshot_integrity_errors
from .version import package_version


LEVEL_ORDER = ("L0", "L1", "L2", "L3")


def build_generation_plan(
    seed_spec: dict[str, Any],
    *,
    existing_paths: Iterable[str] | None = None,
    target_snapshot: dict[str, Any] | None = None,
    bundle_provenance: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """Build a deterministic no-authority GenerationPlan from a reviewed SeedSpec."""
    errors = validate_seed_spec(seed_spec)
    if errors:
        raise ValueError("; ".join(errors))
    existing = {normalize_relative_path(path) for path in (existing_paths or [])}
    if target_snapshot is not None:
        snapshot_errors = validate_target_snapshot(target_snapshot) + snapshot_integrity_errors(target_snapshot)
        if snapshot_errors:
            raise ValueError("; ".join(f"target_snapshot: {error}" for error in snapshot_errors))
    snapshot_items = snapshot_entries(target_snapshot or {})
    existing.update(snapshot_items)
    project = seed_spec["project"]
    level = seed_spec["readiness_level"]
    plan_files = _planned_files(project, level)
    target_mode = seed_spec["target"]["mode"]
    target_snapshot_hash = (target_snapshot or {}).get("tree_hash", "new-repository-no-snapshot")
    target_identity = (target_snapshot or {}).get("target_identity", canonical_hash({"target": seed_spec["target"]}))
    stale_snapshot = target_mode == "existing_repository_retrofit" and not target_snapshot
    items = []
    blocked_reasons: list[str] = []
    if stale_snapshot:
        blocked_reasons.append("existing repository retrofit requires a current valid TargetSnapshot")
    for path in sorted(plan_files):
        content = plan_files[path]
        action = "create"
        planned_hash = _content_hash(content)
        existing_entry = snapshot_items.get(path)
        existing_hash = existing_entry.get("content_hash") if existing_entry else None
        if stale_snapshot:
            action = "withhold"
        elif path in existing:
            if existing_hash == planned_hash:
                action = "leave_unchanged"
            elif path.startswith(".repokernel/"):
                action = "propose_update"
            elif path in {"AGENTS.md", "CURRENT_STATE.md", "README.md"}:
                action = "propose_update"
            else:
                action = "conflict"
        items.append({
            "path": path,
            "action": action,
            "reason": _reason_for(path, action),
            "source_fields": ["project.name", "project.intent", "project.product", "readiness_level"],
            "content_hash": planned_hash,
            "patch_or_content_ref": f"inline:{planned_hash}",
            "risk": "safe" if action in {"create", "leave_unchanged"} else "review_required",
            "approval_needed": action in {"propose_update", "conflict"},
            "authority_effect": "none",
            "content": content,
        })
    items_hash = canonical_hash(items)
    compiler_version = package_version()
    seed_hash = canonical_hash(seed_spec)
    policy = {
        "apply_policy": "stage_only",
        "file_plan_policy": seed_spec.get("file_plan_policy"),
        "target_mode": target_mode,
    }
    plan_identity = {
        "compiler_version": compiler_version,
        "seed_hash": seed_hash,
        "bundle": bundle_provenance or {},
        "target_identity": target_identity,
        "target_snapshot_hash": target_snapshot_hash,
        "policy": policy,
        "items_hash": items_hash,
    }
    projected_after_state_hash = canonical_hash({
        "kind": "projected_after_state.v1",
        "before_hash": target_snapshot_hash,
        "target_identity": target_identity,
        "items": [
            {"path": item["path"], "action": item["action"], "content_hash": item["content_hash"]}
            for item in items
        ],
    })
    blocked = stale_snapshot or any(item["action"] == "conflict" for item in items)
    if any(item["action"] == "conflict" for item in items):
        blocked_reasons.append("one or more planned files conflict with target authority")
    return {
        "schema": "repokernel.generation-plan.v1",
        "plan_id": canonical_hash(plan_identity),
        "compiler_version": compiler_version,
        "seed_hash": seed_hash,
        "bundle_hash": canonical_hash(bundle_provenance or {}),
        "bundle_provenance": bundle_provenance or {},
        "generated_on": seed_spec.get("reviewed_on", "undated"),
        "target": seed_spec["target"],
        "target_identity": target_identity,
        "target_snapshot_hash": target_snapshot_hash,
        "before_hash": target_snapshot_hash,
        "after_hash": projected_after_state_hash,
        "after_hash_kind": "projected_after_state.v1",
        "apply_policy": "stage_only",
        "rollback_manifest": None,
        "items": items,
        "blocked": blocked,
        "blocked_reasons": blocked_reasons,
        "extensions": seed_spec.get("extensions", {}),
    }


def render_seed_files(seed_spec: dict[str, Any]) -> dict[str, str]:
    errors = validate_seed_spec(seed_spec)
    if errors:
        raise ValueError("; ".join(errors))
    return _planned_files(seed_spec["project"], seed_spec["readiness_level"])


def dry_run_apply_plan(plan: dict[str, Any], target: Path) -> dict[str, Any]:
    """Return the write set without touching the target filesystem."""
    planned_writes = [item["path"] for item in plan.get("items", []) if item.get("action") == "create"]
    return {
        "schema": "repokernel.apply-report.v1",
        "target": str(target),
        "dry_run": True,
        "writes_performed": [],
        "planned_writes": planned_writes,
        "blocked": bool(plan.get("blocked")),
    }


def _planned_files(project: dict[str, Any], level: str) -> dict[str, str]:
    name = project["name"]
    intent = project["intent"]
    product = project["product"]
    slug = _slug(name)
    files = {
        "AGENTS.md": f"# {name} Agent Gate\n\nThis root file is an adapter. Read `.repokernel/state/CURRENT_STATE.md` before editing.\n",
        ".repokernel/state/CURRENT_STATE.md": f"# Current State\n\nupdated: generated-from-seed\nstatus: draft\n\n```text\nactive_surface: {name}\ncurrent_next: verify first RepoKernel cycle\n```\n",
        ".repokernel/packets/FIRST_PACKET.md": f"# First Packet\n\nobjective: establish RepoKernel continuity for {name}\nintent: {intent}\n",
    }
    if _level_at_least(level, "L1"):
        files.update({
            "README.md": f"# {name}\n\n{product}\n\nIntent: {intent}\n",
            ".repokernel/sources/SOURCE_ATLAS.md": f"# Source Atlas\n\n| Path | Role |\n| --- | --- |\n| `README.md` | project definition |\n| `.repokernel/state/CURRENT_STATE.md` | active state |\n",
            f".repokernel/skills/{slug}-semantic-kernel/SKILL.md": f"---\nname: {slug}-semantic-kernel\ndescription: Preserve continuity, sources and boundaries for {name}.\n---\n\n# {name} Semantic Kernel\n",
        })
    if _level_at_least(level, "L2"):
        files.update({
            ".repokernel/manifest.json": "{\n  \"schema\": \"repokernel.manifest.v1\",\n  \"readiness_target\": \"L2\"\n}\n",
            ".repokernel/registry/skills.json": "{\n  \"schema\": \"repokernel.skill-registry.v1\",\n  \"skills\": []\n}\n",
            ".repokernel/evidence/README.md": "# Evidence\n\nValidation records for this project kernel.\n",
            ".repokernel/deltas/README.md": "# Deltas\n\nDurable accepted changes only.\n",
        })
    return files


def _level_at_least(level: str, minimum: str) -> bool:
    return LEVEL_ORDER.index(level) >= LEVEL_ORDER.index(minimum)


def _reason_for(path: str, action: str) -> str:
    if action == "propose_update":
        return f"{path} already exists; existing authority requires reviewable update"
    if action == "conflict":
        return f"{path} already exists and cannot be overwritten silently"
    if action == "leave_unchanged":
        return f"{path} already exists with matching content"
    if action == "withhold":
        return "existing repository retrofit requires a current TargetSnapshot"
    return "required by selected readiness level"


def _slug(value: str) -> str:
    return "".join(ch.lower() if ch.isalnum() else "-" for ch in value).strip("-")


def _content_hash(content: str) -> str:
    return hashlib.sha256(content.encode("utf-8")).hexdigest()
