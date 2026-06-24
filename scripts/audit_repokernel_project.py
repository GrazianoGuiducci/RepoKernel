#!/usr/bin/env python3
"""Compatibility wrapper for the package audit command."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from repokernel.audit import PROFILES, audit

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--path", required=True)
    parser.add_argument("--profile", choices=sorted(PROFILES), default="project")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    root = Path(args.path).expanduser().resolve()
    if not root.is_dir():
        raise SystemExit(f"not a directory: {root}")
    result = audit(root, args.profile)
    if args.json:
        print(json.dumps(result, indent=2, ensure_ascii=False))
    else:
        print(f"profile: {args.profile}\nreadiness: {result['readiness']['level']}")
        for item in result["failed"]:
            print(f"FAIL {item['path']}: {item['message']}")
    return 0 if result["ready"] else 1

if __name__ == "__main__":
    raise SystemExit(main())
