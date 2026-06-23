# Departmental Autonomy — Spectral Regressive Analysis

Date: 2026-06-23  
Status: architecture decision candidate; no implementation authority by itself

## Executive Resultant

Use **two governance planes** and allow **bounded local microcycles** inside the second plane.

Do not create a third persistent governance layer for every subdomain.

```text
Plane 1 — Constitutional / Source Plane
  intent, invariants, shared authority, canonical contracts, common method

Plane 2 — Departmental / Holonic Plane
  local charter, sources, guides, methods, capabilities, fitness and evidence

Inside Plane 2 — Task Microcycles
  temporary D0-D3 loops for one objective; no independent constitutional authority

Between planes — Synaptic Membrane
  events, impact, provenance and priority; no hidden state or authority
```

The department is therefore a **bounded holon**: operationally capable inside its contract, but not sovereign over global intent, shared schemas, other departments or its own promotion.

## Regressive Source Ascent

The visible question is whether to add subcycles.

The causal objective behind it is:

```text
distribute context and decision work
without duplicating project truth,
creating recursive bureaucracy,
or forcing the operator to coordinate every local action.
```

The system does not need more hierarchical planes. It needs a clean separation between:

```text
global invariants
local application of those invariants
short-lived task processing
cross-boundary propagation
```

The D-ND CEC already gives the structural answer: domain canons are not a separate level from the axioms; they are the axioms **in action** in a specific domain. The generator produces the domain filter. RepoKernel should reproduce this pattern.

## Spectral Interpretation

The spectral question is not what each compartment contains, but how it responds to change, inversion and perturbation.

### Band Ω0 — Slow Constitutional Frequency

Changes rarely. Carries:

```text
seed invariant
mission
shared terminology
canonical source authority
authority model
cross-department constraints
core schemas
promotion policy
```

Characteristics:

```text
low frequency
high propagation radius
high review requirement
low tolerance for local override
```

A change in Ω0 must propagate downward through regenerated or reviewed departmental adaptations.

### Band Ω1 — Medium Departmental Frequency

Changes as the domain evolves. Carries:

```text
department charter
local objective space
local authoritative sources
domain canons and guides
method profile
capability registry
local fitness contract
active packet
local evidence and deltas
```

Characteristics:

```text
medium frequency
bounded authority
local memory
repeated workflows
explicit interfaces
```

Departments may observe, model, distill and propose autonomously. Bounded project-local action may be granted later by policy.

### Band Ω2 — Fast Task Frequency

Temporary microcycles for one problem or packet:

```text
D0 direct task
D1 source ascent
D2 possibility field
D3 systemic distillation
```

Characteristics:

```text
high frequency
short lifetime
small target
strict budget
no independent durable truth
```

A task cycle terminates in:

```text
resultant
evidence
local delta
cascade notice
or residue
```

It does not become a new department merely because it produced useful work.

### Band Σ — Synaptic Membrane

Not a third governance plane.

It transports:

```text
who acted
what changed
what opened
which source or artifact proves it
who is affected
priority and expiry
required acknowledgement
```

It does not transport detailed micromanagement or implicit authority.

## Structural Decision

```text
Two persistent planes.
One level of persistent departments.
Ephemeral microcycles inside departments.
No indefinite nesting.
```

A department may contain tools, skills and task packets. It should not contain another autonomous department by default.

A subdepartment is justified only when a stable domain has its own source authority, fitness, cadence, state and low-coupling interface. Otherwise use:

```text
profile
guide
skill
capability
projection
task packet
```

## Department As Holon

Each department receives a local contract from the global kernel.

Candidate canonical surface:

```text
.repokernel/departments/<department-id>/
  charter.json
  state/current.md
  sources/atlas.md
  methods/profile.md
  guides/
  capabilities.json
  fitness.json
  packets/active.md
  evidence/
  deltas/
  proposals/
  events/inbox.jsonl
  events/outbox.jsonl
```

This is a future contract candidate, not a current implementation instruction.

### Department Charter

Minimum fields:

```text
department_id
purpose
owned_problem_space
non_goals
inherited_invariants
local_sources
local_authority
interfaces
inputs
outputs
fitness_criteria
escalation_conditions
promotion_route
lifecycle_state
```

## Inheritance Without Duplication

Principles, methods and guides should distribute through compilation and reference, not copy-paste.

```text
global invariant
-> departmental canon
-> local guide or method
-> active packet
-> task action
```

Rules:

1. Global principles remain canonical at Plane 1.
2. Departments record how a principle applies locally.
3. A local guide cites the global principle and local evidence.
4. A local adaptation cannot silently redefine the source principle.
5. If the global invariant changes, affected local adaptations become stale and require regeneration or review.
6. Stable local rules may be proposed upward; they do not promote themselves.

## Local Autonomy

### Default Department Mode

```text
readiness: L2
autonomy: A1 observe_and_propose
authority: propose
cognitive depth: adaptive D0-D3
```

A department may:

- monitor authorized local sources;
- maintain local state, packets and evidence;
- generate domain-specific guides and method applications;
- run bounded analytical microcycles;
- evaluate local resultants against its fixed fitness contract;
- propose local rules, skills, guards and changes;
- send cascade notices to affected departments.

It may not:

- modify global mission or seed invariants;
- raise its own authority;
- alter another department's state;
- accept its own promotion;
- rewrite shared schemas or canonical methods;
- trigger unbounded cross-department cascades;
- create persistent nested departments without review.

### Later A2 Mode

A department may receive A2 only for reversible, pre-authorized local actions with:

```text
target boundary
snapshot hash
single-writer lock
budget
idempotency
checkpoint
rollback
independent evaluation
```

## When A Department Is Justified

Create a department only when the candidate domain satisfies most of these tests:

1. **Distinct intent subspace** — it owns a coherent part of the project mission.
2. **Source locality** — it has sources not required by every other compartment.
3. **Repeated cadence** — its work recurs enough to justify persistent state.
4. **Local fitness** — success can be evaluated locally without redefining global success.
5. **Bounded interface** — inputs and outputs can be stated explicitly.
6. **Low write coupling** — it rarely needs to modify another department directly.
7. **Context compression** — local specialization reduces global context load materially.
8. **Stable responsibility** — one accountable owner or role can be identified.

If these conditions are weak, create a skill, guide, projection or task packet instead.

## When A Microcycle Is Justified

A local microcycle is justified when:

```text
the objective is bounded
the state transition is observable
the evidence and stop rule are local
the output can be evaluated
the task recurs or carries non-trivial uncertainty
```

A simple deterministic action stays D0 and does not open a full cycle.

## Entropy Model

Departmental entropy grows through:

```text
duplicated canonical truth
competing state files
cross-department writes
unbounded event fan-out
stale local adapters
local metrics that oppose global intent
nested cycles without stop rules
permanent memory of temporary reasoning
```

Treat entropy as an audit vector, not a single magic score.

### Entropy Budget

Default constraints:

```text
one canonical global intent
one active packet per department
one authoritative local state surface
no direct cross-department state mutation
bounded event fan-out
TTL and deduplication for events
D3 maximum default depth
periodic global reconciliation
promotion only through independent review
```

## Coupling Rules

### Global To Department

May transmit:

```text
intent
invariants
constraints
shared terminology
canonical method updates
authority policy
cross-project decisions
```

### Department To Global

May transmit:

```text
resultants
evidence
local invariant candidates
capability gaps
fitness outcomes
architecture tensions
promotion proposals
```

### Department To Department

May transmit only through explicit interfaces or synaptic events:

```text
context
impact
artifact reference
priority
expiry
requested acknowledgement
```

The receiving department chooses how to act within its own contract.

## Promotion And Reconciliation

A local rule migrates upward only when:

- it survived repeated local use;
- it applies beyond one immediate task;
- evidence and failure conditions are explicit;
- another domain or independent evaluator can reproduce it;
- what must not travel is declared;
- promotion reduces total duplication or rework.

Periodic reconciliation compares:

```text
global intent vs department charter
global principles vs local canons
local state vs active packet
local metrics vs global mission
events sent vs acknowledged implications
```

## Spectral Diagnostics

The first prototype should measure structure under perturbation rather than merely inventory contents.

Candidate tests:

### Local Perturbation Test

Change one local task or guide.

Expected:

```text
local cycle absorbs the change
no unrelated department state changes
only significant implications cross the membrane
```

### Global Perturbation Test

Change a shared invariant.

Expected:

```text
affected department adapters become stale
review is requested
unaffected departments remain stable
```

### Shuffle Test

Randomize event order in a synthetic trace.

If the same outcome remains, the result may depend on event distribution rather than causal order. If it changes materially, sequence and lineage must be preserved.

### Coupling Test

Perturb one department's state and measure how many other compartments require changes.

High coupling indicates a false department boundary or missing shared service.

### Saturation Test

If repeated microcycles reproduce the same tensions without a new resultant, crystallize a rule, escalate the unresolved boundary or terminate the cycle.

## Pilot

Do not create many departments immediately.

After Phase 0 and the convergence gate, run one synthetic A1 pilot:

```text
department: architecture-and-method
scope: docs, schemas and method proposals only
authority: propose
writes: none during autonomous cycle
inputs: accepted architecture, state, active packet, local evidence
outputs: one ResultantPacket and cascade map
```

Compare centralized and departmental operation on:

```text
context required
clarification cycles
duplicate instructions
rework
false cascades
operator interventions
quality of local evidence
alignment with global intent
```

## Final Decision

```text
Work between the first and second planes.
Give the second plane bounded departmental closure.
Allow fast local microcycles, but do not turn them into new governance planes.
Use one synaptic membrane for propagation.
Promote only stable resultants upward.
```

This preserves distributed intelligence without recursive bureaucracy.
