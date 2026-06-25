# RepoKernel Compatibility Matrix

Status: living compatibility record  
Last architectural review baseline: `b5f7958c877314adba75e5c104342dd6c7024c45`

## Current Development Line

| Field | Current value | Status |
| --- | --- | --- |
| Package version | `0.3.0.dev0` | development only |
| Python | `>=3.11` | declared; clean wheel/CLI proof passed on local Windows node |
| SourceManifest | `repokernel.source-manifest.v1` | draft contract |
| ProjectModel | `repokernel.project-model.v1` | draft contract |
| SeedSpec | `repokernel.seed-spec.v1` | draft contract; accepted review, source/model hashes and compiler compatibility required |
| GenerationPlan | `repokernel.generation-plan.v1` | draft contract; target snapshot/hash fields and stage-only apply policy required |
| TargetSnapshot | `repokernel.target-snapshot.v1` | draft contract; read-only inspect and content-aware planning proof passed |
| ActivationReport | `repokernel.activation-report.v1` | draft/minimal; active reports require all checks ok |
| SkillRegistry | `repokernel.skill-registry.v1` and validator compatibility with v2 | draft/migration unresolved |
| CLI | `validate-spec`, `inspect`, `plan`, `stage`, `guides`, `audit`, `verify-dist` | local checkout and installed wheel path proven |
| Apply | absent | intentionally deferred |
| Canonical target | `.repokernel/` plus optional root adapters | accepted architecture |
| L0-L2 | first stable scope | Track A core conformance implemented locally; external readback pending |
| L3 | contract only | executable runtime deferred |
| Public distribution | blocked | private pilot first |

## Evidence Matrix

| Evidence | Baseline | Result | Limitation |
| --- | --- | --- | --- |
| Unit tests | Track A core conformance local checkout | 32 passed | hosted CI result pending |
| Schema validator parity | Draft 2020-12 plus Python validators | passed | additional negative fixtures can be expanded |
| Minimal validate/plan/stage/guides | local checkout | passed | hand-prepared minimal SeedSpec; public external fixture pending |
| TargetSnapshot planning | local synthetic fixtures | passed | real pilot pending Track B |
| Local A1 no-write proof | synthetic target | passed | not an external target; independent evaluation incomplete |
| Installed package proof | local clean venv, outside source checkout | passed | Windows local proof only; hosted matrix pending |
| Reference Seed reproducibility | `specs/reference/starter-l1.seed.json` | verify-dist passed | one starter distribution only |
| External-style procedure | public-safe procedure | ready | procedure only, not a completed neutral pilot |
| Distribution verdict | 2026-06-25 | private pilot first | collaborator/public use blocked |
| Denis pilot | private neutral scaffold | available | Track B intentionally not executed before core readback |

## Compatibility Rules

1. A Git branch is not a compatibility identifier; use a commit SHA or tag.
2. Pilot evidence applies only to the package/source/contract versions it records.
3. Draft contract IDs may change before the first alpha; every breaking change must be recorded.
4. Unknown namespaced extensions must round-trip but have no authority effect.
5. A newer package may read an older contract only when compatibility is tested and documented.
6. Generated artifacts must record compiler/source version and SeedSpec hash.
7. Public-readiness status is invalidated by changes to planner, schema semantics, path safety, disclosure or audit behavior until affected tests rerun.

## Next Compatibility Milestone

Target: `0.3.0a1`

Required:

```text
actual JSON Schema validation and parity tests;
reviewed SeedSpec contract;
target snapshot and content-aware planning;
canonical .repokernel audit profile;
clean-environment wheel/CLI proof;
version-locked private pilot;
review-cycle ledger and independent pilot evaluation.
```

Track A status:

```text
implemented locally and awaiting GPT Pro/operator readback;
hosted CI, private pilot execution and independent pilot evaluation remain
required before 0.3.0a1.
```
