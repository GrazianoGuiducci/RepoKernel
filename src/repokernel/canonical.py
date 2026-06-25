"""Canonical JSON serialization and hashing for RepoKernel contracts."""
from __future__ import annotations

import hashlib
import json
from typing import Any


import re


EXTENSION_KEY = re.compile(r"^[a-z0-9][a-z0-9_-]*(?:\.[a-z0-9][a-z0-9_-]*)+$")


def canonical_dumps(value: Any) -> str:
    """Return deterministic JSON for hashing and equality checks."""
    return json.dumps(value, allow_nan=False, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def canonical_hash(value: Any) -> str:
    """Return a stable SHA-256 hash for a canonical JSON value."""
    return hashlib.sha256(canonical_dumps(value).encode("utf-8")).hexdigest()


def validate_namespaced_extensions(extensions: dict[str, Any] | None) -> list[str]:
    """Return validation errors for extension blocks.

    Extensions are preserved as opaque data. Core validators and planners do
    not infer authority, capabilities or write permissions from extension
    payloads. Keys must be namespaced as `namespace.key`.
    """
    errors: list[str] = []
    if extensions is None:
        return errors
    if not isinstance(extensions, dict):
        return ["extensions must be an object"]
    for key in extensions:
        if not isinstance(key, str) or not EXTENSION_KEY.fullmatch(key):
            errors.append(f"extension key must be namespaced: {key}")
    return errors
