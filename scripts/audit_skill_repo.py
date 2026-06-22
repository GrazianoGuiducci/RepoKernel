#!/usr/bin/env python3
"""Evidence audit for repository-shaped skills."""
from __future__ import annotations
import argparse, json, re
from pathlib import Path
from audit_repokernel_project import audit, read

RANK = {"draft": 0, "candidate": 1}

def declared_state(root):
    match = re.search(r"(?im)^\s*status\s*:\s*([a-z_-]+)\s*$", read(root / "CURRENT_STATE.md"))
    value = match.group(1).lower().replace("_", "-") if match else "draft"
    return value if value in RANK else "draft"

def substantive(root, folder):
    base = root / folder
    if not base.is_dir(): return []
    result = []
    for path in base.rglob("*"):
        if not path.is_file() or path.name.lower() in {"readme.md", ".gitkeep"}: continue
        value = read(path).strip().lower()
        if value and "todo" not in value and "add one" not in value:
            result.append(str(path.relative_to(root)))
    return sorted(result)

def validation(root):
    path = root / "validation/result.json"
    if path.is_file():
        try:
            data = json.loads(read(path))
            if isinstance(data, dict) and data.get("passed") is True: return ["validation/result.json"]
        except json.JSONDecodeError: pass
    return [p for p in substantive(root, "tests") if p.endswith((".py", ".js", ".ts", ".json", ".md"))]

def main():
    parser = argparse.ArgumentParser(); parser.add_argument("--path", required=True); parser.add_argument("--json", action="store_true"); args = parser.parse_args()
    root = Path(args.path).expanduser().resolve()
    if not root.is_dir(): raise SystemExit(f"not a directory: {root}")
    base = audit(root, "skill-repo")
    declared = declared_state(root)
    examples = substantive(root, "examples"); tests = validation(root)
    supported = "candidate" if base["readiness"]["semantic_ready"] and examples and tests else "draft"
    overclaim = RANK[declared] > RANK[supported]
    underclaim = RANK[declared] < RANK[supported]
    result = {
        "schema": "repokernel.skill-audit.v2", "path": str(root),
        "declared_state": declared, "supported_state": supported,
        "classification": supported if overclaim else declared,
        "semantic_ready": base["readiness"]["semantic_ready"],
        "overclaim": overclaim, "underclaim": underclaim,
        "evidence": {"examples": examples, "validation": tests},
        "base_failures": base["failed"],
        "next_action": "add evidence or lower the declared state" if overclaim else "record a reviewed lifecycle delta" if underclaim else "continue with one bounded validation step",
    }
    if args.json: print(json.dumps(result, indent=2, ensure_ascii=False))
    else: print(f"declared: {declared}\nsupported: {supported}\noverclaim: {overclaim}\nnext: {result['next_action']}")
    return 0 if result["semantic_ready"] and not overclaim else 1

if __name__ == "__main__": raise SystemExit(main())
