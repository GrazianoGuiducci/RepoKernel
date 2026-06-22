#!/usr/bin/env python3
"""Evidence-aware read-only audit for RepoKernel projects."""
from __future__ import annotations
import argparse, json, re
from pathlib import Path

ID = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
PROFILES = {
    "reentry-core": (["AGENTS.md", "CURRENT_STATE.md", "process/FIRST_PACKET.md"], [], "structure_ready"),
    "project": (["README.md", "AGENTS.md", "CURRENT_STATE.md", "sources/bootstrap/PROJECT_INSTRUCTIONS_v1.0.txt", "sources/bootstrap/SOURCE_ATLAS_v1.0.md", "process/FIRST_PACKET.md"], ["skills", "sources/bootstrap", "process"], "semantic_ready"),
    "skill-repo": (["README.md", "AGENTS.md", "CURRENT_STATE.md", "sources/bootstrap/PROJECT_INSTRUCTIONS_v1.0.txt", "sources/bootstrap/SOURCE_ATLAS_v1.0.md", "process/FIRST_PACKET.md"], ["skills", "sources/bootstrap", "process", "examples"], "semantic_ready"),
    "repokernel-source": (["README.md", "AGENTS.md", "CURRENT_STATE.md", "repokernel.json", "registry/skills.json", "docs/readiness-levels.md", "docs/runtime-adapters.md", "process/FIRST_PACKET.md", "process/deltas/README.md", "process/evidence/README.md", "tests/test_repokernel.py"], ["docs", "skills", "scripts", "process/deltas", "process/evidence", "registry", "tests"], "evolution_ready"),
}

def read(path):
    try: return path.read_text(encoding="utf-8")
    except (OSError, UnicodeError): return ""

def check(checks, name, ok, path, message):
    checks.append({"id": name, "ok": bool(ok), "path": path, "message": message})

def frontmatter(value):
    lines = value.splitlines()
    if not lines or lines[0].strip() != "---": return None
    try: end = next(i for i, line in enumerate(lines[1:], 1) if line.strip() == "---")
    except StopIteration: return None
    data = {}
    for line in lines[1:end]:
        if ":" in line:
            key, val = line.split(":", 1); data[key.strip()] = val.strip().strip("\"'")
    return data

def audit(root, profile):
    files, dirs, target = PROFILES[profile]
    checks = []
    for rel in files:
        ok = (root / rel).is_file() and bool(read(root / rel).strip())
        check(checks, "file", ok, rel, "populated" if ok else "missing or empty")
    for rel in dirs:
        check(checks, "directory", (root / rel).is_dir(), rel, "present" if (root / rel).is_dir() else "missing")
    state = read(root / "CURRENT_STATE.md").lower()
    for key in ("active_surface", "current_next", "boundary", "first_safe_action"):
        check(checks, "state", key in state, "CURRENT_STATE.md", f"contains {key}")
    packet = read(root / "process/FIRST_PACKET.md").lower()
    for key in ("objective", "source", "boundary", "first_safe_action", "memory delta"):
        check(checks, "packet", key in packet, "process/FIRST_PACKET.md", f"contains {key}")
    structure_ready = all(c["ok"] for c in checks if c["id"] in {"file", "directory"})
    if profile != "reentry-core":
        skill_paths = sorted((root / "skills").glob("*/SKILL.md")) if (root / "skills").is_dir() else []
        check(checks, "skills", skill_paths, "skills", "at least one skill")
        for path in skill_paths:
            meta = frontmatter(read(path)); rel = str(path.relative_to(root))
            check(checks, "skill-frontmatter", meta, rel, "valid frontmatter")
            if meta:
                name = meta.get("name", ""); desc = meta.get("description", "")
                check(checks, "skill-name", ID.fullmatch(name), rel, "valid id")
                check(checks, "skill-path", path.parent.name == name, rel, "path matches id")
                check(checks, "skill-description", len(desc) > 12, rel, "substantive description")
        atlas = read(root / "sources/bootstrap/SOURCE_ATLAS_v1.0.md")
        for rel in re.findall(r"\|\s*`([^`*<>]+)`\s*\|", atlas):
            check(checks, "atlas", (root / rel).exists(), "sources/bootstrap/SOURCE_ATLAS_v1.0.md", f"path exists: {rel}")
    semantic_ready = structure_ready and all(c["ok"] for c in checks)
    if profile == "repokernel-source":
        objects = {}
        for rel in ("repokernel.json", "registry/skills.json"):
            try: data = json.loads(read(root / rel)); ok = isinstance(data, dict)
            except json.JSONDecodeError: ok = False; data = {}
            objects[rel] = data
            check(checks, "json", ok, rel, "valid object")
        entries = objects.get("registry/skills.json", {}).get("skills", [])
        actual = {p.parent.name for p in (root / "skills").glob("*/SKILL.md")}
        registered = {e.get("id") for e in entries if isinstance(e, dict)}
        check(checks, "registry-coverage", actual == registered, "registry/skills.json", "covers all skill directories")
    evolution_ready = profile == "repokernel-source" and structure_ready and all(c["ok"] for c in checks)
    readiness = {"level": "L2" if evolution_ready else "L1" if semantic_ready else "L0" if structure_ready else "none", "structure_ready": structure_ready, "semantic_ready": semantic_ready, "evolution_ready": evolution_ready}
    failed = [c for c in checks if not c["ok"]]
    return {"schema": "repokernel.audit.v2", "path": str(root), "profile": profile, "target": target, "ready": readiness[target], "readiness": readiness, "failed": failed, "checks": checks}

def main():
    parser = argparse.ArgumentParser(); parser.add_argument("--path", required=True); parser.add_argument("--profile", choices=sorted(PROFILES), default="project"); parser.add_argument("--json", action="store_true"); args = parser.parse_args()
    root = Path(args.path).expanduser().resolve()
    if not root.is_dir(): raise SystemExit(f"not a directory: {root}")
    result = audit(root, args.profile)
    if args.json: print(json.dumps(result, indent=2, ensure_ascii=False))
    else:
        print(f"profile: {args.profile}\nreadiness: {result['readiness']['level']}")
        for item in result["failed"]: print(f"FAIL {item['path']}: {item['message']}")
    return 0 if result["ready"] else 1

if __name__ == "__main__": raise SystemExit(main())
