"""Path safety helpers for RepoKernel plans."""
from __future__ import annotations

from pathlib import PurePosixPath
import re


FORBIDDEN_PARTS = {"", ".", ".."}
RESERVED_WINDOWS_NAMES = {
    "CON", "PRN", "AUX", "NUL",
    "COM1", "COM2", "COM3", "COM4", "COM5", "COM6", "COM7", "COM8", "COM9",
    "LPT1", "LPT2", "LPT3", "LPT4", "LPT5", "LPT6", "LPT7", "LPT8", "LPT9",
}
CONTROL_CHARS = re.compile(r"[\x00-\x1f\x7f]")


def normalize_relative_path(path: str) -> str:
    """Normalize and validate a target-relative POSIX path."""
    if not isinstance(path, str):
        raise ValueError("path must be a string")
    raw = path.replace("\\", "/").strip()
    if not raw:
        raise ValueError("path must not be empty")
    if CONTROL_CHARS.search(raw):
        raise ValueError(f"path contains control character: {path!r}")
    if raw.startswith("//"):
        raise ValueError(f"path must not be a UNC path: {path}")
    if ":" in raw:
        raise ValueError(f"path must not contain drive or stream syntax: {path}")
    pure = PurePosixPath(raw)
    if pure.is_absolute():
        raise ValueError(f"path must be relative: {path}")
    if any(part in FORBIDDEN_PARTS for part in pure.parts):
        raise ValueError(f"path contains forbidden segment: {path}")
    for part in pure.parts:
        stem = part.split(".", 1)[0].upper()
        if stem in RESERVED_WINDOWS_NAMES:
            raise ValueError(f"path contains reserved Windows name: {path}")
    return str(pure)
