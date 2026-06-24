# RepoKernel Phase 1 A1 Observe-And-Propose Gate

date: 2026-06-24
status: pending_after_p0_validation

## Objective

Prove that RepoKernel can observe a target repository and produce a bounded
proposal without writing to the target repository.

## Sequence

```text
synthetic_empty_target
synthetic_existing_target_with_root_authority
local_existing_repository_snapshot
external_style_repository_review
```

Do not skip directly to an external repository.

## Authority

```text
authority_mode: read | propose
target_write: forbidden
network: forbidden unless a later explicit external-style gate authorizes it
apply: absent
```

## Required Evidence

For each proof:

```text
inspect output
SeedSpec validation output
GenerationPlan output
no-write check
blocked/propose_update/conflict classification
human-readable proof report
```

## Pass Condition

```text
no files written to target
existing authority is not overwritten
root adapters are proposed, not forced
.repokernel/ remains the canonical control plane
private or withheld source labels do not appear in guide output
plan is reproducible from the same SeedSpec
```

## First Proof

Run only a local synthetic proof first. External-style proof is blocked until
the local proof report exists and passes review.
