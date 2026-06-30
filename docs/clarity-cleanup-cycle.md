# Clarity Cleanup Cycle

Status: L2 governance method

## Purpose

Dirty, stale or unclear files slow repository work because the next agent must
first decide whether each file is source, residue, generated output, operator
work, sensitive material or cleanup candidate.

RepoKernel treats this as clarity debt. The answer is not automatic deletion.
The answer is a small observe-and-propose loop that makes cleanup decisions
explicit before any destructive action.

## Core Rule

```text
unclear file state is an operational signal, not cleanup authority
```

Classify first. Mutate only after owner review, validation and a receipt.

## Loop

```text
observe worktree and project memory
-> classify dirty/unclear items
-> group by owner and risk
-> propose the smallest cleanup action
-> require gate for delete/move/ignore/bulk normalization
-> validate after action
-> preserve receipt only if it improves future reentry
```

## Inputs

Use only bounded repository evidence:

```text
git status / git diff summaries;
tracked-file inventory;
TargetSnapshot or Source Atlas;
CURRENT_STATE / FIRST_PACKET;
generated distribution verification;
existing cleanup or migration reports.
```

Do not read credentials, private logs, runtime streams or adjacent repositories
unless that surface has been explicitly selected.

## Classification

```text
path:
observed_state: dirty | untracked | generated | stale | duplicate | unknown
owner: current-agent | operator | generated-tool | external | unknown
risk: safe | review_required | sensitive | destructive
proposed_action: keep | commit | document | archive | ignore | delete_candidate | ask_owner
evidence:
gate:
receipt:
```

## Action Meanings

```text
keep:
  the file is valid state or evidence.

commit:
  the file belongs to the current accepted change.

document:
  the file is useful but needs source or boundary explanation.

archive:
  the file should stop acting as current authority but retain lineage.

ignore:
  the file is generated or local-only and should be excluded after review.

delete_candidate:
  the file appears useless or obsolete, but deletion still needs an explicit
  owner gate.

ask_owner:
  the file may be operator work, sensitive, adjacent-surface state or unclear.
```

## Generated Project Kernel Transfer

For L2 generated Project Kernels, RepoKernel stages:

```text
.repokernel/clarity/README.md
Project Clarity Rule in CURRENT_STATE
Clarity Intake in FIRST_PACKET
Clarity Cleanup Protocol in the project semantic skill
root AGENTS adapter text for dirty or unclear files
```

This gives the target project a local method for reducing noise without
granting autonomous cleanup authority.

## Boundary

This cycle does not authorize:

```text
deletion;
moving files;
rewriting history;
bulk formatting or line-ending normalization;
changing ignore rules;
cleaning adjacent repos;
publishing or pushing;
runtime/service actions.
```

Those actions remain separate, owner-gated mutations.
