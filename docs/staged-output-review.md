# Staged Output Review

status: active_contract

RepoKernel staging writes proposals into an empty external review directory.
It is not an apply command and it must not mutate the target repository.

Every staged output should contain:

```text
REVIEW_ME_FIRST.md
.repokernel/state/CURRENT_STATE.md
.repokernel/packets/FIRST_PACKET.md
.repokernel/sources/SOURCE_ATLAS.md
AGENTS.md adapter delta
```

## REVIEW_ME_FIRST Contract

`REVIEW_ME_FIRST.md` tells the reviewer:

```text
plan_id:
target_mode:
target_path:
boundary:
first_safe_action:
approval_needed:
generated_or_proposed_files:
```

Read it before reviewing generated files, and before asking for any target
write, commit, PR, apply step or automation.

## Boundary

Staging creates evidence for review. It does not prove semantic acceptance,
production readiness, hosted CI, target compatibility or authority to write.
