"""Deterministic GenerationPlan creation for RepoKernel Phase 1."""
from __future__ import annotations

from datetime import date
from pathlib import Path
from typing import Any, Iterable

from .canonical import canonical_hash
from .models import validate_seed_spec
from .paths import normalize_relative_path


LEVEL_ORDER = ("L0", "L1", "L2", "L3")


def build_generation_plan(seed_spec: dict[str, Any], *, existing_paths: Iterable[str] | None = None) -> dict[str, Any]:
    """Build a deterministic no-authority GenerationPlan from a reviewed SeedSpec."""
    errors = validate_seed_spec(seed_spec)
    if errors:
        raise ValueError("; ".join(errors))
    existing = {normalize_relative_path(path) for path in (existing_paths or [])}
    project = seed_spec["project"]
    level = seed_spec["readiness_level"]
    plan_files = _planned_files(project, level)
    items = []
    for path in sorted(plan_files):
        content = plan_files[path]
        action = "create"
        if path in existing:
            action = "propose_update" if path in {"AGENTS.md", "CURRENT_STATE.md", "README.md"} else "conflict"
        items.append({
            "path": path,
            "action": action,
            "reason": _reason_for(path, action),
            "source_fields": ["project.name", "project.intent", "project.product", "readiness_level"],
            "content_hash": canonical_hash(content),
            "risk": "safe" if action in {"create", "leave_unchanged"} else "review_required",
            "approval_needed": action in {"propose_update", "conflict"},
            "authority_effect": "none",
            "content": content,
        })
    return {
        "schema": "repokernel.generation-plan.v1",
        "seed_hash": canonical_hash(seed_spec),
        "generated_on": date.today().isoformat(),
        "target": seed_spec["target"],
        "items": items,
        "blocked": any(item["action"] == "conflict" for item in items),
        "extensions": seed_spec.get("extensions", {}),
    }


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
        "AGENTS.md": f"# {name} Agent Gate\n\nRead `CURRENT_STATE.md` before editing. Work from sources, boundaries and verification.\n",
        "CURRENT_STATE.md": f"# Current State\n\nupdated: {date.today().isoformat()}\nstatus: draft\n\n```text\nactive_surface: {name}\ncurrent_next: verify first RepoKernel cycle\n```\n",
        "process/FIRST_PACKET.md": f"# First Packet\n\nobjective: establish RepoKernel continuity for {name}\nintent: {intent}\n",
    }
    if _level_at_least(level, "L1"):
        files.update({
            "README.md": f"# {name}\n\n{product}\n\nIntent: {intent}\n",
            "sources/bootstrap/SOURCE_ATLAS_v1.0.md": f"# Source Atlas\n\n| Path | Role |\n| --- | --- |\n| `README.md` | project definition |\n| `CURRENT_STATE.md` | active state |\n",
            f"skills/{slug}-semantic-kernel/SKILL.md": f"---\nname: {slug}-semantic-kernel\ndescription: Preserve continuity, sources and boundaries for {name}.\n---\n\n# {name} Semantic Kernel\n",
        })
    if _level_at_least(level, "L2"):
        files.update({
            "repokernel.json": "{\n  \"schema\": \"repokernel.manifest.v1\",\n  \"readiness_target\": \"L2\"\n}\n",
            "registry/skills.json": "{\n  \"schema\": \"repokernel.skill-registry.v1\",\n  \"skills\": []\n}\n",
            "process/evidence/README.md": "# Evidence\n\nValidation records for this project kernel.\n",
            "process/deltas/README.md": "# Deltas\n\nDurable accepted changes only.\n",
        })
    return files


def _level_at_least(level: str, minimum: str) -> bool:
    return LEVEL_ORDER.index(level) >= LEVEL_ORDER.index(minimum)


def _reason_for(path: str, action: str) -> str:
    if action == "propose_update":
        return f"{path} already exists; existing authority requires reviewable update"
    if action == "conflict":
        return f"{path} already exists and cannot be overwritten silently"
    return "required by selected readiness level"


def _slug(value: str) -> str:
    return "".join(ch.lower() if ch.isalnum() else "-" for ch in value).strip("-")
