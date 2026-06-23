# RepoKernel Readiness Levels

Readiness is demonstrated by evidence. File presence is necessary but not sufficient.

## L0 — Reentry Core

A future AI session can orient before acting.

```text
AGENTS.md
CURRENT_STATE.md
process/FIRST_PACKET.md
```

The project exposes identity, active state, boundaries, sources and first safe action.

## L1 — Semantic Kernel

The project can route sources and preserve continuity across sessions and tools.

```text
README.md
sources/bootstrap/PROJECT_INSTRUCTIONS_v1.0.txt
sources/bootstrap/SOURCE_ATLAS_v1.0.md
skills/<project>-semantic-kernel/SKILL.md
```

The source atlas resolves, the skill has valid frontmatter, and state, packet and semantic kernel agree.

## L2 — Governed Improvement

The project can turn repeated verified learning into reviewable rules, skills, templates or promotion candidates.

```text
repokernel.json
registry/skills.json
process/evidence/
process/deltas/
review and promotion policy
```

Lifecycle transitions require evidence. Promotion records exclusions, validation, limitations and a reversal or deprecation path.

## L3 — Operational Runtime

The project has an optional replaceable execution body.

```text
runtime manifest
action and result gates
session lineage
event lifecycle
extension trust policy
model and tool adapters
```

L3 requires explicit project trust, bounded authority, pre-action and post-action checks, append-only session lineage and review-gated promotion. The generated default is `proposal_only`.

## Non-Equivalence Rule

```text
files present != semantics valid
semantics valid != improvement governed
improvement governed != operational runtime
runtime available != external-action permission
```

Audits report `structure_ready`, `semantic_ready`, `evolution_ready`, `runtime_ready`, failed checks and the next bounded action.
