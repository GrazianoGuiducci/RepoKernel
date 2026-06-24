"""Path safety helpers for RepoKernel plans."""
from __future__ import annotations

from pathlib import PurePosixPath


FORBIDDEN_PARTS = {"", ".", ".."}


def normalize_relative_path(path: str) -> str:
    """Normalize and validate a target-relative POSIX path."""
    raw = path.replace("\\", "/").strip()
    pure = PurePosixPath(raw)
    if pure.is_absolute():
        raise ValueError(f"path must be relative: {path}")
    if any(part in FORBIDDEN_PARTS for part in pure.parts):
        raise ValueError(f"path contains forbidden segment: {path}")
    return str(pure)
