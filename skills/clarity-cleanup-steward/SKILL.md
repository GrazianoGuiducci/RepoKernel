---
name: clarity-cleanup-steward
description: Use when a RepoKernel project has dirty, untracked, stale, duplicate or unclear files and needs a non-destructive classification before cleanup, commit, archive, ignore or owner review.
---

# Clarity Cleanup Steward

Use this skill to reduce action noise before it becomes reentry debt.

It is a classifier and proposal skill. It is not a deletion tool, formatter,
history rewriter, scheduler or automatic cleanup daemon.

## Read

```text
CURRENT_STATE.md
sources/bootstrap/SOURCE_ATLAS_v1.0.md
docs/clarity-cleanup-cycle.md
git status / concise diff summary
existing inventory or migration reports when present
```

## Workflow

```text
observe worktree
-> classify unclear items
-> group by owner and risk
-> propose smallest useful cleanup
-> stop before destructive action
-> validate if an owner-approved cleanup is later performed
-> write receipt only when future reentry improves
```

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

## Rules

- Prefer one compact cleanup receipt over scattered notes.
- Treat operator changes as owner work until proven otherwise.
- Treat generated artifacts as generated only when the generator and expected
  output are known.
- Treat line-ending-only or stat-only changes as clarity issues, not content
  changes.
- Never delete, move, ignore, normalize in bulk or clean adjacent repositories
  without an explicit gate.

## Output

```text
ClarityCleanupReceipt:
  surface:
  checked:
  dirty_items:
  classifications:
  proposed_actions:
  blocked_actions:
  validation:
  next_safe_action:
```
