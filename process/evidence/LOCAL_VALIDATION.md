# Local Validation

Date: 2026-06-25

Repository-hosted validation: passed

## Phase 1 P0 Hardening Tests

Command:

```powershell
$env:PYTHONPATH='src'
python -m unittest discover -s tests/unit -v
```

Result:

```text
Ran 18 tests
OK
```

Covered behavior:

1. Canonical JSON order is stable.
2. Non-finite JSON numbers are rejected.
3. Namespaced extensions round-trip and cannot raise authority.
4. Private and non-public-guide sources are excluded from guide output.
5. Dry-run writes nothing.
6. Existing root `AGENTS.md` becomes a reviewable proposal, not an overwrite.
7. Plans use the `.repokernel/` control plane.
8. Same SeedSpec produces the same plan metadata and item hashes.
9. Unsafe Windows drive-style paths are rejected.
10. Contract validators accept minimal valid contracts.
11. Schema files parse as JSON.
12. SeedSpec validation requires `seed_id` and safe target paths.
13. CLI `validate-spec` returns a valid structured report.
14. CLI `plan` emits a GenerationPlan without writing target files.
15. CLI `guides` withholds private source labels.
16. CLI `inspect` is read-only.
17. CLI `stage` writes proposed files only to an explicit staging directory.
18. CLI `stage` rejects non-empty staging directories.

## Historical Note

The previous 2026-06-23 overlay validation remains historical evidence only.
The active evidence for repository-hosted Phase 1 work is the command above plus
the current audit and inventory reports.

## CLI Smoke Validation

Commands:

```powershell
$env:PYTHONPATH='src'
python -m repokernel.cli audit --path . --profile repokernel-source
python -m repokernel.cli stage --plan <plan.json> --output-dir <empty-staging-dir>
python scripts/audit_repokernel_project.py --path . --profile repokernel-source --json
```

Result:

```text
ready: true
readiness.level: L2
failed: []
```

## Post-Call RepoKernel Validation - 2026-06-25

Context:

```text
Denis call concluded.
Previous/visible Denis repositories are obsolete.
Material was shared by the operator for testing.
RepoKernel focus returned to local product hardening.
```

Commands:

```powershell
python -m pytest -q
$env:PYTHONPATH='src'; python -m repokernel.cli audit --path . --profile repokernel-source
git diff --check
```

Result:

```text
pytest: 18 passed
audit.ready: true
audit.readiness.level: L2
audit.failed: []
git diff --check: no errors; CRLF warnings only
```

Boundary confirmed:

```text
obsolete Denis repositories are not proof targets;
no external repository write;
no public tester request;
feedback on shared material remains pending.
```

## Minimal Product Path Proof

Fixture:

```text
examples/minimal/seed-spec.json
examples/minimal/source-manifest.json
```

Commands:

```powershell
$env:PYTHONPATH='src'
python -m repokernel.cli validate-spec --kind seed-spec --input examples/minimal/seed-spec.json
python -m repokernel.cli plan --seed-spec examples/minimal/seed-spec.json > plan.json
python -m repokernel.cli stage --plan plan.json --output-dir <empty-staging-dir>
python -m repokernel.cli guides --seed-spec examples/minimal/seed-spec.json --source-manifest examples/minimal/source-manifest.json
python -m repokernel.cli audit --path . --profile repokernel-source
```

Result:

```text
SeedSpec valid: true
staged files:
  AGENTS.md
  README.md
  .repokernel/packets/FIRST_PACKET.md
  .repokernel/skills/minimal-project-semantic-kernel/SKILL.md
  .repokernel/sources/SOURCE_ATLAS.md
  .repokernel/state/CURRENT_STATE.md
target_writes_performed: []
guides include: Minimal example README
audit ready: true
```

## A1 Local No-Write Proof

Report:

```text
process/reports/a1-local-no-write-proof-2026-06-24.md
```

Result:

```text
inspect_boundary: read_only
SeedSpec valid: true
AGENTS.md action: propose_update
README.md action: propose_update
private_label_leaked: false
no_extra_target_files: true
```
