# RepoKernel Current State

updated: 2026-06-24
status: Phase 1 prototype accepted for P0 hardening only; external use blocked until hardening passes
repository: GrazianoGuiducci/RepoKernel
visibility: public
license: MIT
branch: main

## Active Surface

```text
active_surface: Phase 1 P0 hardening after independent review
current_next: use the operational procedure to prepare external-style A1 review packets before any real external repository test
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

## Repo Observer Setup Ownership Correction

```text
status: classification_only
packet: packets/FOR_CODEX/REPO_OBSERVER_SETUP_OWNERSHIP_CORRECTION_2026-06-24.md
decision: dnd-repo-observer-setup is canonically a RepoKernel A1
  observe_and_propose / retrofit adapter, not a Business Manager core function.
business_boundary: Business Manager may use an adapter copy for relationship,
  call, offer and follow-up routing.
seed_boundary: no d-nd-seed mutation or portable Seed promotion before stable
  RepoKernel L0-L2 evidence, Reference Seed reproducibility and reviewed
  retrofit behavior.
```

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
packets/FOR_CODEX/PHASE1_P0_HARDENING_PACKET_2026-06-24.md
packets/FOR_GPT_PRO/REPOKERNEL_PHASE1_GPT_PRO_INDEPENDENT_REVIEW_2026-06-24.md
registry/skills.json
scripts/repokernel_core.py
```

## Boundary

```text
can_change: RepoKernel governance, Phase 1 docs, schemas, validators, planner, guide model, tests and local validation reports
needs_confirmation: external repository pilot, d-nd-seed promotion, license changes, downstream promotion, remote actions and executable L3 work
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
  - GPT Pro independent review preserved inside RepoKernel
  - Phase 1 is accepted only as a prototype surface for P0 hardening
  - governance, docs, validators, canonical serialization, path safety, planner determinism, guide disclosure and audit claims hardened
  - minimal read-only CLI added: validate-spec, inspect, plan, guides and audit
  - A1 observe-and-propose gate created for local no-write proofs before external repository tests
  - local synthetic A1 observe-and-propose proof passed with no target writes
  - operational procedure documented for new, existing and external repositories
not_yet_verified:
  - recursive current-tree migration classification
  - registry and evidence consistency after cleanup
  - Reference Seed reproducibility
  - external-style A1 observe-and-propose proof
  - synthesis and retrofit implementation
  - recursive distillation trigger fidelity and measured latency effect
  - A1 observe-and-propose cycle
  - independent evaluation and crash recovery
```

## First Safe Action

```text
first_safe_action: define the external-style repository review protocol before using a real third-party repository
validation_needed: unit tests, CLI smoke tests, inventory/link check, audit, git diff --check and explicit external-style proof blockers
```

Operational procedure:

```text
docs/guides/operational-procedure.md
```

Latest Phase 0 validation summary:

```text
process/reports/phase0-validation-summary.md
```

Latest convergence outputs:

```text
packets/FOR_CODEX/FORGE_R_PHASE1_CONVERGED_RESULTANT.md
process/reports/phase1-schema-classification.json
process/reports/package-boundaries-v1.md
process/reports/departmental-topology-decision.md
process/reports/guide-system-decision.md
packets/FOR_CODEX/A1_OBSERVE_AND_PROPOSE_PROOF_PLAN.md
packets/FOR_CODEX/PHASE1_PACKET_AMENDMENT_PROPOSAL.md
```

Latest Phase 1 implementation surfaces:

```text
src/repokernel/
schemas/
docs/guides/
tests/unit/
```

External review request prepared:

```text
packets/FOR_GPT_PRO/REPOKERNEL_PHASE1_EXTERNAL_REVIEW_REQUEST_2026-06-24.md
```

External review received:

```text
packets/FOR_GPT_PRO/REPOKERNEL_PHASE1_GPT_PRO_INDEPENDENT_REVIEW_2026-06-24.md
```

Active hardening packet:

```text
packets/FOR_CODEX/PHASE1_P0_HARDENING_PACKET_2026-06-24.md
```

Next A1 proof gate:

```text
packets/FOR_CODEX/PHASE1_A1_OBSERVE_AND_PROPOSE_GATE_2026-06-24.md
```

Latest A1 proof report:

```text
process/reports/a1-local-no-write-proof-2026-06-24.md
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
