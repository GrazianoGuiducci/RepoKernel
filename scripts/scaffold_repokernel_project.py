#!/usr/bin/env python3
"""Create a minimal RepoKernel project structure."""

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
    write_if_missing(root / "AGENTS.md", "# Agent Gate\n\nRead `CURRENT_STATE.md` before editing.\n")
    write_if_missing(
        root / "CURRENT_STATE.md",
        f"# Current State\n\nactive_surface: {args.name}\ncurrent_next: define first useful move\nboundary: do not publish or delete without confirmation\n",
    )
    write_if_missing(
        root / "sources/bootstrap/PROJECT_INSTRUCTIONS_v1.0.txt",
        f"Project: {args.name}\nMission: {args.mission}\nWork from current state, sources, boundary and next action.\n",
    )
    write_if_missing(
        root / "sources/bootstrap/SOURCE_ATLAS_v1.0.md",
        "# Source Atlas\n\n| Path | Role |\n| --- | --- |\n| `CURRENT_STATE.md` | active state |\n",
    )
    write_if_missing(
        root / f"skills/{slug}-semantic-kernel/SKILL.md",
        f"---\nname: {slug}-semantic-kernel\ndescription: Use when working in the {args.name} project.\n---\n\n# {args.name} Semantic Kernel\n\nRead current state first. Preserve useful deltas.\n",
    )
    write_if_missing(
        root / "process/FIRST_PACKET.md",
        f"# First Packet\n\nobjective: {args.mission}\nfirst_safe_action: audit current structure and define next move\n",
    )
    print(f"created or verified RepoKernel project at {root}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

