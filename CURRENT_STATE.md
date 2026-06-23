# RepoKernel Current State

updated: 2026-06-23
status: final architecture accepted; critical gap review integrated; Codex Phase 0 authorized
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

Optional architecture layers are now explicit:

```text
repokernel-core       compiler, schemas, Reference Seeds, retrofit and L0-L2
repokernel-cognition  cognitive profiles and recursive ResultantPacket production
repokernel-cycle      event, tension, fitness and memory metabolism
repokernel-runtime    deferred execution body and host independence
```

Recursive improvement remains an optional cognitive plane:

```text
Project Kernel + objective or tension + evidence
  -> recursive improvement distillation
  -> ResultantPacket
  -> reviewed implementation
```

The autopoietic cycle remains a governed optional plane:

```text
approved event
  -> ContextSnapshot
  -> Intent alignment
  -> TensionReport
  -> ResultantPacket
  -> independent evaluation
  -> durable LearningDelta
```

The first proof target is A1 `observe_and_propose`, with no project writes.

## Independent Coordinates

```text
readiness: L0-L3
autonomy: A0-A4
authority: none | read | propose | project_write | external_action
cognitive_depth: D0-D3
```

No coordinate implies another.

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
docs/recursive-distillation-plane.md
docs/autopoietic-cycle-gap-analysis.md
skills/recursive-improvement-distiller/SKILL.md
skills/autopoietic-cycle-controller/SKILL.md
packets/FOR_CODEX/POST_PHASE0_AUTOPOIETIC_CONVERGENCE_GATE.md
registry/skills.json
scripts/repokernel_core.py
```

## Boundary

```text
can_change: Phase 0 inventory, classification, documentation cleanup, registry/evidence correction and packet archival
needs_confirmation: post-Phase-0 convergence acceptance, Phase 1 schemas/package work, license changes, downstream promotion, remote actions and executable L3 work
must_not_touch: credentials, unauthorized sources, private logs, unrelated repositories and accepted project canon without reviewed plan
```

## Critical Gap Decision

The most important missing safeguard is constitutional separation of duties:

```text
Intent Custodian
Observer
Distiller
Executor
Evaluator
Promoter
```

The same unreviewed process may not define intent, produce a candidate, execute it, evaluate it and promote it.

Further critical gaps are classified in `docs/autopoietic-cycle-gap-analysis.md`:

```text
IntentContract
ContextSnapshot
TensionReport
CycleState
FitnessContract
safe action transaction
autonomy axis
memory metabolism
capability candidate forge
trigger and cascade semantics
security and trust
empirical latency proof
post-Phase-0 gate consolidation
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
  - recursive-improvement-distiller registered as a draft skill
  - autopoietic-cycle-controller registered as a draft skill
  - critical gap analysis and one post-Phase-0 convergence gate committed
  - Phase 0 scope remains unchanged
not_yet_verified:
  - recursive current-tree migration classification
  - registry and evidence consistency after cleanup
  - Reference Seed reproducibility
  - schemas and deterministic planner
  - synthesis and retrofit implementation
  - recursive distillation trigger fidelity and measured latency effect
  - A1 observe-and-propose cycle
  - independent evaluation and crash recovery
```

## First Safe Action

```text
first_safe_action: give Codex the final implementation package and authorize Phase 0 only
validation_needed: complete tracked-file coverage, resolved registry paths, link checks, clean diff and explicit Phase 1 blockers
```

After explicit Phase 0 acceptance:

```text
open packets/FOR_CODEX/POST_PHASE0_AUTOPOIETIC_CONVERGENCE_GATE.md
produce one FORGE_R_PHASE1_CONVERGED_RESULTANT.md
require operator acceptance before Phase 1
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
recursive depth applied to every task
unbounded self-analysis without new evidence or a stop rule
one process self-approving intent, action, evaluation and promotion
adding autonomous writes before A1 observe-and-propose is proven
using one self-optimized scalar as the fitness definition
```
