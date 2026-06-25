# Source Atlas

| Path | Type | Role |
| --- | --- | --- |
| `README.md` | public surface | First-level definition and current positioning |
| `CURRENT_STATE.md` | project state | Active surface, boundaries, verified state and next move |
| `process/FIRST_PACKET.md` | active packet | Core and pilot completion gate |
| `process/reports/REPOKERNEL_FULL_SURFACE_AND_PILOT_REVIEW_2026-06-25.md` | independent review | Full current core/pilot findings and dual conformance resultant |
| `packets/FOR_CODEX/REPOKERNEL_CORE_AND_PILOT_COMPLETION_PACKET_2026-06-25.md` | active implementation packet | Track A core conformance and Track B private pilot qualification |
| `docs/guides/evolution-versioning-and-review-loop.md` | governance | GPT Pro–Codex–operator review lifecycle and artifact provenance |
| `docs/compatibility-matrix.md` | compatibility | Package, contract, source and evidence compatibility state |
| `process/reviews/REVIEW_LEDGER.md` | review index | Review-cycle lineage, implementation and closure status |
| `process/reviews/RK-RVW-20260625-01/CODEX_RETURN.md` | implementation return | Track A Codex readback, command evidence and remaining blockers |
| `process/reports/current-tree.json` | inventory report | Generated tracked-file inventory |
| `process/reports/migration-classification.json` | inventory report | Generated migration classification and unclassified count |
| `process/reports/link-check.json` | link report | Generated internal Markdown link check |
| `process/reports/phase0-validation-summary.md` | historical report | Phase 0 validation result and earlier blockers |
| `docs/recovery-procedure.md` | recovery | Minimal non-stale reentry through state, packet and atlas |
| `packets/FOR_CODEX/REPOKERNEL_FINAL_IMPLEMENTATION_PACKAGE_2026-06-23.md` | historical implementation index | Earlier phased architecture entry point |
| `packets/FOR_GPT_PRO/REPOKERNEL_NEUTRAL_REVIEW_REQUEST_2026-06-25.md` | review request | Neutral independent review request that led to the current cycle |
| `packets/FOR_GPT_PRO/REPOKERNEL_PHASE1_GPT_PRO_INDEPENDENT_REVIEW_2026-06-24.md` | prior review | Earlier Phase 1 independent review and P0 findings |
| `packets/FOR_CODEX/PHASE1_P0_HARDENING_PACKET_2026-06-24.md` | prior active packet | Earlier P0 hardening plan, superseded by the dual completion packet after acceptance |
| `packets/FOR_CODEX/GPT_PRO_REPOKERNEL_FINAL_ARCHITECTURE_AND_CODEX_PACKET_2026-06-23.md` | architecture | Final ontology, installed surface and contracts |
| `packets/FOR_CODEX/GPT_PRO_REPOKERNEL_FINAL_ARCHITECTURE_APPENDIX_2026-06-23.md` | architecture | Migration, phases, tests and decision capsule |
| `docs/distribution-model.md` | architecture | Compiler, Reference Seeds, application modes and Project Kernel |
| `docs/seed-synthesis-pipeline.md` | architecture | Intent and document assimilation pipeline |
| `docs/retrofit-model.md` | architecture | Existing-repository integration and namespace strategy |
| `docs/readiness-levels.md` | policy | L0-L3 evidence model |
| `docs/runtime-adapters.md` | adapter contract | Host-neutral runtime mappings |
| `docs/internal-runtime-architecture.md` | optional architecture | L3 execution body and event direction, not current implementation authority |
| `docs/recursive-distillation-plane.md` | cognitive architecture | Bounded D0-D3 improvement operator |
| `docs/autopoietic-cycle-gap-analysis.md` | gap analysis | Closed-loop gaps, separation of duties and A1 target |
| `docs/departmental-autonomy-spectral-analysis.md` | topology analysis | Two governance planes, bounded departments and entropy controls |
| `docs/possibility-horizon.md` | strategic horizon | Bidirectional and multi-target possibilities without current authority |
| `docs/pi-reference.md` | external reference | Transferable Pi patterns without dependency |
| `docs/claim-boundaries.md` | boundary | Public claim limits |
| `docs/feedback.md` | feedback | Privacy-safe feedback request for users and coders |
| `docs/guides/operational-procedure.md` | procedure | Current no-write validate/inspect/plan/stage/guides/audit path |
| `docs/guides/cli-reference.md` | guide | Current Phase 1 CLI surface |
| `docs/skill-repo-lifecycle.md` | method | Skill lifecycle routing |
| `skills/repokernel-semantic-kernel/SKILL.md` | skill | Local repository kernel |
| `skills/project-seed-synthesizer/SKILL.md` | meta-skill | Project-specific SeedSpec synthesis |
| `skills/recursive-improvement-distiller/SKILL.md` | meta-skill | Source ascent, possibility expansion and ResultantPacket distillation |
| `skills/autopoietic-cycle-controller/SKILL.md` | meta-skill | Governed observe-align-distill-evaluate cycle contract |
| `registry/skills.json` | registry | Skill state and evidence |
| `src/repokernel/` | Phase 1 core | Canonical serialization, validation, planning, staging, audit and CLI |
| `src/repokernel/schema_validation.py` | contract validation | Draft 2020-12 JSON Schema execution surface |
| `src/repokernel/snapshot.py` | target snapshot | Read-only content-aware target snapshot generation |
| `schemas/` | contract schemas | Current draft JSON Schema surfaces |
| `schemas/target-snapshot.schema.json` | contract schema | TargetSnapshot contract |
| `tests/unit/` | validation | Current repository-contained unit tests |
| `tests/unit/test_schema_validator_parity.py` | validation | Python validator and JSON Schema parity tests |
| `tests/unit/test_snapshot.py` | validation | TargetSnapshot behavior tests |
| `tests/unit/test_verify_dist.py` | validation | Reference Seed distribution verification test |
| `examples/minimal/` | fixture | Minimal validate/plan/stage/guides example |
| `specs/reference/starter-l1.seed.json` | reference seed | Minimal L1 Reference Seed spec with distribution hashes |
| `dist/reference/starter-l1/` | generated distribution | Starter L1 Reference Seed distribution |
| `process/evidence/LOCAL_VALIDATION.md` | local evidence | Repository-contained local validation; not hosted CI evidence |
| `process/reports/a1-local-no-write-proof-2026-06-24.md` | proof report | Synthetic local A1 no-write proof |
| `process/reports/distribution-readiness-2026-06-25.md` | readiness report | Current private-pilot-first verdict |
| `scripts/repokernel_core.py` | compatibility prototype | Earlier L0-L3 generation prototype pending parity/migration |
| `scripts/audit_repokernel_project.py` | compatibility wrapper | Wrapper around current audit implementation |
| `scripts/phase0_inventory.py` | inventory tool | Generates current-tree, migration and link reports |
| `packets/FOR_CODEX/V03_INTEGRATION.md` | superseded packet | Historical v0.3 plan; archive/delete after lineage preservation |
| `packets/FOR_CODEX/V04_PROJECT_SEED_SYNTHESIS.md` | superseded packet | Historical v0.4 plan; archive/delete after lineage preservation |

## Private Pilot

```text
repository: GrazianoGuiducci/denis-repokernel-pilot
run: RK-PILOT-20260625-01
role: private version-locked existing-repository no-write fixture
boundary: no Denis-owned external repository is part of the current test
```
