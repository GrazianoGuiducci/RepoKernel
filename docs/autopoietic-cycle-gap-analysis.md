# Autopoietic Cycle — Critical Gap Analysis And Reconfiguration

Date: 2026-06-23  
Status: architecture decision candidate; no implementation authority by itself

## Executive Resultant

RepoKernel currently contains the main components of a generative project system:

```text
sources -> ProjectModel -> SeedSpec -> plan -> Project Kernel
state -> evidence -> proposal -> reviewed delta
objective or tension -> recursive distillation -> ResultantPacket
```

It does not yet contain a closed autonomous autopoietic cycle.

The missing capability is not unrestricted self-modification. It is a governed metabolism that can:

```text
receive an event
-> observe the current field
-> align with accepted intent
-> detect a material tension
-> produce a bounded Resultant
-> act only within granted authority
-> observe the effect
-> evaluate it against an independent contract
-> preserve a durable delta
-> propose a new capability when a real gap is demonstrated
```

The architecture should therefore be reconfigured around four separable layers:

```text
repokernel-core       project truth, compiler, plans, evidence and L0-L2
repokernel-cognition  observer profiles and recursive distillation
repokernel-cycle      event, tension, evaluation and memory metabolism
repokernel-runtime    optional execution body and host independence
```

These layers may coexist in one repository initially, but their contracts and authorities must remain distinct.

## What Already Exists

RepoKernel already defines:

- a canonical Project Kernel under `.repokernel/`;
- accepted source, model, specification and planning boundaries;
- L0-L3 readiness;
- proposal-only as the safe runtime default;
- an append-only event/session direction;
- recursive improvement distillation with bounded depth and stop rules;
- separation between cognitive extensions and operational authority;
- reviewed promotion rather than direct self-rewrite.

The recovery procedure also preserves the central discipline:

```text
field = state + sources + decisions + boundaries + active packet
```

and requires the next instance to act only inside the current gate.

## Critical Gaps

### G1 — Intent Is Not Yet A Governed Runtime Contract

`SeedSpec` expresses project intent, but an autonomous cycle needs a stable runtime-facing contract that distinguishes:

```text
seed invariant
mission
active objective
priority
non-goals
hard constraints
success conditions
review or expiry condition
who may reinterpret
who may modify
```

Without this distinction, the cycle may optimize a local objective while drifting from the project source.

**Decision:** add a versioned `IntentContract` referenced by SeedSpec. The cycle may interpret it and propose amendments; it cannot accept its own amendment.

### G2 — No Perception Closure

There is no canonical `ContextSnapshot` that tells the cycle what changed since the prior accepted state.

It must capture:

```text
source and state hashes
new or changed events
failed validations
expired evidence
open conflicts
pending proposals
capability availability
uncertainty and freshness
```

**Decision:** every cycle starts from an immutable, target-bound ContextSnapshot.

### G3 — No Motivation Or Tension Function

The system has no rule for deciding why it should wake or whether a change merits a cycle.

**Decision:** introduce a `TensionReport` comparing IntentContract and ContextSnapshot. It may identify drift, failure, freshness expiry, opportunity, capability gap or operator request. Below threshold, the correct action is `sleep`.

### G4 — No Cycle State Machine

Runtime events are listed, but the legal transitions, persistence, retries and recovery behavior are not defined.

**Decision:** define an explicit state machine:

```text
sleep
-> wake
-> observe
-> align
-> detect_tension
-> distill
-> plan
-> authority_preflight
-> checkpoint
-> act_or_propose
-> observe_effect
-> evaluate
-> metabolize
-> forge_candidate_optional
-> cascade
-> sleep
```

Every transition records `cycle_id`, parent lineage, input hash, output hash and stop reason.

### G5 — No Constitutional Separation Of Duties

This is the most important gap.

One component must not be allowed to:

```text
set the goal
produce the candidate
execute the candidate
evaluate the candidate
promote the candidate
```

inside one unreviewed authority context.

**Decision:** enforce five logical roles, even if one host executes several roles sequentially:

```text
Intent Custodian   owns accepted intent and invariants
Observer           produces ContextSnapshot and TensionReport
Distiller          produces ResultantPacket and candidate plan
Executor           performs only an approved, target-bound action
Evaluator          compares prediction and effect using a pre-existing FitnessContract
Promoter           accepts, rejects, rolls back or requests operator review
```

Hard invariants:

- the Distiller cannot approve its own plan;
- the Executor cannot be the sole evaluator of success;
- the Evaluator cannot change the FitnessContract in the evaluated cycle;
- the candidate capability cannot promote or load itself;
- no role can increase `authority_mode`.

### G6 — No Fitness Closure

Passing file-shape tests is not sufficient to show evolution.

**Decision:** add a multi-criteria `FitnessContract` created before action and a `ResultantEvaluation` after action.

Minimum dimensions:

```text
intent alignment
acceptance tests
source fidelity
evidence gain
uncertainty reduction
regression risk
complexity added
cost and latency
reversibility
transferability
operator burden
side effects
```

Do not reduce fitness to one self-optimized scalar. Hard constraints and independent tests take precedence over a score.

### G7 — No Safe Action Transaction

A plan needs more than approval. It needs atomicity, idempotency and recovery.

**Decision:** every executable cycle requires:

```text
target snapshot hash
single-writer lock
budget
plan hash
checkpoint
staging area
idempotency key
rollback bundle
post-action snapshot
```

A stale snapshot, expired budget, conflict or failed preflight blocks execution.

### G8 — No Autonomy Axis

Readiness L0-L3, cognitive depth D0-D3 and action authority are independent, but autonomy is not yet formalized.

**Decision:** add a separate autonomy axis:

```text
A0 manual
   runs only on explicit command

A1 observe_and_propose
   responds to approved events and emits packets; no project writes

A2 bounded_project_action
   performs reversible, pre-authorized project-local actions

A3 event_driven_operation
   schedules and initiates bounded cycles under budgets and rate limits

A4 governed_self_evolution
   generates and tests candidate capabilities; promotion remains independent
```

A system may be `L3/A1/proposal_only/D3`. Runtime readiness never implies autonomy or authority.

### G9 — Memory Is Recorded But Not Fully Metabolized

Delta logging alone does not define what becomes durable, what decays and what is revisited.

**Decision:** use four memory classes:

```text
source      immutable or versioned operator/project lineage
reflection  candidate interpretation that may decay
rule        accepted invariant or operating rule
a residue   rejected, superseded or currently unplaceable material with revisit triggers
```

Every memory item needs provenance, status, freshness, supersession and review conditions. Raw reasoning is not project memory.

### G10 — Capability Production Is Not Closed

RepoKernel can identify the need for skills, but lacks the full candidate-forge protocol.

**Decision:** capability generation follows:

```text
demonstrated capability gap
-> capability specification
-> isolated candidate artifact
-> static and synthetic tests
-> bounded real case
-> evidence packet
-> promotion decision
-> registry update or residue
```

Candidate tools and skills run in isolation and are disabled by default. Temporary capabilities may dissolve after the task; the evidence and resultant remain.

### G11 — Trigger, Queue And Cascade Semantics Are Missing

Event-driven operation requires bounded wake-up and propagation behavior.

**Decision:** define:

```text
whitelisted trigger types
deduplication key
debounce and rate limit
priority and expiry
read or acknowledgement state
causal parent
cascade targets
maximum fan-out
```

A cascade communicates context and impact, not detailed commands, and never grants authority to the receiver.

### G12 — Security And Trust Model Is Incomplete

Prompt injection is recognized, but autonomy adds supply-chain, secret and extension risks.

**Decision:** before A2 require:

```text
project trust decision
source instruction classification
secret and sensitive-path exclusion
extension provenance and allowlist
network policy
tool capability declaration
filesystem boundary
resource budget
kill switch and watchdog
tamper-evident event log
```

### G13 — No Empirical Proof Of Reduced Latency

The recursive method is plausible but the project has not yet demonstrated that it lowers total time or rework.

**Decision:** evaluate against a direct baseline using:

```text
time to accepted packet
time to implementation acceptance
number of clarification cycles
rework commits or patches
rollback rate
operator interventions
false-trigger rate
scope expansion
accepted reusable guards or skills
```

Do not claim exponential or latency gains until measured.

### G14 — Too Many Post-Phase-0 Gates

Schema horizon, recursive distillation and autonomy analysis risk becoming separate sequences that future instances must reconstruct.

**Decision:** create one post-Phase-0 convergence gate. Existing packets become inputs to that gate, not independent execution paths.

## Reconfigured Architecture

### Plane 1 — Intent And Kernel

```text
IntentContract
SourceManifest
ProjectModel
SeedSpec
accepted state
boundaries
registry
```

This plane is slow-changing and cannot be rewritten by an active cycle without promotion.

### Plane 2 — Perception And Cognition

```text
ContextSnapshot
TensionReport
observer or cognitive profile
recursive-improvement-distiller
ResultantPacket
```

This plane can interpret, compare and propose. It has no implicit write authority.

### Plane 3 — Operation

```text
CycleState
ActionPlan
AutonomyPolicy
AuthorityPreflight
ExecutorAdapter
Checkpoint
RollbackBundle
EventLedger
```

This plane performs only what the accepted policy allows.

### Plane 4 — Evaluation And Evolution

```text
FitnessContract
ObservationReport
ResultantEvaluation
LearningDelta
CapabilityGap
EvolutionProposal
PromotionDecision
```

This plane decides whether a change improved the project and what should persist.

### Cross-Cutting Governance

```text
role and approval matrix
budgets
trust and security
freshness
lineage
locks and concurrency
watchdog and kill switch
audit and recovery
```

## Minimal Autopoietic Cycle

The first implementation should stop at **A1 observe-and-propose**:

```text
approved event
-> ContextSnapshot
-> Intent alignment
-> TensionReport
-> recursive ResultantPacket
-> FitnessContract proposal
-> operator review
-> sleep
```

No automatic project write, skill generation or runtime escalation is required to prove this cycle.

### A1 Acceptance Tests

1. A deterministic low-value event produces `no_cycle` or D0, not deep recursion.
2. A repeated failure produces one tension with source references and a bounded ResultantPacket.
3. Conflicting sources remain conflicts.
4. The packet cannot alter authority or IntentContract.
5. Duplicate events do not generate duplicate cycles.
6. A missing external fact blocks the cycle instead of being invented.
7. An evaluator can reject the Resultant independently.
8. Crash recovery reconstructs the last persisted cycle state.
9. The event log links trigger, snapshot, tension, resultant and stop reason.
10. Compared with direct work, the evaluation records measured or explicitly estimated rework effects.

## Deferred Until A1 Is Proven

```text
A2 project-local writes
A3 autonomous scheduling
A4 capability generation
multi-node polling and cascade transport
external network actions
secrets
self-hosted model selection
cross-repository operation
automatic promotion
```

## Package Boundary

Recommended future distribution:

```text
repokernel-core
  compiler, schemas, reference seeds, retrofit, evidence and L0-L2

repokernel-cognition
  recursive distillation, cognitive profiles and ResultantPacket

repokernel-cycle
  ContextSnapshot, tension, cycle state, fitness and memory metabolism

repokernel-runtime
  optional events, sessions, tools and execution adapters
```

The first public release remains `repokernel-core`. Other layers are optional and must declare compatibility and authority requirements.

## Final Decision

```text
Do not add an autonomous loop directly to the current runtime architecture.
First formalize intent, perception, tension, fitness and separation of duties.
Then prove A1 observe-and-propose.
Only after independent evaluation and recovery tests should local reversible action be enabled.
```
