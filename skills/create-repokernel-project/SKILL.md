---
name: create-repokernel-project
description: Use when creating a new repository or retrofitting an existing repository with RepoKernel structure: AGENTS gate, CURRENT_STATE, source bootstrap, semantic kernel, process packet, templates and audit checks.
---

# Create RepoKernel Project

## Purpose

Create or retrofit a repository so future AI sessions can reenter without starting from zero.

## Minimum Structure

```text
AGENTS.md
CURRENT_STATE.md
sources/bootstrap/PROJECT_INSTRUCTIONS_v1.0.txt
sources/bootstrap/SOURCE_ATLAS_v1.0.md
skills/<project>-semantic-kernel/SKILL.md
process/FIRST_PACKET.md
```

## Workflow

1. Identify project name, path, mission, owner, visibility and publication boundary.
2. Audit existing files before writing.
3. Add only missing layers.
4. Use trust-oriented instructions.
5. Add a memory-delta rule.
6. Validate with `scripts/audit_repokernel_project.py`.

## Boundary

Ask before creating a public remote, pushing, deleting, exposing private material or changing project canon.

