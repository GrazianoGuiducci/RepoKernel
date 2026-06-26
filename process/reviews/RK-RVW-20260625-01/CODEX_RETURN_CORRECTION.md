# Codex Return Correction - RK-RVW-20260625-01

date: 2026-06-25
status: track_a_corrections_implemented_pending_final_readback
scope: RepoKernel Track A corrections only
package_version: 0.3.0.dev0
correction_commit: 4390230 fix: close Track A readback corrections
readback_pointer_commit: commit containing this exact pointer
track_b_status: blocked
pilot_status: not executed and not modified

## Authority Used

The operator accepted:

```text
packets/FOR_CODEX/TRACK_A_READBACK_CORRECTIONS_2026-06-25.md
```

Executed scope:

```text
RepoKernel contracts, validators, bundle validation, TargetSnapshot policy,
planner binding, Reference Seed reproducibility, audit, CLI, tests, packaging
and governance records.
```

Not executed:

```text
former private pilot fixture;
Track B;
target apply or writes;
runtime/L3;
network automation;
public tester request;
Seed/THIA/Lab promotion.
```

## Files Changed

Core:

```text
src/repokernel/bundle.py
src/repokernel/version.py
src/repokernel/models.py
src/repokernel/snapshot.py
src/repokernel/planner.py
src/repokernel/staging.py
src/repokernel/cli.py
src/repokernel/audit.py
```

Contracts and package data:

```text
schemas/activation-report.schema.json
schemas/generation-plan.schema.json
schemas/project-model.schema.json
schemas/skill-registry.schema.json
schemas/target-snapshot.schema.json
src/repokernel/schemas/*.schema.json
pyproject.toml
```

Fixtures and reference distribution:

```text
examples/minimal/project-model.json
examples/minimal/seed-spec.json
specs/reference/starter-l1.seed.json
dist/reference/starter-l1/
```

Tests:

```text
tests/unit/fixtures.py
tests/unit/test_bundle.py
tests/unit/test_schema_validator_parity.py
tests/unit/test_snapshot.py
tests/unit/test_planner.py
tests/unit/test_cli.py
tests/unit/test_audit.py
tests/unit/test_verify_dist.py
tests/unit/test_schemas.py
```

Governance:

```text
CURRENT_STATE.md
process/FIRST_PACKET.md
process/evidence/LOCAL_VALIDATION.md
docs/compatibility-matrix.md
docs/guides/cli-reference.md
sources/bootstrap/SOURCE_ATLAS_v1.0.md
process/reviews/RK-RVW-20260625-01/CODEX_RETURN_CORRECTION.md
```

## Correction Summary

```text
R1 contract parity:
  all current contracts have valid/invalid parity fixtures.

R2 snapshot integrity:
  supplied TargetSnapshot is Python/schema validated before planning;
  tree_hash and target_snapshot_id are recomputed from entries;
  unsafe/duplicate paths and blocking warnings reject planning.

R3 target-bound plans:
  plan_id binds compiler version, seed hash, bundle provenance, target identity,
  snapshot hash, policy and item hash; after_hash is labelled
  projected_after_state.v1.

R4 bundle linkage:
  validate-bundle recomputes SourceManifest and ProjectModel canonical hashes,
  verifies SeedSpec linkage, verifies ProjectModel source refs and checks
  running package compatibility.

R5 ProjectModel evidence:
  assertions with status/source_refs are required; conflicts and unknowns are
  structural.

R6 audit:
  project-kernel profile reads canonical .repokernel surfaces; source readiness
  depends on actual bundle/planner checks.

R7 Reference Seed:
  verify-dist regenerates expected files with the compiler and rejects missing
  or extra output.

R8 CLI validation:
  plan requires valid bundle; guides validates inputs; stage rejects blocked
  plans; reports include provenance/package fields.

R9 privacy:
  snapshot exclusion policy redacts sensitive excluded paths and avoids reading
  excluded content.

R10 packaging:
  license field is now SPDX string; clean installed CLI proof passed.
```

## Commands And Results

```powershell
python -m unittest discover -s tests/unit -v
```

```text
Ran 45 tests
OK
```

```powershell
$env:PYTHONPATH='src'
python -m repokernel.cli validate-bundle --source-manifest examples/minimal/source-manifest.json --project-model examples/minimal/project-model.json --seed-spec examples/minimal/seed-spec.json
```

```text
valid: true
errors: []
package_version: 0.3.0.dev0
```

```powershell
$env:PYTHONPATH='src'
python -m repokernel.cli plan --seed-spec examples/minimal/seed-spec.json --source-manifest examples/minimal/source-manifest.json --project-model examples/minimal/project-model.json
```

```text
schema: repokernel.generation-plan.v1
blocked: false
bundle_provenance: present
target_identity: present
after_hash_kind: projected_after_state.v1
```

```powershell
$env:PYTHONPATH='src'
python -m repokernel.cli verify-dist --seed-spec specs/reference/starter-l1.seed.json --dist-dir dist/reference/starter-l1
```

```text
valid: true
errors: []
```

```powershell
$env:PYTHONPATH='src'
python -m repokernel.cli audit --path . --profile repokernel-source
```

```text
ready: true
readiness.level: L2
failed: []
contract_conformant: true
planner_conformant: true
```

Clean install proof:

```powershell
python -m build --sdist --wheel
python -m venv <temp-venv>
<temp-venv>\Scripts\python.exe -m pip install dist\repokernel-0.3.0.dev0-py3-none-any.whl
Push-Location <outside-repo-dir>
<temp-venv>\Scripts\repokernel.exe --help
<temp-venv>\Scripts\repokernel.exe validate-bundle --source-manifest C:\PVSC\ANTI_G\RepoKernel\examples\minimal\source-manifest.json --project-model C:\PVSC\ANTI_G\RepoKernel\examples\minimal\project-model.json --seed-spec C:\PVSC\ANTI_G\RepoKernel\examples\minimal\seed-spec.json
<temp-venv>\Scripts\repokernel.exe verify-dist --seed-spec C:\PVSC\ANTI_G\RepoKernel\specs\reference\starter-l1.seed.json --dist-dir C:\PVSC\ANTI_G\RepoKernel\dist\reference\starter-l1
<temp-venv>\Scripts\python.exe -c "import repokernel, jsonschema; print('imports ok')"
Pop-Location
```

```text
package-proof-correction: ok
validate-bundle valid: true
verify-dist valid: true
imports ok
```

## Deviations

```text
Hosted CI is still absent because the available GitHub token cannot write
.github/workflows/* without workflow scope.

The correction keeps package_version at 0.3.0.dev0; no alpha release/tag was
created.

JSON Schema cannot enforce normalized duplicate-path uniqueness as precisely as
Python validation; duplicate snapshot paths are enforced by Python tests.
```

## Remaining Blockers

```text
final GPT Pro readback on the correction commit;
operator decision to accept or request further correction;
explicit operator authorization before Track B;
pilot version lock update after acceptance;
hosted CI before public experimental distribution.
```

## Request

```text
Please run final GPT Pro Track A readback on the correction commit and decide
whether it is accepted_for_private_pilot.
```
