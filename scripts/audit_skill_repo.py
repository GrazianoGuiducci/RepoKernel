#!/usr/bin/env python3
"""Read-only audit for repository-shaped skills."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--path", required=True)
    args = parser.parse_args()

    root = Path(args.path).resolve()
    if not root.is_dir():
        raise SystemExit(f"not a directory: {root}")

    checks = {
        "entry_gate": (root / "AGENTS.md").exists(),
        "current_state": (root / "CURRENT_STATE.md").exists(),
        "skill_file": any((root / "skills").glob("*/SKILL.md")) if (root / "skills").exists() else False,
        "first_packet": (root / "process/FIRST_PACKET.md").exists(),
        "examples": (root / "examples").exists(),
    }
    missing = [name for name, ok in checks.items() if not ok]
    classification = "candidate" if not missing else "draft"
    print(json.dumps({"path": str(root), "classification": classification, "checks": checks, "missing": missing}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

