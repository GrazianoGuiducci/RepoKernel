#!/usr/bin/env python3
"""Create a repository-shaped skill starter."""

from __future__ import annotations

import argparse
from pathlib import Path


def write_if_missing(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not path.exists():
        path.write_text(content, encoding="utf-8")


def slugify(name: str) -> str:
    return "".join(ch.lower() if ch.isalnum() else "-" for ch in name).strip("-").replace("--", "-")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--path", required=True)
    parser.add_argument("--name", required=True)
    parser.add_argument("--mission", required=True)
    args = parser.parse_args()

    root = Path(args.path).resolve()
    slug = slugify(args.name)
    root.mkdir(parents=True, exist_ok=True)

    write_if_missing(root / "README.md", f"# {args.name}\n\n{args.mission}\n")
    write_if_missing(root / "AGENTS.md", "# Skill Repo Gate\n\nRead `CURRENT_STATE.md` and the skill file before editing.\n")
    write_if_missing(root / "CURRENT_STATE.md", f"# Current State\n\nskill: {args.name}\nstatus: draft\nnext: create validation example\n")
    write_if_missing(root / f"skills/{slug}/SKILL.md", f"---\nname: {slug}\ndescription: {args.mission}\n---\n\n# {args.name}\n\n## Purpose\n\n{args.mission}\n")
    write_if_missing(root / "sources/bootstrap/PROJECT_INSTRUCTIONS_v1.0.txt", f"Create and validate the {args.name} skill.\n")
    write_if_missing(root / "process/FIRST_PACKET.md", f"# First Packet\n\nobjective: {args.mission}\n")
    write_if_missing(root / "examples/README.md", "# Examples\n\nAdd one minimal validation example.\n")
    print(f"created or verified skill repo at {root}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

