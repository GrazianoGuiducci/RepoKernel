---
name: create-skill-repo
description: Use when creating a repository-shaped skill with an AGENTS gate, current state, source bootstrap, SKILL.md, first packet, memory delta and promotion boundary.
---

# Create Skill Repo

## Mandate

Create a new repository-skill that is readable by AI systems and can be evaluated, improved or promoted later.

## Required Fields

```text
skill_name:
mission:
users:
inputs:
outputs:
source_authority:
boundary:
validation:
promotion_path:
```

## Default Structure

```text
README.md
AGENTS.md
CURRENT_STATE.md
skills/<skill-name>/SKILL.md
sources/bootstrap/PROJECT_INSTRUCTIONS_v1.0.txt
process/FIRST_PACKET.md
examples/
tests/
```

## First Safe Action

Create a minimal local structure and validate it with `scripts/audit_skill_repo.py`. Do not publish or promote until reviewed.

