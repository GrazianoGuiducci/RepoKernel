# RepoKernel Current State

updated: 2026-06-23
status: final architecture accepted; Codex Phase 0 authorized
repository: GrazianoGuiducci/RepoKernel
visibility: public
license: MIT
branch: main

## Active Surface

```text
active_surface: migrate current main toward one compiler, reproducible Reference Seeds and conflict-safe retrofit
current_next: Codex executes Phase 0 inventory and cleanup only
```

## Final Architecture

```text
RepoKernel Source / Compiler
  -> compiles a reviewed SeedSpec
  -> materializes a project-specific Project Kernel
```

```text
Reference Seed = precompiled reproducible SeedSpec
Synthesized ProjectSeed = custom SeedSpec compiled from authorized sources
Retrofit Overlay = target-aware application of a SeedSpec
Project Kernel = validated local control plane under .repokernel/
Root and host-native files = adapters or registered existing authorities
L0-L2 = first stable implementation scope
L3 = schema and architecture contract only
```

## Source Of Truth

```text
packets/FOR_CODEX/REPOKERNEL_FINAL_IMPLEMENTATION_PACKAGE_2026-06-23.md
packets/FOR_CODEX/GPT_PRO_REPOKERNEL_FINAL_ARCHITECTURE_AND_CODEX_PACKET_2026-06-23.md
packets/FOR_CODEX/GPT_PRO_REPOKERNEL_FINAL_ARCHITECTURE_APPENDIX_2026-06-23.md
docs/distribution-model.md
docs/seed-synthesis-pipeline.md
docs/retrofit-model.md
docs/readiness-levels.md
docs/runtime-adapters.md
docs/internal-runtime-architecture.md
registry/skills.json
scripts/repokernel_core.py
```

## Boundary

```text
can_change: Phase 0 inventory, classification, documentation cleanup, registry/evidence correction and packet archival
needs_confirmation: Phase 1 schemas/package work, license changes, downstream promotion, remote actions and executable L3 work
must_not_touch: credentials, unauthorized sources, private logs, unrelated repositories and accepted project canon without reviewed plan
```

## Verified State

```text
verified:
  - final ontology and distribution model decided
  - .repokernel/ selected as canonical host-neutral installed control plane
  - direct starter resolved as a precompiled SeedSpec
  - synthesis and retrofit resolved under one compiler
  - L3 deferred to contract status
  - phased Codex packet and test matrix committed
not_yet_verified:
  - recursive current-tree migration classification
  - registry and evidence consistency after cleanup
  - Reference Seed reproducibility
  - schemas and deterministic planner
  - synthesis and retrofit implementation
```

## First Safe Action

```text
first_safe_action: give Codex the final implementation package and authorize Phase 0 only
validation_needed: complete tracked-file coverage, resolved registry paths, link checks, clean diff and explicit Phase 1 blockers
```

## Residue Not To Follow

```text
static starter templates as a separate architecture
cloning RepoKernel Source into target projects
root files as competing canonical state
untrusted documents or model output treated as authority
hand-edited dist distributions
implementation of executable L3 before permission and sandbox proof
promotion to d-nd-seed before stable L0-L2 evidence
```
