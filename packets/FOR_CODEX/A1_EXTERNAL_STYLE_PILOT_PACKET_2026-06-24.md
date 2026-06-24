# A1 External-Style Pilot Packet

date: 2026-06-24
status: active_procedure_packet
authority: read_and_propose_only

## Purpose

This packet defines the first external-style RepoKernel pilot:

```text
observe a public or authorized repository;
derive a small Project Kernel proposal;
prove that RepoKernel can help without writing to the target;
stop before apply, PR, issue, fork or Seed promotion.
```

The pilot may be used for collaborators, partners, clients, creators or
friends. The relationship details belong in the appropriate private business or
contact surface, not in this public RepoKernel repository.

## Public / Private Split

RepoKernel may preserve:

```text
public repository structure;
public repository metadata;
generic project type;
generic setup gaps;
sanitized proposal pattern;
no-write evidence.
```

RepoKernel must not preserve:

```text
private messages;
email addresses;
calendar details;
commercial terms;
relationship judgments;
non-public project claims;
personal details not needed for the technical proposal.
```

## Required Gate

Before observing a real external target:

```text
target_url:
owner_identity_check:
homonym_check:
source_quality:
relationship_context_location:
allowed_sources:
write_authority: none
publication_boundary:
```

If identity or ownership is uncertain, stop and ask neutral clarification
questions. Do not merge sources by name similarity.

## Minimum Observation

Use direct repository evidence only:

```text
README and root files;
language/runtime manifests;
docs and guides;
tests and workflows;
deployment or Docker files;
recent activity;
existing assistant or project-state files;
evidence, benchmark or evaluation files.
```

Portfolio pages, social profiles and conversation notes may guide questions,
but they must not replace repository evidence.

## Classification

Classify the target as one or more:

```text
exploratory_learning
prototype
portfolio_project
production_candidate
client_or_business_project
research_or_ai_experiment
multi_repo_system
```

Then classify the lowest useful RepoKernel layer:

```text
L0 Reentry Core:
  entry gate, current state, first safe action, boundary.

L1 Semantic Kernel:
  source atlas, project vocabulary, assistant/coder instructions.

L2 Governed Improvement:
  evidence log, evaluation notes, review policy, memory deltas.

L3 Runtime Contract:
  proposal-only unless a later explicit runtime gate exists.
```

## Setup Capsule

Produce a capsule with:

```text
repo_or_profile:
owner_identity_confidence:
source_quality:
verified_sources:
homonym_or_ownership_risk:

observed_assets:
primary_languages:
frameworks_or_stack:
ai_or_agentic_components:
docs_present:
tests_present:
deployment_or_runtime_clues:
recent_activity:

project_type:
current_strengths:
setup_gaps:

RepoKernel_fit:
  L0_reentry_core:
  L1_semantic_kernel:
  L2_governed_improvement:
  L3_runtime_contract:

recommended_layer:
proposed_files:
what_not_to_touch:
conversation_angle:
pilot_shape:
operator_gate:
next_bounded_action:
stop_rule:
```

## Proposal Shape

Prefer the smallest useful overlay.

For a public external project:

```text
AGENTS.md or AI_ASSISTANT.md
CURRENT_STATE.md
docs/SOURCE_ATLAS.md
docs/EVALUATION_NOTES.md
docs/MEMORY_DELTA.md
```

For an internal RepoKernel-style target:

```text
.repokernel/state/CURRENT_STATE.md
.repokernel/sources/SOURCE_ATLAS.md
.repokernel/PROJECT_KERNEL.md
.repokernel/REVIEW_POLICY.md
.repokernel/deltas/MEMORY_DELTA.md
```

Do not propose all files by default.

## No-Write Proof

A valid A1 pilot must preserve evidence that:

```text
no target files were written;
no issue, PR, discussion, fork or message was created;
existing target authority was not overwritten;
the output is a proposal packet only;
private or withheld sources were not exposed in public guide output.
```

## Stop Condition

The pilot stops at:

```text
sanitized setup capsule;
optional private relationship/call packet;
operator decision;
no-write proof.
```

Any implementation requires a later apply gate with explicit target authority,
plan review, rollback strategy and post-write audit.
