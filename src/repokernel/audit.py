"""Evidence-aware read-only audit for RepoKernel projects."""
from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any


ID = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
STATES = {"draft", "candidate", "accepted", "promoted", "private", "residue"}
PROFILES = {
    "reentry-core": (["AGENTS.md", "CURRENT_STATE.md", "process/FIRST_PACKET.md"], [], "structure_ready"),
    "project": (
        [
            "README.md",
            "AGENTS.md",
            "CURRENT_STATE.md",
            "sources/bootstrap/PROJECT_INSTRUCTIONS_v1.0.txt",
            "sources/bootstrap/SOURCE_ATLAS_v1.0.md",
            "process/FIRST_PACKET.md",
        ],
        ["skills", "sources/bootstrap", "process"],
        "semantic_ready",
    ),
    "skill-repo": (
        [
            "README.md",
            "AGENTS.md",
            "CURRENT_STATE.md",
            "sources/bootstrap/PROJECT_INSTRUCTIONS_v1.0.txt",
            "sources/bootstrap/SOURCE_ATLAS_v1.0.md",
            "process/FIRST_PACKET.md",
        ],
        ["skills", "sources/bootstrap", "process", "examples"],
        "semantic_ready",
    ),
    "repokernel-source": (
        [
            "README.md",
            "AGENTS.md",
            "CURRENT_STATE.md",
            "repokernel.json",
            "registry/skills.json",
            "docs/readiness-levels.md",
            "docs/runtime-adapters.md",
            "process/FIRST_PACKET.md",
            "process/deltas/README.md",
            "process/evidence/README.md",
            "process/evidence/LOCAL_VALIDATION.md",
        ],
        ["docs", "skills", "scripts", "process/deltas", "process/evidence", "registry"],
        "evolution_ready",
    ),
    "project-kernel": (
        [
            ".repokernel/state/CURRENT_STATE.md",
            ".repokernel/packets/FIRST_PACKET.md",
            ".repokernel/sources/SOURCE_ATLAS.md",
        ],
        [".repokernel"],
        "project_kernel_ready",
    ),
}


def audit(root: Path, profile: str) -> dict[str, Any]:
    """Return a read-only RepoKernel audit report."""
    files, dirs, target = PROFILES[profile]
    checks: list[dict[str, Any]] = []
    for rel in files:
        ok = (root / rel).is_file() and bool(_read(root / rel).strip())
        _check(checks, "file", ok, rel, "populated" if ok else "missing or empty")
    for rel in dirs:
        _check(checks, "directory", (root / rel).is_dir(), rel, "present" if (root / rel).is_dir() else "missing")

    state = _read(root / "CURRENT_STATE.md").lower()
    for key in ("active_surface", "current_next", "boundary", "first_safe_action"):
        _check(checks, "state", key in state, "CURRENT_STATE.md", f"contains {key}")

    packet = _read(root / "process/FIRST_PACKET.md").lower()
    for key in ("objective", "source", "boundary", "first_safe_action", "memory delta"):
        _check(checks, "packet", key in packet, "process/FIRST_PACKET.md", f"contains {key}")

    structure_ready = all(c["ok"] for c in checks if c["id"] in {"file", "directory"})
    if profile != "reentry-core":
        _audit_skills(root, checks)
        _audit_atlas(root, checks)

    semantic_ready = structure_ready and all(c["ok"] for c in checks)
    if profile == "repokernel-source":
        _audit_repokernel_source(root, checks)

    evolution_ready = profile == "repokernel-source" and structure_ready and all(c["ok"] for c in checks)
    repository_structure_ready = structure_ready
    contract_conformant = _contract_conformant(root, checks) if profile == "repokernel-source" else True
    planner_conformant = _planner_conformant(root, checks) if profile == "repokernel-source" else True
    project_kernel_ready = structure_ready and all(c["ok"] for c in checks)
    distribution_ready = False
    readiness = {
        "level": "L2" if evolution_ready else "L1" if semantic_ready else "L0" if structure_ready else "none",
        "structure_ready": structure_ready,
        "semantic_ready": semantic_ready,
        "evolution_ready": evolution_ready,
        "repository_structure_ready": repository_structure_ready,
        "contract_conformant": contract_conformant,
        "planner_conformant": planner_conformant,
        "project_kernel_ready": project_kernel_ready,
        "distribution_ready": distribution_ready,
    }
    failed = [c for c in checks if not c["ok"]]
    return {
        "schema": "repokernel.audit.v2",
        "path": str(root),
        "profile": profile,
        "target": target,
        "ready": readiness[target],
        "readiness": readiness,
        "failed": failed,
        "checks": checks,
    }


def inspect_repository(root: Path) -> dict[str, Any]:
    """Return a compact read-only repository inspection."""
    paths = {
        "git": (root / ".git").exists(),
        "root_agents": (root / "AGENTS.md").is_file(),
        "root_current_state": (root / "CURRENT_STATE.md").is_file(),
        "legacy_first_packet": (root / "process/FIRST_PACKET.md").is_file(),
        "repokernel_control_plane": (root / ".repokernel").is_dir(),
        "repokernel_state": (root / ".repokernel/state/CURRENT_STATE.md").is_file(),
        "repokernel_packet": (root / ".repokernel/packets/FIRST_PACKET.md").is_file(),
    }
    likely_mode = "existing_repository_retrofit" if paths["git"] or paths["root_agents"] or paths["root_current_state"] else "new_repository"
    return {
        "schema": "repokernel.inspect.v1",
        "path": str(root),
        "exists": root.is_dir(),
        "likely_mode": likely_mode,
        "paths": paths,
        "boundary": "read_only",
    }


def report_as_json(report: dict[str, Any]) -> str:
    return json.dumps(report, indent=2, ensure_ascii=False)


def _audit_skills(root: Path, checks: list[dict[str, Any]]) -> None:
    skill_paths = sorted((root / "skills").glob("*/SKILL.md")) if (root / "skills").is_dir() else []
    _check(checks, "skills", bool(skill_paths), "skills", "at least one skill")
    for path in skill_paths:
        meta = _frontmatter(_read(path))
        rel = str(path.relative_to(root))
        _check(checks, "skill-frontmatter", bool(meta), rel, "valid frontmatter")
        if meta:
            name = meta.get("name", "")
            desc = meta.get("description", "")
            _check(checks, "skill-name", bool(ID.fullmatch(name)), rel, "valid id")
            _check(checks, "skill-path", path.parent.name == name, rel, "path matches id")
            _check(checks, "skill-description", len(desc) > 12, rel, "substantive description")


def _audit_atlas(root: Path, checks: list[dict[str, Any]]) -> None:
    atlas = _read(root / "sources/bootstrap/SOURCE_ATLAS_v1.0.md")
    for rel in re.findall(r"\|\s*`([^`*<>]+)`\s*\|", atlas):
        _check(checks, "atlas", (root / rel).exists(), "sources/bootstrap/SOURCE_ATLAS_v1.0.md", f"path exists: {rel}")


def _audit_repokernel_source(root: Path, checks: list[dict[str, Any]]) -> None:
    objects: dict[str, dict[str, Any]] = {}
    for rel in ("repokernel.json", "registry/skills.json"):
        try:
            data = json.loads(_read(root / rel))
            ok = isinstance(data, dict)
        except json.JSONDecodeError:
            ok = False
            data = {}
        objects[rel] = data
        _check(checks, "json", ok, rel, "valid object")

    entries = objects.get("registry/skills.json", {}).get("skills", [])
    actual = {p.parent.name for p in (root / "skills").glob("*/SKILL.md")}
    registered = {e.get("id") for e in entries if isinstance(e, dict)}
    _check(checks, "registry-coverage", actual == registered, "registry/skills.json", "covers all skill directories")
    for entry in entries if isinstance(entries, list) else []:
        if not isinstance(entry, dict):
            _check(checks, "registry-entry", False, "registry/skills.json", "entry must be an object")
            continue
        skill_id = entry.get("id", "")
        path = entry.get("path", "")
        state = entry.get("state", "")
        evidence = entry.get("evidence", [])
        _check(checks, "registry-id", bool(ID.fullmatch(skill_id)), "registry/skills.json", f"valid id: {skill_id}")
        _check(checks, "registry-path", isinstance(path, str) and (root / path).is_file(), "registry/skills.json", f"path exists: {path}")
        _check(checks, "registry-state", state in STATES, "registry/skills.json", f"valid state: {state}")
        valid_evidence = isinstance(evidence, list) and all(isinstance(item, str) and (root / item).exists() for item in evidence)
        _check(checks, "registry-evidence", valid_evidence, "registry/skills.json", f"evidence resolves for: {skill_id}")

    _check(checks, "schema-validation-module", (root / "src/repokernel/schema_validation.py").is_file(), "src/repokernel/schema_validation.py", "present")
    _check(checks, "snapshot-module", (root / "src/repokernel/snapshot.py").is_file(), "src/repokernel/snapshot.py", "present")
    _check(checks, "schema-parity-tests", (root / "tests/unit/test_schema_validator_parity.py").is_file(), "tests/unit/test_schema_validator_parity.py", "present")


def _contract_conformant(root: Path, checks: list[dict[str, Any]]) -> bool:
    schema_files = sorted((root / "schemas").glob("*.schema.json"))
    ok = bool(schema_files) and (root / "src/repokernel/schema_validation.py").is_file()
    _check(checks, "contract-conformant", ok, "schemas", "schemas executed by schema_validation module")
    return ok


def _planner_conformant(root: Path, checks: list[dict[str, Any]]) -> bool:
    planner = _read(root / "src/repokernel/planner.py")
    ok = all(token in planner for token in ("target_snapshot_hash", "before_hash", "after_hash", "apply_policy"))
    _check(checks, "planner-conformant", ok, "src/repokernel/planner.py", "target-bound plan fields present")
    return ok


def _read(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except (OSError, UnicodeError):
        return ""


def _check(checks: list[dict[str, Any]], name: str, ok: bool, path: str, message: str) -> None:
    checks.append({"id": name, "ok": bool(ok), "path": path, "message": message})


def _frontmatter(value: str) -> dict[str, str] | None:
    lines = value.splitlines()
    if not lines or lines[0].strip() != "---":
        return None
    try:
        end = next(i for i, line in enumerate(lines[1:], 1) if line.strip() == "---")
    except StopIteration:
        return None
    data = {}
    for line in lines[1:end]:
        if ":" in line:
            key, val = line.split(":", 1)
            data[key.strip()] = val.strip().strip("\"'")
    return data
