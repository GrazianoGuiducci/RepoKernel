# Post-Phase-0 — Recursive Improvement Distiller

Date: 2026-06-23  
Status: design and self-application gate; no Phase 0 scope change

## Purpose

Use the `recursive-improvement-distiller` skill to reduce implementation latency before Phase 1 by recursively distilling the Phase 1 schema and package problem into one high-leverage, testable Codex packet.

This is the first autological use of the new operator:

```text
RepoKernel applies its improvement method to its own next implementation phase.
```

## Prerequisites

Do not execute this packet until:

1. Phase 0 is complete and explicitly accepted.
2. The current-tree inventory and migration classification have zero unclassified tracked files.
3. Registry and evidence paths resolve.
4. `POST_PHASE0_SCHEMA_HORIZON_2026-06-23.md` has been reviewed.

This packet does not authorize Phase 1 implementation by itself.

## Read Order

```text
docs/recursive-distillation-plane.md
skills/recursive-improvement-distiller/SKILL.md
docs/possibility-horizon.md
packets/FOR_CODEX/POST_PHASE0_SCHEMA_HORIZON_2026-06-23.md
packets/FOR_CODEX/GPT_PRO_REPOKERNEL_FINAL_ARCHITECTURE_AND_CODEX_PACKET_2026-06-23.md
packets/FOR_CODEX/GPT_PRO_REPOKERNEL_FINAL_ARCHITECTURE_APPENDIX_2026-06-23.md
process/reports/current-tree.json
process/reports/migration-classification.json
```

## First Self-Application

### Objective

```text
Distill the smallest Phase 1 architecture that preserves future recursive potential without overloading the first stable schemas or increasing authority.
```

### Required Depth

Start at D1. Escalate to D2 or D3 only when justified by unresolved structural alternatives.

```text
D1: recover the source intent of Phase 1 and identify where schema complexity entered
D2: compare structurally different schema/package routes
D3: unite equivalent routes, expose hidden dependencies and extract guards/tests
```

### Required Techniques

Use only where productive:

```text
source ascent
question the question
assumption inversion
exception scan
scale shift
prune / unite / open
neighborhood expansion
falsification
```

## Deliverable A — Resultant Packet

Create:

```text
packets/FOR_CODEX/FORGE_R_PHASE1_RESULTANT.md
```

It must contain the complete `ResultantPacket` fields defined by the skill:

```text
objective
source_anchor
current_tension
accepted_invariants
verified_facts
assumptions
unknowns
conflicts
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

The packet must be concise enough to implement and detailed enough to test. It must not expose private chain-of-thought; record only reviewable evidence, alternatives and decisions.

## Deliverable B — Codex Phase 1 Delta

Create a proposed replacement or amendment for the Phase 1 section of the final architecture packet.

It must answer:

1. Which schemas are strictly required first?
2. Which fields are core, optional or namespaced extensions?
3. Which future concepts should remain outside v1?
4. What is the smallest package skeleton that proves canonical hashing, path safety and schema dispatch?
5. What tests prevent future extension fields from escalating authority?
6. What can be deferred without blocking Reference Seeds or retrofit?

Do not modify the final architecture packet until the Resultant is reviewed.

## Deliverable C — Skill Evaluation Record

Create:

```text
process/evidence/RECURSIVE_IMPROVEMENT_DISTILLER_PHASE1_EVAL.md
```

Record:

```text
trigger_correctness
selected_depth
branches_before_distillation
branches_after_distillation
implementation_scope_before
implementation_scope_after
new_tests_or_guards
time_or_rework_expected_to_be_saved
limitations
operator_review_status
```

Do not claim latency reduction as proven unless measured. A reasoned expectation must be labeled as an estimate.

## Later Prototype — `repokernel forge`

Do not implement this command during the self-application gate.

After the canonical schemas and deterministic planner exist, a bounded prototype may provide:

```bash
python -m repokernel forge \
  --target . \
  --objective objective.md \
  --mode adaptive \
  --max-depth 3 \
  --dry-run
```

The initial prototype should:

- load the canonical Project Kernel and selected evidence;
- create a target-bound context snapshot;
- emit a ResultantPacket template;
- validate a completed ResultantPacket;
- translate the accepted packet into an implementation packet;
- never call an unrestricted model loop;
- never apply patches or increase authority.

## Future Schema Candidate

Consider, but do not freeze automatically:

```text
repokernel.resultant-packet.v1
```

Potential core fields:

```text
packet_id
objective
source_refs
accepted_invariants
current_tension
recursive_depth
techniques
resultant
implementation_contract
validation_contract
rollback_condition
cascade
residue
stop_reason
authority_mode
extensions
```

Any unknown extension must round-trip without affecting planning, writes or authority.

## Acceptance Criteria

The self-application passes when:

- D0 is rejected for a documented reason or selected if Phase 1 is already sufficiently clear;
- no more than five materially distinct branches are explored;
- duplicate branches are explicitly united;
- the selected Resultant reduces or clarifies implementation scope;
- exact tests and rollback conditions are provided;
- no new runtime, network or external-action authority is introduced;
- the evaluator records limitations and operator review status;
- Phase 1 remains blocked until the Resultant is accepted.

## Boundary

Do not use recursive depth as a reason to expand scope indefinitely.

Do not implement projections, federation, internal runtime, autonomous promotion or large Domain Pack systems here.

The purpose is:

```text
more possibility before selection;
less complexity after distillation;
less rework between architectural intent and Codex implementation.
```
