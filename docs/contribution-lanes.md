# Contribution Lanes

status: active_guidance

Use this guide when a local node, contributor or agent works on RepoKernel
while also receiving upstream updates.

## Rule

Keep one clean lane and one contribution lane.

```text
clean lane:
  canonical checkout aligned to origin/main; receive updates here.

contribution lane:
  branch, worktree or patch for local discoveries, audit fixes and experiments.
```

Do not mix both lanes in the same dirty checkout. The clean lane keeps
RepoKernel easy to update; the contribution lane keeps local learning
reviewable.

## Handoff Shape

When another node reports a contribution, preserve these fields:

```text
base_commit:
clean_lane_path:
contribution_lane_path:
patch_path:
problem_fixed:
files_changed:
tests_run:
result:
remaining_boundary:
```

If the patch is not locally available, record it as `pending_contribution`
instead of recreating it from memory.

## Boundary

This rule does not authorize forced pulls, resets, history rewrites, target
writes, apply behavior, runtime activation or secret transfer. It only
separates update intake from reviewed contribution work.
