# RepoKernel Roadmap

Status: updated after the independent Phase 1 review.

## Phase 0 - Baseline Inventory And Cleanup

- Produce `process/reports/current-tree.json`.
- Produce `process/reports/migration-classification.json`.
- Produce `process/reports/link-check.json`.
- Mark V03 and V04 packets superseded while preserving provenance.
- Replace incomplete documentation surfaces.
- Correct registry/evidence drift without changing generator behavior.

Exit condition:

```text
zero unclassified tracked files
registry paths and evidence resolve
internal Markdown links resolve
source audit passes
git diff --check passes
one isolated Phase 0 commit
```

## Post-Phase-0 Convergence Gate

After explicit Phase 0 acceptance, open:

```text
packets/FOR_CODEX/POST_PHASE0_AUTOPOIETIC_CONVERGENCE_GATE.md
```

The gate must collapse schema horizon, recursive distillation, autopoietic
cycle, departmental topology and A1 proof plan into one reviewed resultant
before Phase 1 starts.

## Phase 1 - Canonical Schemas And Package Skeleton

- Establish canonical `SeedSpec`, source manifest, ProjectModel, file plan and
  activation report schemas.
- Create the package skeleton only after convergence acceptance.
- Preserve compatibility wrappers until parity tests pass.

Current status:

```text
implemented_as_prototype: src/repokernel/, schemas/, docs/guides/, tests/unit/
blocked_for_external_use: yes
active_gate: packets/FOR_CODEX/PHASE1_P0_HARDENING_PACKET_2026-06-24.md
external_review: packets/FOR_GPT_PRO/REPOKERNEL_PHASE1_GPT_PRO_INDEPENDENT_REVIEW_2026-06-24.md
```

## Phase 1 P0 - Hardening Before External Use

- Repair governance state after Phase 1 acceptance.
- Remove unsafe legacy public paths from README and quickstart.
- Make schemas and Python validators enforce real contracts.
- Fix canonical serialization and path safety.
- Make planner output deterministic and aligned to `.repokernel/`.
- Make guide projection privacy-safe and authority-aware.
- Correct audit readiness claims so files alone do not imply L2 readiness.
- Add a minimal read-only CLI for validation, inspection, planning, guides and
  audit. Keep `apply` absent.

Exit condition:

```text
unit tests pass
inventory and link check pass
audit does not overclaim readiness
README and quickstart do not route users to legacy writer scripts as Phase 1
read-only CLI exists without apply authority
remaining blockers are explicit before any A1 external-style test
```

## Phase 2 - Deterministic Planning And Dry Run

- Implement compile/plan/apply separation.
- Guarantee same reviewed SeedSpec -> same file plan.
- Keep write application behind dry-run/review gates.

## Phase 3 - A1 Observe-And-Propose Proof

- Run one synthetic new-repository proof.
- Run one existing-repository retrofit proof.
- Run one external-style observe-and-propose proof with no writes.

Active entry gate:

```text
packets/FOR_CODEX/PHASE1_A1_OBSERVE_AND_PROPOSE_GATE_2026-06-24.md
```

The local synthetic proof must pass before any external-style repository review.

Current proof evidence:

```text
process/reports/a1-local-no-write-proof-2026-06-24.md
```

## Seed/Lab Promotion Track

RepoKernel is a candidate D-ND/THIA/Lab/Seed capability, but it is not promoted
yet.

Current candidate brief:

```text
packets/FOR_CODEX/REPOKERNEL_SEED_LAB_PROMOTION_BRIEF_2026-06-24.md
```

Promotion remains blocked until an external-style A1 proof and an explicit
operator decision define whether Seed receives documentation, templates, CLI
wrapper, installer or capability contract.

## Deferred

- Executable L3 runtime.
- Seed promotion.
- Domain packs beyond the minimal proof.
- External public product claims beyond verified evidence.
