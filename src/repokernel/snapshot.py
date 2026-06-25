"""Read-only target snapshots for content-aware planning."""
from __future__ import annotations

import fnmatch
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

DEFAULT_EXCLUSIONS = {
    ".git": "repository_metadata",
    ".env": "credential_or_environment_file",
    ".env.*": "credential_or_environment_file",
    "*.pem": "private_key_material",
    "*.key": "private_key_material",
    "node_modules": "vendor_tree",
    ".venv": "virtual_environment",
    "venv": "virtual_environment",
    "__pycache__": "generated_cache",
    "build": "build_artifact",
    "dist": "build_artifact",
    ".pytest_cache": "generated_cache",
    ".mypy_cache": "generated_cache",
}


def build_target_snapshot(root: Path) -> dict[str, Any]:
    """Return a read-only snapshot of eligible repository files."""
    root = root.expanduser().resolve()
    entries: list[dict[str, Any]] = []
    excluded: list[dict[str, str]] = []
    warnings: list[dict[str, str]] = []
    if not root.is_dir():
        return {
            "schema": "repokernel.target-snapshot.v1",
            "target_snapshot_id": canonical_hash({"missing": str(root)}),
            "target_identity": canonical_hash({"root": str(root)}),
            "root": str(root),
            "tree_hash": canonical_hash([]),
            "entries": [],
            "excluded": [],
            "warnings": [{"kind": "missing", "path": str(root)}],
        }

    seen_lower: dict[str, str] = {}
    for path in sorted(root.rglob("*")):
        rel = path.relative_to(root).as_posix()
        reason = exclusion_reason(rel)
        if reason:
            excluded.append({"path": _redacted_path(rel), "reason": reason})
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
            if _eligible_text(path):
                try:
                    content_hash = _hash_text_file(path)
                except (OSError, UnicodeError) as exc:
                    warnings.append({"kind": "unreadable", "path": safe_rel, "message": type(exc).__name__})
                    content_hash = None
            else:
                content_hash = None
        else:
            kind = "other"
            content_hash = None
        entries.append({
            "path": safe_rel,
            "kind": kind,
            "content_hash": content_hash,
            "authority_role": _authority_role(safe_rel),
        })
    tree_hash = compute_tree_hash(entries)
    target_identity = canonical_hash({"root": str(root)})
    return {
        "schema": "repokernel.target-snapshot.v1",
        "target_snapshot_id": tree_hash,
        "target_identity": target_identity,
        "root": str(root),
        "tree_hash": tree_hash,
        "entries": entries,
        "excluded": excluded,
        "warnings": warnings,
    }


def snapshot_entries(snapshot: dict[str, Any]) -> dict[str, dict[str, Any]]:
    entries = snapshot.get("entries", [])
    if not isinstance(entries, list):
        return {}
    return {entry["path"]: entry for entry in entries if isinstance(entry, dict) and isinstance(entry.get("path"), str)}


def compute_tree_hash(entries: list[dict[str, Any]]) -> str:
    return canonical_hash(sorted(entries, key=lambda entry: entry.get("path", "")))


def snapshot_integrity_errors(snapshot: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    entries = snapshot.get("entries")
    if not isinstance(entries, list):
        return ["entries must be a list"]
    expected = compute_tree_hash(entries)
    if snapshot.get("tree_hash") != expected:
        errors.append("tree_hash does not match snapshot entries")
    if snapshot.get("target_snapshot_id") != expected:
        errors.append("target_snapshot_id does not match snapshot entries")
    return errors


def exclusion_reason(rel: str) -> str | None:
    parts = rel.split("/")
    for part in parts:
        if part in DEFAULT_EXCLUSIONS:
            return DEFAULT_EXCLUSIONS[part]
    name = parts[-1]
    for pattern, reason in DEFAULT_EXCLUSIONS.items():
        if "*" in pattern and fnmatch.fnmatch(name, pattern):
            return reason
    return None


def _eligible_text(path: Path) -> bool:
    return path.suffix.lower() in TEXT_SUFFIXES


def _hash_text_file(path: Path) -> str:
    text = path.read_text(encoding="utf-8").replace("\r\n", "\n").replace("\r", "\n")
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def _redacted_path(rel: str) -> str:
    reason = exclusion_reason(rel)
    if reason in {"credential_or_environment_file", "private_key_material"}:
        return "<withheld-sensitive-path>"
    return rel


def _authority_role(path: str) -> str:
    if path.startswith(".repokernel/"):
        return "canonical_project_kernel"
    if path in {"AGENTS.md", "README.md", "CURRENT_STATE.md"}:
        return "root_adapter_or_project_authority"
    return "target_project_file"
