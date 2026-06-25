"""RepoKernel package version."""

from __future__ import annotations

try:
    from importlib.metadata import PackageNotFoundError, version
except ImportError:  # pragma: no cover - Python 3.11+ has importlib.metadata
    PackageNotFoundError = Exception  # type: ignore[assignment]
    version = None  # type: ignore[assignment]


FALLBACK_VERSION = "0.3.0.dev0"


def package_version() -> str:
    if version is None:
        return FALLBACK_VERSION
    try:
        return version("repokernel")
    except PackageNotFoundError:
        return FALLBACK_VERSION
