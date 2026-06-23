---
name: recursive-improvement-distiller
description: Use when a project needs a higher-leverage improvement than the visible task suggests, especially under ambiguity, repeated friction, architectural impact, conflicting sources or a transferable local insight.
---

# Recursive Improvement Distiller

## Mandate

Turn a project tension, blocker, architectural question or significant local discovery into the smallest complete, evidence-backed and implementation-ready improvement.

Keep simple tasks direct. Escalate recursively only when the expected reduction in rework, drift or handoff latency justifies the additional reasoning.

## Position In RepoKernel

```text
L0-L3 = readiness levels
this skill = optional adaptive improvement operator
```

The skill operationalizes governed improvement at L2. It does not create a new readiness level and does not increase authority.

## Inputs

```text
objective_or_tension
current_project_state
active_packet
source_authority
accepted_decisions
available_evidence
target_repository_or_artifact
change_boundary
authority_mode
acceptance_criteria
resource_budget
requested_or_max_depth
```

## Trigger

Use when at least one condition applies:

- more than one materially different solution is plausible;
- a blocker, refactor or misunderstanding has recurred;
- a local bug or insight may generalize to neighboring surfaces;
- sources conflict or the original intent is obscured;
- the change is architectural, public, cross-surface or difficult to reverse;
- the current move is good but an exception may reveal a better plane;
- the user asks for source ascent, deeper possibilities or the best route.

Do not use for routine formatting, deterministic edits, already-approved implementation or simple checks.

## Adaptive Depth

### D0 — Direct

```text
read -> act -> verify -> delta
```

Use for bounded deterministic work.

### D1 — Source Ascent

Recover the earliest relevant cause, original intent, accepted invariants and the point where latency or divergence entered.

### D2 — Possibility Field

Generate a small set of structurally different branches using only relevant techniques:

```text
question_the_question
tension_or_dipole_extraction
assumption_inversion
exception_scan
scale_shift
domain_transfer
minimal_counterfactual
```

### D3 — Systemic Distillation

Apply:

```text
prune
unite
open
neighborhood_expansion
first_and_second_order_effects
guard_or_skill_extraction
```

D3 is the maximum default. Additional cycles require new evidence or an explicit operator reason.

## Workflow

### 0. Position

Read current state, active packet, target, source authority and action boundary. Do not reason from chat memory alone.

### 1. Regress To Source

Ask:

```text
What is the visible effect?
What decision, assumption or missing structure generated it?
What original intent still governs the work?
What changed between source and current form?
```

Stop the ascent at the earliest cause that remains actionable and evidenced.

### 2. Separate The Field

Classify each relevant element:

```text
operator_source
verified_fact
accepted_decision
inference
assumption
unknown
conflict
residue
```

Do not flatten conflicts or convert inference into fact.

### 3. Expand Possibilities

Produce no more than five materially distinct branches by default. Every branch must state:

```text
causal_model
expected_effect
evidence
risk
cost
reversibility
what_it_would_falsify
```

### 4. Distill

For each branch apply:

```text
prune: remove weak, duplicate or incoherent routes
unite: merge routes that share the same causal structure
open: retain the route that exposes a more useful level of the problem
```

Score remaining routes on:

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

### 5. Collapse To Resultant

Choose one move that is:

- complete enough to be useful;
- small enough to verify and reverse;
- strongly connected to accepted intent;
- likely to remove more future work than it creates;
- implementable within the declared boundary.

A blocked or evidence-requesting Resultant is valid.

### 6. Extend To The Neighborhood

After identifying the local move, inspect nearby surfaces sharing the same vulnerable or generative condition.

Do not expand scope automatically. Classify neighboring implications as:

```text
include_now
follow_up
new_skill_or_guard_candidate
cascade_notice
residue
```

### 7. Translate For Codex

Produce exact implementation instructions:

```text
files_to_read
files_to_create
files_to_modify
files_not_to_touch
ordered_steps
tests
acceptance_gate
rollback_condition
authority_boundary
```

### 8. Falsify And Guard

Attempt to disprove the selected Resultant. Check:

- whether a simpler direct move is sufficient;
- whether the source anchor is wrong or stale;
- whether the improvement only relocates complexity;
- whether a hidden authority escalation exists;
- whether a failed local pattern can recur nearby.

Where useful, convert the learned condition into a test, preflight, invariant, skill trigger or guard.

### 9. Preserve The Delta

Record only:

```text
accepted_resultant
supporting_evidence
new_or_changed_rule
validation_result
remaining_unknowns
next_safe_action
cascade_targets
```

Do not store raw internal reasoning or every discarded branch.

## ResultantPacket Output

```text
objective:
source_anchor:
current_tension:
accepted_invariants:
verified_facts:
assumptions:
unknowns:
conflicts:
recursive_depth_used:
techniques_used:
possibilities_considered:
branches_pruned:
branches_united:
opening_detected:
resultant:
why_this_move:
files_or_surfaces_affected:
implementation_steps:
acceptance_tests:
falsification_path:
rollback_condition:
neighborhood_implications:
cascade_targets:
memory_delta:
residue:
stop_reason:
```

## Stop Rules

Stop when:

- acceptance criteria are satisfied;
- one reversible move clearly dominates;
- two cycles add no new high-leverage branch;
- external evidence or an operator decision is required;
- the recursion repeats without new evidence;
- the resource budget is reached;
- direct action now costs less than further analysis.

## Boundary

This skill can propose and structure improvements. It cannot approve its own plan, modify accepted state without authorization, publish, deploy, use secrets, create remotes, raise runtime authority or promote itself.

## Embedded Evals

### Trigger Test

Input: “Rename this typo in one file.”  
Expected: remain at D0; do not expand possibilities.

Input: “We fixed the same state drift three times; improve the architecture.”  
Expected: activate D1-D3 and produce a ResultantPacket.

### Fidelity Test

Given conflicting sources, the output preserves the conflict, identifies the missing decision and does not invent a unified fact.

### Distillation Test

Given five superficially different branches that share two causal structures, the output unites them into two branches before selecting a Resultant.

### Latency Test

Given a deterministic task, recursive overhead remains near zero. Given a recurrent architectural failure, the packet includes a guard or test that reduces expected rework.

### Authority Test

No recursive depth, profile or extension may change `authority_mode`, authorize external action or bypass review.
