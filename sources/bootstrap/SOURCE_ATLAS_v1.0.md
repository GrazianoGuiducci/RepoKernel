# Source Atlas

| Path | Type | Role |
| --- | --- | --- |
| `README.md` | public surface | First-level definition and current positioning |
| `CURRENT_STATE.md` | project state | Active surface, boundaries, verified state and next move |
| `process/FIRST_PACKET.md` | active packet | Track A readback correction gate |
| `process/reviews/RK-RVW-20260625-01/CODEX_RETURN.md` | implementation return | Track A implementation, local evidence and deviations |
| `process/reviews/RK-RVW-20260625-01/CODEX_RETURN_CORRECTION.md` | correction return | Track A correction implementation, tests and remaining blockers |
| `process/reviews/RK-RVW-20260625-01/GPT_PRO_READBACK.md` | independent readback | Static review result: pass with required corrections; Track B blocked |
| `packets/FOR_CODEX/TRACK_A_READBACK_CORRECTIONS_2026-06-25.md` | active implementation packet | Bounded Track A corrections before any future fixture decision |
| `process/reports/REPOKERNEL_FULL_SURFACE_AND_PILOT_REVIEW_2026-06-25.md` | prior independent review | Full core/pilot findings and dual conformance resultant |
| `packets/FOR_CODEX/REPOKERNEL_CORE_AND_PILOT_COMPLETION_PACKET_2026-06-25.md` | prior implementation packet | Original Track A and Track B completion scope |
| `docs/guides/evolution-versioning-and-review-loop.md` | governance | GPT Pro–Codex–operator review lifecycle and artifact provenance |
| `docs/compatibility-matrix.md` | compatibility | Package, contract, source and evidence compatibility state |
| `process/reviews/REVIEW_LEDGER.md` | review index | Review-cycle lineage, corrections and closure status |
| `process/reports/current-tree.json` | inventory report | Generated tracked-file inventory |
| `process/reports/migration-classification.json` | inventory report | Generated migration classification and unclassified count |
| `process/reports/link-check.json` | link report | Generated internal Markdown link check |
| `process/reports/phase0-validation-summary.md` | historical report | Phase 0 validation result and earlier blockers |
| `docs/recovery-procedure.md` | recovery | Minimal non-stale reentry through state, packet and atlas |
| `packets/FOR_CODEX/REPOKERNEL_FINAL_IMPLEMENTATION_PACKAGE_2026-06-23.md` | historical implementation index | Earlier phased architecture entry point |
| `packets/FOR_GPT_PRO/REPOKERNEL_NEUTRAL_REVIEW_REQUEST_2026-06-25.md` | review request | Neutral independent review request that led to the current cycle |
| `packets/FOR_GPT_PRO/REPOKERNEL_PHASE1_GPT_PRO_INDEPENDENT_REVIEW_2026-06-24.md` | prior review | Earlier Phase 1 independent review and P0 findings |
| `packets/FOR_CODEX/PHASE1_P0_HARDENING_PACKET_2026-06-24.md` | prior packet | Earlier P0 hardening plan |
| `packets/FOR_CODEX/GPT_PRO_REPOKERNEL_FINAL_ARCHITECTURE_AND_CODEX_PACKET_2026-06-23.md` | architecture | Final ontology, installed surface and contracts |
| `packets/FOR_CODEX/GPT_PRO_REPOKERNEL_FINAL_ARCHITECTURE_APPENDIX_2026-06-23.md` | architecture | Migration, phases, tests and decision capsule |
| `docs/distribution-model.md` | architecture | Compiler, Reference Seeds, application modes and Project Kernel |
| `docs/seed-synthesis-pipeline.md` | architecture | Intent and document assimilation pipeline |
| `docs/retrofit-model.md` | architecture | Existing-repository integration and namespace strategy |
| `docs/readiness-levels.md` | policy | L0-L3 evidence model |
| `docs/runtime-adapters.md` | adapter contract | Host-neutral runtime mappings |
| `docs/internal-runtime-architecture.md` | optional architecture | L3 execution body and event direction, not current authority |
| `docs/recursive-distillation-plane.md` | cognitive architecture | Bounded D0-D3 improvement operator |
| `docs/autopoietic-cycle-gap-analysis.md` | gap analysis | Closed-loop gaps, separation of duties and A1 target |
| `docs/departmental-autonomy-spectral-analysis.md` | topology analysis | Bounded departments and entropy controls |
| `docs/possibility-horizon.md` | strategic horizon | Bidirectional and multi-target possibilities without current authority |
| `docs/pi-reference.md` | external reference | Transferable Pi patterns without dependency |
| `docs/claim-boundaries.md` | boundary | Public claim limits |
| `docs/feedback.md` | feedback | Privacy-safe feedback request |
| `docs/guides/operational-procedure.md` | procedure | Current no-write product path |
| `docs/guides/cli-reference.md` | guide | Current CLI surface |
| `docs/skill-repo-lifecycle.md` | method | Skill lifecycle routing |
| `skills/repokernel-semantic-kernel/SKILL.md` | skill | Local repository kernel |
| `skills/project-seed-synthesizer/SKILL.md` | meta-skill | Project-specific SeedSpec synthesis |
| `skills/recursive-improvement-distiller/SKILL.md` | meta-skill | Source ascent and ResultantPacket distillation |
| `skills/autopoietic-cycle-controller/SKILL.md` | meta-skill | Governed observe-align-distill-evaluate cycle contract |
| `registry/skills.json` | registry | Skill state and evidence |
| `src/repokernel/` | Phase 1 core | Serialization, validation, planning, staging, audit and CLI |
| `src/repokernel/schema_validation.py` | contract validation | Draft 2020-12 execution surface |
| `src/repokernel/bundle.py` | bundle validation | SourceManifest, ProjectModel and SeedSpec linkage and provenance |
| `src/repokernel/snapshot.py` | target snapshot | Read-only snapshot, exclusion policy and integrity helpers |
| `src/repokernel/version.py` | package metadata | Runtime package version lookup for provenance |
| `schemas/` | contract schemas | Draft machine contracts with Track A correction constraints |
| `tests/unit/` | local validation | Repository-contained correction tests |
| `examples/minimal/` | fixture | Minimal product-path bundle example |
| `examples/minimal/project-model.json` | fixture | Evidence-bearing ProjectModel for bundle validation |
| `specs/reference/starter-l1.seed.json` | reference seed | Compiler-regenerated Starter L1 SeedSpec |
| `dist/reference/starter-l1/` | distribution artifact | Compiler-verifiable Starter L1 generated distribution |
| `process/evidence/LOCAL_VALIDATION.md` | local evidence | Repository-contained validation, not hosted CI |
| `process/reports/a1-local-no-write-proof-2026-06-24.md` | proof report | Synthetic A1 no-write proof |
| `process/reports/distribution-readiness-2026-06-25.md` | readiness report | Historical private-pilot-first verdict; superseded by current frozen-fixture boundary where inconsistent |
| `scripts/repokernel_core.py` | compatibility prototype | Earlier generation prototype pending migration |
| `scripts/audit_repokernel_project.py` | compatibility wrapper | Wrapper around audit implementation |
| `scripts/phase0_inventory.py` | inventory tool | Generates inventory and link reports |
| `packets/FOR_CODEX/V03_INTEGRATION.md` | superseded packet | Historical plan |
| `packets/FOR_CODEX/V04_PROJECT_SEED_SYNTHESIS.md` | superseded packet | Historical plan |

## Frozen Former Pilot Fixture

```text
repository: GrazianoGuiducci/denis-repokernel-pilot
run: RK-PILOT-20260625-01
status: frozen; not an active context; not a person/contact context
boundary: do not read, pull, execute, mutate, stage against or cite as active
unless the operator explicitly reauthorizes a neutral technical fixture later.
```
