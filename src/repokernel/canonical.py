"""Canonical JSON serialization and hashing for RepoKernel contracts."""
from __future__ import annotations

import hashlib
import json
from typing import Any


AUTHORITY_KEYS = {"authority", "authority_mode", "autonomy", "autonomy_level"}
WRITE_ACTIONS = {"write", "project_write", "external_action", "publish", "deploy"}


def canonical_dumps(value: Any) -> str:
    """Return deterministic JSON for hashing and equality checks."""
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def canonical_hash(value: Any) -> str:
    """Return a stable SHA-256 hash for a canonical JSON value."""
    return hashlib.sha256(canonical_dumps(value).encode("utf-8")).hexdigest()


def validate_namespaced_extensions(extensions: dict[str, Any] | None) -> list[str]:
    """Return validation errors for extension blocks.

    Extensions are preserved, but they cannot raise authority or request write
    actions. Keys must be namespaced as `namespace.key`.
    """
    errors: list[str] = []
    if extensions is None:
        return errors
    if not isinstance(extensions, dict):
        return ["extensions must be an object"]
    for key, value in extensions.items():
        if "." not in key:
            errors.append(f"extension key must be namespaced: {key}")
        errors.extend(_authority_errors(value, path=f"extensions.{key}"))
    return errors


def _authority_errors(value: Any, *, path: str) -> list[str]:
    errors: list[str] = []
    if isinstance(value, dict):
        for key, nested in value.items():
            next_path = f"{path}.{key}"
            lowered = str(key).lower()
            if lowered in AUTHORITY_KEYS and str(nested).lower() not in {"none", "read", "propose", "proposal_only", "a0", "a1"}:
                errors.append(f"extension cannot raise authority at {next_path}")
            if lowered in {"action", "action_class"} and str(nested).lower() in WRITE_ACTIONS:
                errors.append(f"extension cannot request write action at {next_path}")
            errors.extend(_authority_errors(nested, path=next_path))
    elif isinstance(value, list):
        for index, nested in enumerate(value):
            errors.extend(_authority_errors(nested, path=f"{path}[{index}]"))
    return errors
