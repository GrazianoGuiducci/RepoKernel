# TM7-vps Onboarding Feedback Integration

date: 2026-06-30
status: applied_and_locally_validated_with_pending_patch_reference

## Trigger

TM3/TM7-vps reported that `/opt/RepoKernel` is now a clean lane aligned to
`origin/main` at `5a179ef`, with local audit-fix work preserved in a separate
worktree/patch.

## Integrated

- Added clean lane / contribution lane guidance.
- Made the external coder first output contract explicit.
- Preserved `RepoKernel not needed` as a valid first-contact outcome.
- Added `REVIEW_ME_FIRST` staging contract and generation.
- Required public capability source recommendations to pin repository, ref and
  exact files read.
- Fixed the generated Starter L1 Project Kernel audit invariant locally by
  projecting `first_safe_action` and `memory delta` fields into generated
  output.

## Pending Contribution

The TM7-vps patch path was reported as:

```text
/tmp/repokernel-tm7-audit-fix.patch
```

No local copy was found in this workspace. Treat the VPS patch as a
`pending_contribution` unless TM3/TM7-vps sends the diff or the operator opens
an explicit SSH/import pass.

## Boundary

No shared TM7 state, private runtime state, secrets, target repositories,
public site surfaces or downstream projects were mutated by this delta.

## Validation

```text
starter_l1_project_kernel_audit: passed
repokernel_source_audit: passed
pytest tests/unit -q: 50 passed
verify-dist starter-l1: valid true
phase0_inventory: unclassified_count 0, broken_links 0
```
