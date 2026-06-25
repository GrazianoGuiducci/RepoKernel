"""Read-only target snapshots for content-aware planning."""
from __future__ import annotations

import hashlib
from pathlib import Path
from typing import Any

from .canonical import canonical_hash
from .paths import normalize_relative_path


TEXT_SUFFIXES = {
    ".md",
    ".txt",
    ".json",
    ".yaml",
    ".yml",
    ".toml",
    ".py",
    ".js",
    ".ts",
    ".tsx",
    ".jsx",
}


def build_target_snapshot(root: Path) -> dict[str, Any]:
    """Return a read-only snapshot of eligible repository files."""
    root = root.expanduser().resolve()
    entries: list[dict[str, Any]] = []
    warnings: list[dict[str, str]] = []
    if not root.is_dir():
        return {
            "schema": "repokernel.target-snapshot.v1",
            "target_snapshot_id": canonical_hash({"missing": str(root)}),
            "root": str(root),
            "tree_hash": canonical_hash([]),
            "entries": [],
            "warnings": [{"kind": "missing", "path": str(root)}],
        }

    seen_lower: dict[str, str] = {}
    for path in sorted(root.rglob("*")):
        rel = path.relative_to(root).as_posix()
        if _excluded(rel):
            continue
        try:
            safe_rel = normalize_relative_path(rel)
        except ValueError as exc:
            warnings.append({"kind": "unsafe_path", "path": rel, "message": str(exc)})
            continue
        lowered = safe_rel.lower()
        if lowered in seen_lower and seen_lower[lowered] != safe_rel:
            warnings.append({"kind": "case_collision", "path": safe_rel, "other": seen_lower[lowered]})
        else:
            seen_lower[lowered] = safe_rel
        if path.is_symlink():
            warnings.append({"kind": "symlink", "path": safe_rel})
            kind = "symlink"
            content_hash = None
        elif path.is_dir():
            kind = "directory"
            content_hash = None
        elif path.is_file():
            kind = "file"
            content_hash = _hash_text_file(path) if _eligible_text(path) else None
        else:
            kind = "other"
            content_hash = None
        entries.append({
            "path": safe_rel,
            "kind": kind,
            "content_hash": content_hash,
            "authority_role": _authority_role(safe_rel),
        })
    tree_hash = canonical_hash(entries)
    return {
        "schema": "repokernel.target-snapshot.v1",
        "target_snapshot_id": tree_hash,
        "root": str(root),
        "tree_hash": tree_hash,
        "entries": entries,
        "warnings": warnings,
    }


def snapshot_entries(snapshot: dict[str, Any]) -> dict[str, dict[str, Any]]:
    entries = snapshot.get("entries", [])
    if not isinstance(entries, list):
        return {}
    return {entry["path"]: entry for entry in entries if isinstance(entry, dict) and isinstance(entry.get("path"), str)}


def _excluded(rel: str) -> bool:
    return rel == ".git" or rel.startswith(".git/")


def _eligible_text(path: Path) -> bool:
    return path.suffix.lower() in TEXT_SUFFIXES


def _hash_text_file(path: Path) -> str:
    text = path.read_text(encoding="utf-8").replace("\r\n", "\n").replace("\r", "\n")
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def _authority_role(path: str) -> str:
    if path.startswith(".repokernel/"):
        return "canonical_project_kernel"
    if path in {"AGENTS.md", "README.md", "CURRENT_STATE.md"}:
        return "root_adapter_or_project_authority"
    return "target_project_file"
