# Active Packet - Phase 1 P0 Hardening

date: 2026-06-24
status: authorized_phase1_p0_hardening

## Objective

```text
objective: harden the Phase 1 RepoKernel compiler skeleton before any collaborator, public or external-repository test
```

## Authoritative Package

```text
packets/FOR_CODEX/PHASE1_P0_HARDENING_PACKET_2026-06-24.md
packets/FOR_GPT_PRO/REPOKERNEL_PHASE1_GPT_PRO_INDEPENDENT_REVIEW_2026-06-24.md
packets/FOR_CODEX/FORGE_R_PHASE1_CONVERGED_RESULTANT.md
```

## Sources

```text
source_of_truth: authoritative package above; CURRENT_STATE.md; process/DECISION_LOG.md; sources/bootstrap/SOURCE_ATLAS_v1.0.md
```

## P0 Scope

```text
repair governance state after Phase 1 acceptance
remove unsafe legacy public path from README and quickstart
harden schemas and Python validators
fix canonical serialization and path safety
make planning deterministic and aligned to .repokernel/ layout
make guide projection privacy-safe and deny-by-default
correct audit readiness claims so prototype presence is not treated as L2 readiness
add a tester-safe staging surface that renders proposed files into a separate
  review directory without applying them to the target repository
```

## Boundary

```text
allowed: RepoKernel repository governance, documentation, Phase 1 core contracts, tests and local validation
needs_confirmation: external repository pilot, Seed promotion, runtime/L3 execution, downstream repository mutation and public product claims beyond evidence
out_of_scope: applying generated files to third-party repositories, changing d-nd-seed, changing Business Manager ownership, network automation and credentials
```

## First Move

```text
first_safe_action: preserve the independent review inside RepoKernel, record Phase 1 acceptance and create this P0 hardening gate
validation: unit tests, inventory/link check, audit, git diff --check, CLI smoke tests, staged review-bundle proof and explicit remaining blockers
```

## Required Codex Return

```text
exact files changed
validation output
remaining P0 blockers
commit identifier
```

## Memory Delta

```text
preserve: GPT Pro review findings, accepted P0 decisions, validation results, staged review-bundle behavior and blockers before external testing
do_not_preserve: speculative Phase 2 work, unreviewed runtime claims and external-repository assumptions
```
