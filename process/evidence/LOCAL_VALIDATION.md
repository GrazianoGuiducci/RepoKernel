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

## Minimal Product Path Proof

Fixture:

```text
examples/minimal/seed-spec.json
examples/minimal/source-manifest.json
examples/minimal/project-model.json
```

Commands:

```powershell
$env:PYTHONPATH='src'
python -m repokernel.cli validate-spec --kind seed-spec --input examples/minimal/seed-spec.json
python -m repokernel.cli validate-bundle --source-manifest examples/minimal/source-manifest.json --project-model examples/minimal/project-model.json --seed-spec examples/minimal/seed-spec.json
python -m repokernel.cli plan --seed-spec examples/minimal/seed-spec.json --source-manifest examples/minimal/source-manifest.json --project-model examples/minimal/project-model.json > plan.json
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

## Track A Core Conformance Proof

Review cycle:

```text
RK-RVW-20260625-01
```

Commands:

```powershell
python -m unittest discover -s tests/unit -v
$env:PYTHONPATH='src'
python -m repokernel.cli audit --path . --profile repokernel-source
python -m repokernel.cli validate-spec --kind seed-spec --input examples/minimal/seed-spec.json
python -m repokernel.cli verify-dist --seed-spec specs/reference/starter-l1.seed.json --dist-dir dist/reference/starter-l1
python -m build --sdist --wheel
```

Installed package proof:

```powershell
python -m venv <temp-venv>
<temp-venv>\Scripts\python.exe -m pip install dist\repokernel-0.3.0.dev0-py3-none-any.whl
Push-Location <outside-repo-dir>
<temp-venv>\Scripts\repokernel.exe --help
<temp-venv>\Scripts\repokernel.exe validate-spec --kind seed-spec --input C:\PVSC\ANTI_G\RepoKernel\examples\minimal\seed-spec.json
<temp-venv>\Scripts\python.exe -c "import repokernel, jsonschema; print('imports ok')"
Pop-Location
```

Result:

```text
unit tests: Ran 45 tests, OK
audit: ready true, readiness.level L2, failed []
minimal SeedSpec: valid true, python_errors [], schema_errors []
reference seed distribution: valid true
installed CLI outside repo: package-proof ok
```

Covered Track A behavior:

1. Draft 2020-12 JSON Schema execution and Python-validator parity.
2. Reviewed/version-bound SeedSpec with source/model hashes and accepted review status.
3. TargetSnapshot contract and read-only target inspection.
4. Existing repository retrofit blocked without snapshot evidence.
5. Content-aware planning: identical content leaves files unchanged; conflicting root files are review proposals or conflicts.
6. Unknown namespaced extensions are opaque and cannot affect the plan.
7. Public guide disclosure is deny-by-default for project fields and private sources.
8. Canonical project-kernel audit evidence no longer depends on self-attested Markdown phrases.
9. Reference Seed `starter-l1` verifies against generated distribution hashes.
10. Wheel includes runtime schema resources and console entry point works outside the source checkout.

Non-blocking warning:

```text
setuptools warns that pyproject project.license table form is deprecated and
should become a simple SPDX string before 2027-02-18.
```

Superseded by Track A correction proof below: the license warning was removed.

## Track A Readback Correction Proof

Review cycle:

```text
RK-RVW-20260625-01
```

Commands:

```powershell
python -m unittest discover -s tests/unit -v
$env:PYTHONPATH='src'
python -m repokernel.cli validate-bundle --source-manifest examples/minimal/source-manifest.json --project-model examples/minimal/project-model.json --seed-spec examples/minimal/seed-spec.json
python -m repokernel.cli plan --seed-spec examples/minimal/seed-spec.json --source-manifest examples/minimal/source-manifest.json --project-model examples/minimal/project-model.json
python -m repokernel.cli verify-dist --seed-spec specs/reference/starter-l1.seed.json --dist-dir dist/reference/starter-l1
python -m repokernel.cli audit --path . --profile repokernel-source
python -m build --sdist --wheel
```

Installed package proof:

```powershell
python -m venv <temp-venv>
<temp-venv>\Scripts\python.exe -m pip install dist\repokernel-0.3.0.dev0-py3-none-any.whl
Push-Location <outside-repo-dir>
<temp-venv>\Scripts\repokernel.exe --help
<temp-venv>\Scripts\repokernel.exe validate-bundle --source-manifest C:\PVSC\ANTI_G\RepoKernel\examples\minimal\source-manifest.json --project-model C:\PVSC\ANTI_G\RepoKernel\examples\minimal\project-model.json --seed-spec C:\PVSC\ANTI_G\RepoKernel\examples\minimal\seed-spec.json
<temp-venv>\Scripts\repokernel.exe verify-dist --seed-spec C:\PVSC\ANTI_G\RepoKernel\specs\reference\starter-l1.seed.json --dist-dir C:\PVSC\ANTI_G\RepoKernel\dist\reference\starter-l1
<temp-venv>\Scripts\python.exe -c "import repokernel, jsonschema; print('imports ok')"
Pop-Location
```

Result:

```text
unit tests: Ran 45 tests, OK
validate-bundle: valid true, errors []
plan: target-bound GenerationPlan emitted with bundle_provenance
verify-dist: valid true, errors []
audit: ready true, readiness.level L2, failed []
clean installed CLI outside repo: package-proof-correction ok
```

Correction coverage:

```text
contract parity matrix covers every current contract;
bundle hash/source-ref/compiler compatibility validation added;
TargetSnapshot path/hash/duplicate/exclusion validation added;
plan_id now binds compiler, seed, bundle, target identity, snapshot, policy and items;
stage rejects blocked plans;
Reference Seed verification regenerates expected output and fails on extras;
project-kernel audit uses canonical .repokernel paths;
source audit readiness depends on actual bundle/planner checks;
license table warning removed with SPDX string.
```
