# RepoKernel Current State

updated: 2026-06-22
status: public starter published; v0.2 validation hardening active
repository: GrazianoGuiducci/RepoKernel
visibility: public
license: MIT
branch: main

## Active Surface

```text
active_surface: semantic validation, lifecycle governance and host-neutral evolution
current_next: replace structural readiness with verifiable L0/L1/L2 readiness and align scaffolds, audits, registry and evidence
```

## Source Of Truth

```text
primary_sources:
  - README.md
  - AGENTS.md
  - repokernel.json
  - docs/readiness-levels.md
  - docs/skill-repo-lifecycle.md
  - registry/skills.json
supporting_sources:
  - docs/
  - templates/
  - skills/
  - scripts/
  - tests/
  - examples/
  - process/
  - sources/bootstrap/
```

## Accepted Direction

```text
RepoKernel = host-neutral repo / pattern / method for project continuity.
GitHub = first public adapter, not the identity of RepoKernel.
Meta-skills = internal capabilities that create, evaluate, route, promote or update repository-aware skills.
Readiness = evidence-backed state, not file presence alone.
```

RepoKernel is not only a template collection. It is the governed context layer through which a project exposes identity, state, sources, authority, boundaries, deltas and next actions to future AI systems.

## Boundary

```text
can_change:
  - public-safe docs, schemas, registry, templates, scripts, tests and synthetic examples
needs_confirmation:
  - license changes
  - claims of adoption, autonomy or scientific proof
  - downstream promotion into Seed, THIA or another repository
  - publication of private case material
must_not_touch:
  - credentials, private logs, private workspace paths and raw private transcripts
  - downstream repositories from this state alone
```

## Verified State

```text
last_verified: local v0.2 test bundle on 2026-06-22
verification_commands:
  - python -m unittest discover -s tests -v
  - python scripts/audit_repokernel_project.py --path . --profile repokernel-source --json
known_result:
  - six local unit tests passed before repository integration
  - GitHub-hosted validation must be re-run after all v0.2 files are committed
```

## First Safe Action

```text
first_safe_action: complete v0.2 hardening, then run semantic audit and unit tests against the committed repository
validation_needed: confirm scaffold-to-audit parity, registry coverage, lifecycle evidence and runtime-adapter claims
```

## Residue Not To Follow

```text
residue:
  - d-nd-skill-lab as primary repo name: superseded by RepoKernel
  - raw private examples as first public examples: use synthetic examples first
  - autonomous self-modification claims: preserve explicit review and promotion gates
  - repokernel_ready as a single boolean based only on file existence
  - GitHub-specific mechanics presented as universal RepoKernel behavior
```
