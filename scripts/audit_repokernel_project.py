#!/usr/bin/env python3
"""Read-only RepoKernel structure audit."""

from __future__ import annotations

import argparse
import json
import subprocess
from pathlib import Path


REQUIRED = {
    "entry_gate": ["AGENTS.md"],
    "current_state": ["CURRENT_STATE.md"],
    "project_instructions": ["sources/bootstrap/PROJECT_INSTRUCTIONS_v1.0.txt"],
    "source_atlas": ["sources/bootstrap/SOURCE_ATLAS_v1.0.md"],
    "first_packet": ["process/FIRST_PACKET.md"],
}

DIRS = ["docs", "templates", "skills", "scripts", "examples", "process", "sources/bootstrap"]


def git_status(root: Path) -> str:
    if not (root / ".git").exists():
        return "not_a_git_repo"
    result = subprocess.run(
        ["git", "status", "--short", "--branch"],
        cwd=str(root),
        text=True,
        capture_output=True,
        check=False,
    )
    return result.stdout.strip() if result.returncode == 0 else result.stderr.strip()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--path", required=True)
    args = parser.parse_args()

    root = Path(args.path).resolve()
    if not root.is_dir():
        raise SystemExit(f"not a directory: {root}")

    present: dict[str, list[str]] = {}
    missing: dict[str, list[str]] = {}

    for key, paths in REQUIRED.items():
        found = [p for p in paths if (root / p).exists()]
        if found:
            present[key] = found
        else:
            missing[key] = [paths[0]]

    skill_files = sorted(str(p.relative_to(root)) for p in (root / "skills").glob("*/SKILL.md")) if (root / "skills").exists() else []
    if skill_files:
        present["skills"] = skill_files
    else:
        missing["skills"] = ["skills/<name>/SKILL.md"]

    missing_dirs = [d for d in DIRS if not (root / d).is_dir()]
    if missing_dirs:
        missing["directories"] = missing_dirs

    result = {
        "path": str(root),
        "git_state": git_status(root),
        "repokernel_ready": not missing,
        "present": present,
        "missing": missing,
        "recommended_next_action": "add only missing layers; avoid private material in public surfaces",
    }
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

