# RepoKernel Roadmap

Status: updated during Phase 0 cleanup.

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

## Phase 2 - Deterministic Planning And Dry Run

- Implement compile/plan/apply separation.
- Guarantee same reviewed SeedSpec -> same file plan.
- Keep write application behind dry-run/review gates.

## Phase 3 - A1 Observe-And-Propose Proof

- Run one synthetic new-repository proof.
- Run one existing-repository retrofit proof.
- Run one external-style observe-and-propose proof with no writes.

## Deferred

- Executable L3 runtime.
- Seed promotion.
- Domain packs beyond the minimal proof.
- External public product claims beyond verified evidence.
