# 2026-06-30 - Clarity Cleanup And Meta-Skill Map

status: accepted local implementation

## Trigger

The operator noted that dirty or unclear files slow agent performance and asked
whether additional local meta-skills should be added to the RepoKernel
meta-kernel.

## Decision

Add a neutral clarity cleanup faculty to RepoKernel and map local ANTI_G
meta-skills to their transferable RepoKernel equivalents.

## Change

```text
docs/clarity-cleanup-cycle.md:
  defines observe -> classify -> propose -> gate -> receipt cleanup flow.

docs/meta-skill-integration-map.md:
  maps local meta-skills to neutral RepoKernel treatment and blocks private
  residue from public transfer.

skills/clarity-cleanup-steward/SKILL.md:
  adds a safe classifier skill for dirty/unclear file state.

planner output:
  stages Project Clarity Rule, Clarity Intake, Clarity Cleanup Protocol and
  .repokernel/clarity/README.md into generated Project Kernels.

scripts/phase0_inventory.py:
  classifies CI workflow files, MANIFEST.in, reference SeedSpecs and reference
  distributions so current inventory reports can return to zero unclassified
  files after the new generated/reference surfaces are tracked.
```

## Boundary

No automatic cleanup, deletion, file moves, ignore-rule changes, formatter runs,
history rewrites, adjacent-repo mutations, TM7 mutations, runtime hooks or
background automation were authorized.

## Validation

Run the RepoKernel audit, unit tests and reference distribution verification
after regeneration.

## Next Safe Action

Use `clarity-cleanup-steward` before cross-node handoff when dirty or unclear
files exist, especially in shared surfaces such as `tm7`.
