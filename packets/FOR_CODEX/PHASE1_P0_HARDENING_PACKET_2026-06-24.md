# RepoKernel Phase 1 P0 Hardening Packet

date: 2026-06-24
status: active

## Trigger

The independent GPT Pro Phase 1 review accepted the architectural direction but
classified the current Phase 1 implementation as a useful prototype skeleton,
not yet a collaborator-safe or public installer-ready compiler.

Source review:

```text
packets/FOR_GPT_PRO/REPOKERNEL_PHASE1_GPT_PRO_INDEPENDENT_REVIEW_2026-06-24.md
```

## Operator Decision

Phase 1 is accepted by operator delegation for continued implementation, but it
is not accepted as externally usable.

```text
accepted: Phase 1 direction, package skeleton, guides as working surfaces
not_accepted_yet: external repository pilot, public installer path, collaborator use
```

## Required P0 Corrections

1. Repair governance state.
2. Remove unsafe legacy public path.
3. Make schemas and Python validators enforce real contracts.
4. Fix canonical serialization.
5. Fix path safety.
6. Fix planner determinism and `.repokernel/` layout.
7. Fix guide disclosure and authority boundaries.
8. Correct audit readiness claims.
9. Add a minimal read-only CLI: `validate-spec`, `inspect`, `plan`, `guides`,
   `audit`; keep `apply` absent until a later reviewed gate.

## Boundary

```text
allowed: RepoKernel docs, process state, schemas, src/repokernel, tests and local validation scripts
blocked: third-party repo writes, d-nd-seed promotion, runtime/L3 implementation, autonomous apply mode and public product claims
```

## Minimum Validation

```text
python -m unittest discover -s tests/unit -v
python scripts/phase0_inventory.py
python scripts/audit_repokernel_project.py --path . --profile repokernel-source --json
$env:PYTHONPATH="src"
python -m repokernel.cli audit --path . --profile repokernel-source
git diff --check
```

## Exit Condition

RepoKernel can move to an external-style A1 observe-and-propose test only when
the P0 corrections above pass local validation and the active documents no
longer advertise legacy scaffold scripts as the primary Phase 1 path.
