# Recursive Distillation Plane

Date: 2026-06-23  
Status: candidate cognitive plane; no implementation authority by itself

## Resultant

RepoKernel already defines how a project is generated, reentered and governed. What is still missing is the operator that turns friction, uncertainty or a local discovery into the **smallest high-leverage improvement**.

That operator should not become a new readiness level. L0-L3 continue to describe project readiness. Recursive distillation is an optional processing plane that can operate at any level.

```text
Project Kernel + objective or tension + evidence
-> recursive improvement distillation
-> ResultantPacket
-> Codex implementation
-> verification
-> durable delta
```

Internal codename: `Forge-R`.

## Why It Exists

A simple task should remain simple. Deep recursion on every task would increase latency.

The purpose of Forge-R is to spend additional reasoning only when it is likely to reduce larger downstream costs:

```text
orientation latency
+ search latency
+ rework latency
+ handoff latency
+ propagation latency
```

The governing rule is:

```text
shallow by default;
deepen only when ambiguity, leverage or recurrence justifies it;
stop when marginal novelty no longer changes the move.
```

## Relation To L2

L2 says that a project can preserve proposals, evidence and accepted deltas. Forge-R is the cognitive operator that can produce those objects.

```text
L2 = governed-improvement capacity
Forge-R = adaptive improvement procedure
```

Forge-R does not grant write, publish, deploy, network or cross-repository authority.

## Adaptive Depth Profile

### D0 — Direct

Use when the task is deterministic, bounded and low-risk.

```text
read -> act -> verify -> delta
```

No possibility expansion is needed.

### D1 — Source Ascent

Use when the request is ambiguous, the project has drifted, or repeated work suggests that the visible task is not the source problem.

Questions:

```text
What was the original intent?
Which accepted decision created the current state?
Where did latency or divergence first appear?
What is invariant and what is only current form?
```

### D2 — Possibility Field

Use when two or more plausible improvements exist or when the user asks for a better, deeper or unexpected route.

Techniques:

```text
question the question
extract the active tension or dipole
invert the dominant assumption
search the exception
shift scale
transfer the pattern to a nearby domain
construct a minimal counterfactual
```

The goal is not to maximize branch count. It is to expose distinct causal structures.

### D3 — Systemic Distillation

Use for high-impact architecture, repeated failures, transferable insight or changes likely to affect multiple project surfaces.

Techniques:

```text
prune incoherent or weak branches
unite branches that are the same structure from different angles
open the branch that reveals a new plane
extend from the local fix to the vulnerable neighborhood
map first- and second-order effects
translate the resultant into skill, test, guard, adapter or rule
```

D3 is the maximum default depth. Going deeper requires an explicit reason and a new evidence-bearing cycle, not automatic recursion.

## Trigger Conditions

Activate adaptive recursion when at least one condition is present:

- the task has multiple materially different valid routes;
- the same blocker, refactor or misunderstanding has appeared before;
- a local bug may indicate a repeated systemic condition;
- source documents conflict or the project intent is unclear;
- the requested change has broad architectural or public impact;
- the current solution is acceptable but the exception may expose a better level;
- the expected cost of rework is higher than the cost of one bounded recursive pass;
- the user explicitly asks for deeper possibilities, source ascent or the best route.

Do not activate it for obvious edits, deterministic checks, routine formatting or already-decided implementation work.

## Core Cycle

```text
0. Position
   Read state, active packet, source authority, target and boundary.

1. Regress
   Move backward from the visible task to the earliest causal source that still matters.

2. Separate
   Distinguish source, verified fact, inference, assumption, decision, residue and unknown.

3. Expand
   Produce a small field of structurally different possibilities.

4. Distill
   Apply prune / unite / open. Remove duplicate forms and weak branches.

5. Collapse
   Select one Resultant: the smallest complete move with the highest expected leverage.

6. Generalize
   Inspect the neighborhood: where else does the same condition apply?

7. Translate
   Produce an implementation-ready packet, tests, guard and rollback condition.

8. Verify
   Try to falsify the Resultant and check that authority did not expand.

9. Integrate
   Preserve only the durable delta and cascade implications to affected surfaces.
```

## Branch Scoring

Use qualitative or numerical scoring. The default dimensions are:

```text
intent_alignment
evidence_strength
expected_leverage
transferability
reversibility
implementation_cost
coordination_cost
uncertainty
entropy_added
```

A useful heuristic is:

```text
resultant_value =
  alignment * evidence * leverage * reversibility
  ------------------------------------------------
  cost + uncertainty + coordination + entropy
```

The score ranks branches; it does not replace operator judgment or evidence.

## ResultantPacket

Forge-R should emit one packet with:

```text
objective
source_anchor
current_tension
accepted_invariants
verified_facts
assumptions
unknowns
recursive_depth_used
techniques_used
possibilities_considered
branches_pruned
branches_united
opening_detected
resultant
why_this_move
files_or_surfaces_affected
implementation_steps
acceptance_tests
falsification_path
rollback_condition
neighborhood_implications
cascade_targets
memory_delta
residue
stop_reason
```

For Codex, the packet must be implementation-ready: exact files, boundaries, tests and acceptance criteria. It must not expose hidden chain-of-thought; only reviewable findings, evidence and decisions.

## Stop Rules

Stop recursion when any condition is true:

- the accepted objective and tests are satisfied;
- a single reversible move dominates the alternatives;
- two consecutive cycles add no materially new high-leverage branch;
- the remaining uncertainty requires an external source or operator decision;
- recursion begins repeating prior language without new evidence;
- the depth or resource budget is reached;
- further exploration would delay a safe direct action more than it could reduce rework.

A blocked result is valid when evidence is insufficient.

## Authority Boundary

Forge-R may alter observation, framing, branch selection and verification depth. It may propose files, patches, tests, skills, guards and packets.

It may not by itself:

```text
write accepted project state
approve its own plan
publish or deploy
use secrets
create or push remotes
modify another repository
raise runtime authority
promote a candidate capability
```

## Future Product Surface

A later command may expose the plane as:

```bash
python -m repokernel forge \
  --target . \
  --objective objective.md \
  --mode adaptive \
  --max-depth 3 \
  --dry-run
```

The first implementation should validate and package externally reasoned ResultantPackets. It should not embed an unrestricted autonomous model loop.

## Decision

```text
Keep the RepoKernel base path simple.
Add recursive distillation as an optional, bounded L2 improvement operator.
Use maximum depth only when the expected reduction in rework exceeds the cost of recursion.
```
