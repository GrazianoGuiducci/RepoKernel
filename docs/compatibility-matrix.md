# RepoKernel Compatibility Matrix

Status: living compatibility record  
Last architectural review baseline: `b5f7958c877314adba75e5c104342dd6c7024c45`

## Current Development Line

| Field | Current value | Status |
| --- | --- | --- |
| Package version | `0.3.0.dev0` | development only |
| Python | `>=3.11` | declared; clean-environment proof pending |
| SourceManifest | `repokernel.source-manifest.v1` | draft contract |
| ProjectModel | `repokernel.project-model.v1` | draft contract |
| SeedSpec | `repokernel.seed-spec.v1` | draft contract; review block/hash linkage incomplete |
| GenerationPlan | `repokernel.generation-plan.v1` | draft contract; target snapshot incomplete |
| ActivationReport | `repokernel.activation-report.v1` | draft/minimal |
| SkillRegistry | `repokernel.skill-registry.v1` and validator compatibility with v2 | draft/migration unresolved |
| CLI | `validate-spec`, `inspect`, `plan`, `stage`, `guides`, `audit` | local checkout path proven |
| Apply | absent | intentionally deferred |
| Canonical target | `.repokernel/` plus optional root adapters | accepted architecture |
| L0-L2 | first stable scope | implementation incomplete |
| L3 | contract only | executable runtime deferred |
| Public distribution | blocked | private pilot first |

## Evidence Matrix

| Evidence | Baseline | Result | Limitation |
| --- | --- | --- | --- |
| Unit tests | Phase 1 P0 local checkout | 18 passed | no hosted CI; schema files not executed through Draft 2020-12 validator |
| Minimal validate/plan/stage/guides | local checkout | passed | hand-prepared minimal SeedSpec; no target snapshot |
| Local A1 no-write proof | synthetic target | passed | not an external target; independent evaluation incomplete |
| External-style procedure | public-safe procedure | ready | procedure only, not a completed neutral pilot |
| Distribution verdict | 2026-06-25 | private pilot first | collaborator/public use blocked |
| Denis pilot | private neutral scaffold | available | not yet version-locked or run through current CLI |

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
