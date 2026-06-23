# Post-Phase-0 — Autopoietic Architecture Convergence Gate

Date: 2026-06-23  
Status: single convergence gate before Phase 1; no Phase 0 scope change

## Purpose

Consolidate the existing post-Phase-0 schema horizon, recursive distillation, autopoietic-cycle analysis and departmental-autonomy analysis into one decision surface before Phase 1 schemas and package boundaries are frozen.

This packet supersedes the use of the following files as separate execution gates; they remain authoritative inputs:

```text
POST_PHASE0_SCHEMA_HORIZON_2026-06-23.md
POST_PHASE0_RECURSIVE_IMPROVEMENT_DISTILLER.md
docs/possibility-horizon.md
docs/recursive-distillation-plane.md
docs/autopoietic-cycle-gap-analysis.md
docs/departmental-autonomy-spectral-analysis.md
skills/recursive-improvement-distiller/SKILL.md
skills/autopoietic-cycle-controller/SKILL.md
```

## Prerequisites

Do not execute this gate until:

1. Codex Phase 0 is complete and explicitly accepted.
2. Every tracked file is present in the migration classification.
3. Registry and evidence paths resolve.
4. Superseded packets and incomplete surfaces are classified.
5. The repository worktree is clean after the Phase 0 commit.

This gate does not authorize Phase 1 implementation.

## Architectural Decision To Preserve

```text
repokernel-core       ships first: compiler, schemas, Reference Seeds, retrofit and L0-L2
repokernel-cognition  optional: cognitive profiles and recursive ResultantPacket production
repokernel-cycle      optional: event, tension, fitness and memory metabolism
repokernel-runtime    deferred execution body and host independence
```

```text
L0-L3 = readiness
A0-A4 = autonomy
none/read/propose/project_write/external_action = authority
D0-D3 = cognitive depth
```

No axis implies another.

Departmental topology is constrained to:

```text
Plane 1 — constitutional/source plane
Plane 2 — bounded departmental holons
inside Plane 2 — ephemeral task microcycles
between planes — synaptic membrane, not a third governance plane
```

No persistent nested departments are created by default.

## Read Order

```text
CURRENT_STATE.md
process/FIRST_PACKET.md
process/reports/current-tree.json
process/reports/migration-classification.json
packets/FOR_CODEX/REPOKERNEL_FINAL_IMPLEMENTATION_PACKAGE_2026-06-23.md
packets/FOR_CODEX/POST_PHASE0_SCHEMA_HORIZON_2026-06-23.md
docs/possibility-horizon.md
docs/recursive-distillation-plane.md
skills/recursive-improvement-distiller/SKILL.md
docs/autopoietic-cycle-gap-analysis.md
skills/autopoietic-cycle-controller/SKILL.md
docs/departmental-autonomy-spectral-analysis.md
docs/internal-runtime-architecture.md
registry/skills.json
```

## Required Operation

Use `recursive-improvement-distiller` to produce one converged Phase 1 Resultant.

Start at D1. Use D2 only when alternative schema/package boundaries are materially different. Use D3 only to resolve systemic overlap, extract guards and reduce future rework.

Maximum five materially distinct branches.

## Required Questions

### Core Boundary

1. What is the smallest `repokernel-core` that can generate and retrofit L0-L2 safely?
2. Which cognition/cycle/runtime fields must be represented now only as optional references or extensions?
3. Which components must be excluded from Phase 1 implementation?

### Canonical Objects

Decide the minimum v1 contracts for:

```text
SourceManifest
ProjectModel
SeedSpec
GenerationPlan
ActivationReport
SkillRegistry
```

Evaluate whether the following need full v1 schemas, provisional schemas, references or namespaced extensions:

```text
IntentContract
ContextSnapshot
TensionReport
ResultantPacket
AutonomyPolicy
CycleRecord
FitnessContract
ResultantEvaluation
LearningDelta
EvolutionProposal
RuntimeManifest
DepartmentContract
SynapticEvent
```

### Separation Of Duties

Define which invariants belong in core validation immediately:

```text
no self-approval
no authority escalation
fitness fixed before evaluated action
candidate capability disabled by default
source data does not become instruction authority
accepted baseline changes only through reviewed plan
```

### Extension Horizon

Decide the minimal optional fields for:

```text
lineage
lifecycle
authority_mode
autonomy_level
cognitive_profile_ref
method_profile_ref
observer_ref
evaluation_refs
department_ref
extensions
```

Unknown extensions must round-trip without changing planning, writes or authority.

### Departmental Topology

Decide whether Phase 1 should preserve, but not implement, a departmental contract.

The required architectural constraints are:

```text
two persistent governance planes only
one level of persistent departments by default
task microcycles are ephemeral
shared principles are referenced and locally applied, not copied as new canon
no direct cross-department state mutation
one authoritative local state and active packet per department
bounded event fan-out, TTL and deduplication
local autonomy defaults to A1/propose
promotion remains independent
```

Classify `DepartmentContract` and `SynapticEvent` as one of:

```text
core_optional
provisional
namespaced_extension
deferred
```

Do not make departmental machinery a dependency of Direct Start, synthesis or retrofit.

### First Proof

Design the smallest A1 observe-and-propose proof without implementing an autonomous runtime:

```text
fixture event
-> ContextSnapshot fixture
-> TensionReport
-> ResultantPacket
-> independent evaluation fixture
-> no write
```

This proof may be a schema and fixture suite after the core contracts are stable; it must not block Direct Start and retrofit unless a missing invariant would make them unsafe.

Design one optional synthetic departmental perturbation fixture:

```text
one global invariant
one department charter
one local task microcycle
one significant cascade event
one irrelevant local change that must not propagate
```

The fixture tests topology and entropy controls only. It does not implement an autonomous department.

## Required Deliverables

### A. Converged Resultant

Create:

```text
packets/FOR_CODEX/FORGE_R_PHASE1_CONVERGED_RESULTANT.md
```

Required sections:

```text
objective
source anchors
current tension
accepted invariants
verified facts
assumptions and unknowns
branches considered
pruned and united branches
opening detected
selected resultant
why it minimizes total rework
Phase 1 exact scope
explicit deferrals
files to create or modify
acceptance tests
falsification path
rollback point
neighborhood implications
stop reason
```

### B. Schema Classification Matrix

Create:

```text
process/reports/phase1-schema-classification.json
```

For every candidate contract record:

```text
name
classification: core_required | core_optional | provisional | namespaced_extension | deferred
reason
producer
consumer
authority_effect: none
first_test
future_migration
```

Any item with an authority effect other than `none` fails this gate.

### C. Package Boundary Report

Create:

```text
process/reports/package-boundaries-v1.md
```

It must show imports/dependencies allowed among core, cognition, cycle and runtime and demonstrate that core does not depend on optional layers.

It must also show that future departmental contracts depend on core contracts but core does not depend on departments.

### D. A1 Proof Plan

Create:

```text
packets/FOR_CODEX/A1_OBSERVE_AND_PROPOSE_PROOF_PLAN.md
```

It must include fixtures, expected artifacts, no-write assertions, independent evaluation, event deduplication and authority-escalation tests.

### E. Departmental Topology Decision

Create:

```text
process/reports/departmental-topology-decision.md
```

It must state:

```text
persistent planes
microcycle policy
department creation criteria
subdepartment prohibition or exception rule
inheritance and local-application model
synaptic event contract candidate
entropy budget
pilot fixture
explicit deferrals
```

### F. Updated Phase 1 Packet

Propose an amendment to the Phase 1 section of the final Codex architecture packet. Do not modify the authoritative packet until operator review.

## Critical Gap Acceptance Matrix

The convergence gate must explicitly close or defer each gap:

```text
G1 intent contract
G2 context snapshot
G3 tension function
G4 cycle state machine
G5 separation of duties
G6 fitness contract
G7 action transaction
G8 autonomy axis
G9 memory metabolism
G10 capability forge
G11 trigger and cascade semantics
G12 security and trust
G13 empirical latency proof
G14 gate fragmentation
G15 departmental topology and entropy control
```

A deferral is valid only if the v1 core cannot accidentally make the deferred capability authoritative.

## Acceptance Criteria

This gate passes when:

- there is one Phase 1 Resultant, not multiple active implementation routes;
- core remains independently usable without cognition, cycle, departmental or runtime packages;
- no self-approval and no authority escalation are testable invariants;
- schemas preserve future lineage and namespaced extensions without implementing future features;
- Direct Start and retrofit remain the primary release path;
- A1 is specified as proposal-only and no-write;
- departmental autonomy remains optional, bounded and non-recursive by default;
- local guides are defined as applications of shared principles rather than duplicated canonical truth;
- every additional contract is classified and justified;
- all future runtime, scheduling, network, department daemon and capability-forge implementation is explicitly deferred;
- the Resultant reduces or clarifies Phase 1 rather than expanding it;
- operator acceptance is recorded before Phase 1 begins.

## Boundary

Do not implement:

```text
event daemon
scheduler
network transport
multi-agent polling
project writes from autonomous cycles
internal model loop
skill factory execution
automatic promotion
cross-repository action
persistent nested departments
department-to-department direct writes
departmental runtime workers
```

The purpose of this gate is to ensure that the first stable core is safe, minimal, department-compatible and evolution-compatible before code architecture is frozen.
