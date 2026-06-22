# RepoKernel Readiness Levels

RepoKernel readiness is based on evidence. File presence is necessary but not sufficient.

## L0 — Reentry Core

A future AI session can orient itself before acting.

Required:

```text
AGENTS.md
CURRENT_STATE.md
process/FIRST_PACKET.md
```

The files must identify the project, active state, boundaries, sources and first safe action.

## L1 — Semantic Kernel

The project can route sources and preserve continuity across sessions and tools.

Adds:

```text
README.md
sources/bootstrap/PROJECT_INSTRUCTIONS_v1.0.txt
sources/bootstrap/SOURCE_ATLAS_v1.0.md
skills/<project>-semantic-kernel/SKILL.md
```

The source atlas must resolve, the skill must have valid frontmatter, and state, packet and semantic kernel must agree.

## L2 — Governed Evolution

The project can turn repeated verified learning into reviewable rules, skills, templates or promotion candidates.

Adds:

```text
repokernel.json
registry/skills.json
schemas/
process/deltas/
process/evidence/
tests/
promotion gates
runtime-adapter declarations
```

Lifecycle transitions require evidence. Promotion must state risks, exclusions, validation and rollback or deprecation path.

## Non-Equivalence Rule

```text
files present != semantics valid
semantics valid != evolution governed
automation available != external-action permission
```

Audits report `structure_ready`, `semantic_ready`, `evolution_ready`, failed checks and the next bounded action. A single readiness boolean is insufficient.
