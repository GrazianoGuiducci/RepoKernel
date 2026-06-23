#!/usr/bin/env python3
"""Shared generation and validation helpers for RepoKernel seeds."""
from __future__ import annotations

import json
import re
import unicodedata
from datetime import date
from pathlib import Path
from typing import Mapping

VALID_ID = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
LEVELS = ("L0", "L1", "L2", "L3")


def slugify(value: str) -> str:
    normalized = unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode("ascii")
    slug = re.sub(r"[^a-z0-9]+", "-", normalized.strip().lower()).strip("-")
    if not slug or not VALID_ID.fullmatch(slug):
        raise ValueError("name must produce a non-empty ASCII kebab-case identifier")
    return slug


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except (OSError, UnicodeError):
        return ""


def parse_frontmatter(value: str) -> dict[str, str] | None:
    lines = value.splitlines()
    if not lines or lines[0].strip() != "---":
        return None
    try:
        end = next(i for i, line in enumerate(lines[1:], 1) if line.strip() == "---")
    except StopIteration:
        return None
    data: dict[str, str] = {}
    for line in lines[1:end]:
        if ":" not in line or line.lstrip().startswith("#"):
            continue
        key, raw = line.split(":", 1)
        data[key.strip()] = raw.strip().strip("\"'")
    return data


def write_plan(root: Path, plan: Mapping[str, str], *, dry_run: bool, merge: bool) -> dict[str, object]:
    if root.exists() and not root.is_dir():
        raise ValueError(f"target is not a directory: {root}")
    if root.exists() and any(root.iterdir()) and not merge:
        raise ValueError("target directory is not empty; use --merge to add missing files")

    created: list[str] = []
    unchanged: list[str] = []
    conflicts: list[str] = []
    for relative, content in plan.items():
        path = root / relative
        if path.exists():
            if path.is_file() and read_text(path) == content:
                unchanged.append(relative)
            else:
                conflicts.append(relative)
            continue
        created.append(relative)
        if not dry_run:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding="utf-8")

    return {
        "path": str(root),
        "dry_run": dry_run,
        "created": created,
        "unchanged": unchanged,
        "conflicts": conflicts,
        "ok": not conflicts,
    }


def _state(name: str, status: str, next_action: str) -> str:
    return f"""# Current State

updated: {date.today().isoformat()}
status: {status}

## Active Surface

```text
active_surface: {name}
current_next: {next_action}
```

## Boundary

```text
can_change: project-local public-safe files within the active task
needs_confirmation: publish, deploy, delete, change mission, enable runtime writes
must_not_touch: credentials, private logs, unrelated repositories
```

## First Safe Action

```text
first_safe_action: read the source atlas and execute one reversible validation task
validation_needed: verify outputs before preserving a delta
```
"""


def _first_packet(name: str, mission: str) -> str:
    return f"""# First Packet

## Objective

```text
objective: establish the first verified RepoKernel cycle for {name}
mission: {mission}
```

## Sources

```text
source_of_truth: README.md; CURRENT_STATE.md; sources/bootstrap/SOURCE_ATLAS_v1.0.md
```

## Boundary

```text
boundary: no publication, deletion, mission change or runtime write authority without confirmation
```

## First Move

```text
first_safe_action: audit the generated structure and complete one bounded task
validation: record the method and result under process/evidence/
```

## Memory Delta

```text
preserve: accepted corrections, source changes, boundary changes, verification and next action
do_not_preserve: raw chat, credentials and temporary speculation
```
"""


def _agent_gate(name: str, skill_id: str) -> str:
    return f"""# {name} Agent Gate

This project uses RepoKernel.

Before editing, read:

```text
CURRENT_STATE.md
sources/bootstrap/PROJECT_INSTRUCTIONS_v1.0.txt
sources/bootstrap/SOURCE_ATLAS_v1.0.md
skills/{skill_id}/SKILL.md
```

Work from explicit state and sources. Make the smallest reversible change, verify it, then preserve only a durable delta.

Ask before publishing, deploying, deleting, changing project mission, enabling executable extensions or granting runtime write authority.
"""


def _semantic_skill(name: str, skill_id: str) -> str:
    return f"""---
name: {skill_id}
description: Use when working in {name} to preserve state, source authority, boundaries, verification evidence and durable project deltas.
---

# {name} Semantic Kernel

## Entry

Read `CURRENT_STATE.md`, the source atlas and the active packet before acting.

## Cycle

```text
orient -> select sources -> propose -> act within boundary -> verify -> preserve delta
```

## Boundary

Do not infer external authority from local automation. Runtime, publication and cross-repository actions require their declared gates.
"""


def _evolution_policy() -> str:
    return """# Governed Evolution Policy

A project evolves through reviewed evidence, not direct self-modification.

```text
observation -> proposal -> isolated experiment -> evidence -> review -> promotion -> new baseline
```

Rules:

- baseline files are not rewritten by an unreviewed proposal;
- candidate changes preserve source lineage and rollback information;
- higher-risk actions require stronger approval;
- a failed experiment becomes evidence or residue, not hidden history;
- runtime availability never grants external-action authority.
"""


def _runtime_files(name: str, slug: str) -> dict[str, str]:
    runtime_manifest = {
        "schema": "repokernel.runtime.v1",
        "name": f"{slug}-runtime",
        "mode": "internal-candidate",
        "execution_authority": "proposal_only",
        "provider_policy": "adapter",
        "session_store": "runtime/sessions",
        "event_log": "runtime/events",
        "resources": {
            "skills": ["skills"],
            "extensions": ["runtime/extensions"],
            "prompts": ["runtime/prompts"],
        },
        "gates": {
            "project_trust": "required",
            "before_action": "runtime/policies/ACTION_GATE.md",
            "after_action": "runtime/policies/RESULT_GATE.md",
        },
        "evolution": {
            "policy": "docs/evolution-protocol.md",
            "write_target": "process/proposals",
            "promotion_requires_review": True,
        },
    }
    return {
        "runtime/runtime.manifest.json": json.dumps(runtime_manifest, indent=2) + "\n",
        "runtime/README.md": f"""# {name} Internal Runtime Candidate

This optional surface gives the repository a replaceable execution body. It does not grant autonomous authority.

The runtime is organized around:

```text
context transform -> model adapter -> action preflight -> tool execution -> result gate -> event log -> reviewed delta
```

Default authority is `proposal_only`. Executable extensions require project trust and source review.
""",
        "runtime/policies/ACTION_GATE.md": """# Action Gate

Classify every proposed action:

```text
read_only
project_write
network
secret_access
publish
cross_repository
destructive
```

`read_only` may run when the runtime is trusted. All other classes require the approval declared by the project policy. Unknown actions are blocked.
""",
        "runtime/policies/RESULT_GATE.md": """# Result Gate

After an action, record:

```text
action_id
source
result
side_effects
verification
error
candidate_delta
```

Only verified results may support lifecycle promotion.
""",
        "runtime/sessions/README.md": """# Sessions

Sessions use append-only JSONL records with stable `id` and optional `parent_id`. Branching creates a new lineage without deleting prior evidence.

Compaction may create summaries for model context, but the source event history remains separate from promoted project memory.
""",
        "runtime/events/README.md": """# Runtime Events

Reference lifecycle:

```text
runtime_start
cycle_start
context_ready
model_request
model_response
action_preflight
action_start
action_end
cycle_end
runtime_end
```

Each event carries a stable run, cycle and lineage identifier.
""",
        "runtime/extensions/README.md": """# Extensions

Extensions may add tools, adapters, event handlers or interfaces. They are executable code.

Project-local extensions remain disabled until the project is trusted and the extension source has been reviewed.
""",
        "runtime/prompts/README.md": """# Runtime Prompts

Prompts are resources, not authority. They may shape a task but cannot override action gates, source boundaries or lifecycle evidence requirements.
""",
        "process/proposals/README.md": """# Evolution Proposals

Runtime-generated improvements are written here as proposals. A proposal must include source, hypothesis, expected effect, risk, validation plan and rollback path.

Promotion into the baseline requires review.
""",
        "docs/evolution-protocol.md": _evolution_policy(),
    }


def project_plan(name: str, mission: str, *, level: str = "L1") -> dict[str, str]:
    if level not in LEVELS:
        raise ValueError(f"unsupported level: {level}")
    clean_name = name.strip()
    clean_mission = mission.strip()
    if not clean_name or not clean_mission:
        raise ValueError("name and mission are required")
    slug = slugify(clean_name)
    semantic_id = f"{slug}-semantic-kernel"

    plan: dict[str, str] = {
        "AGENTS.md": _agent_gate(clean_name, semantic_id),
        "CURRENT_STATE.md": _state(clean_name, "draft", "complete the first evidence-backed project cycle"),
        "process/FIRST_PACKET.md": _first_packet(clean_name, clean_mission),
    }
    if level in {"L1", "L2", "L3"}:
        plan.update({
            "README.md": f"# {clean_name}\n\n{clean_mission}\n",
            "sources/bootstrap/PROJECT_INSTRUCTIONS_v1.0.txt": (
                f"Project: {clean_name}\nMission: {clean_mission}\n"
                "Work from current state, explicit sources, boundaries and verification.\n"
            ),
            "sources/bootstrap/SOURCE_ATLAS_v1.0.md": f"""# Source Atlas

| Path | Type | Role |
| --- | --- | --- |
| `README.md` | mission | Project definition |
| `CURRENT_STATE.md` | state | Active state and next action |
| `skills/{semantic_id}/SKILL.md` | skill | Project continuity rules |
| `process/FIRST_PACKET.md` | packet | First bounded task |
""",
            f"skills/{semantic_id}/SKILL.md": _semantic_skill(clean_name, semantic_id),
        })
    if level in {"L2", "L3"}:
        manifest = {
            "schema": "repokernel.manifest.v1",
            "name": clean_name,
            "id": slug,
            "version": "0.1.0",
            "readiness_target": level,
            "runtime": "runtime/runtime.manifest.json" if level == "L3" else None,
            "state": "CURRENT_STATE.md",
            "entry_gate": "AGENTS.md",
            "source_atlas": "sources/bootstrap/SOURCE_ATLAS_v1.0.md",
            "registry": "registry/skills.json",
        }
        registry = {
            "schema": "repokernel.skill-registry.v1",
            "version": date.today().isoformat(),
            "skills": [{
                "id": semantic_id,
                "version": "0.1.0",
                "state": "draft",
                "path": f"skills/{semantic_id}/SKILL.md",
                "risk": "safe",
                "evidence": [],
                "supersedes": [],
            }],
        }
        plan.update({
            "repokernel.json": json.dumps(manifest, indent=2) + "\n",
            "registry/skills.json": json.dumps(registry, indent=2) + "\n",
            "process/deltas/README.md": "# Deltas\n\nPreserve durable state changes, not raw chat history.\n",
            "process/evidence/README.md": "# Evidence\n\nStore validation records that justify readiness and lifecycle claims.\n",
            "docs/EVOLUTION_POLICY.md": _evolution_policy(),
        })
    if level == "L3":
        plan.update(_runtime_files(clean_name, slug))
    return plan


def skill_repo_plan(name: str, mission: str) -> dict[str, str]:
    clean_name = name.strip()
    clean_mission = mission.strip()
    if not clean_name or not clean_mission:
        raise ValueError("name and mission are required")
    slug = slugify(clean_name)
    return {
        "README.md": f"# {clean_name}\n\n{clean_mission}\n",
        "AGENTS.md": f"""# {clean_name} Skill Repository Gate

Read `CURRENT_STATE.md`, the source atlas and `skills/{slug}/SKILL.md` before editing.

The skill remains `draft` until a substantive example and passing validation record exist.
""",
        "CURRENT_STATE.md": _state(clean_name, "draft", "create a substantive example and validation record"),
        "sources/bootstrap/PROJECT_INSTRUCTIONS_v1.0.txt": (
            f"Skill: {clean_name}\nMission: {clean_mission}\n"
            "Preserve source authority, examples, validation and promotion boundaries.\n"
        ),
        "sources/bootstrap/SOURCE_ATLAS_v1.0.md": f"""# Source Atlas

| Path | Type | Role |
| --- | --- | --- |
| `README.md` | mission | Public skill definition |
| `CURRENT_STATE.md` | state | Declared lifecycle state |
| `skills/{slug}/SKILL.md` | skill | Capability contract |
| `process/FIRST_PACKET.md` | packet | First validation task |
""",
        f"skills/{slug}/SKILL.md": f"""---
name: {slug}
description: {clean_mission}
---

# {clean_name}

## Purpose

{clean_mission}

## Inputs

Define the minimum input required by the capability.

## Outputs

Define observable outputs and validation criteria.

## Boundary

The skill does not grant publication, deployment or cross-repository authority.
""",
        "process/FIRST_PACKET.md": _first_packet(clean_name, clean_mission),
        "examples/README.md": "# Examples\n\nAdd a substantive input and expected output. This placeholder is not lifecycle evidence.\n",
        "validation/README.md": "# Validation\n\nStore `result.json` with `passed: true` only after executing a real or synthetic case.\n",
    }
