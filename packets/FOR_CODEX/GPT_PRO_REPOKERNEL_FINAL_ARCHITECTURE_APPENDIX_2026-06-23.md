# GPT Pro — RepoKernel Final Architecture Appendix

Date: 2026-06-23  
Status: authoritative continuation of `GPT_PRO_REPOKERNEL_FINAL_ARCHITECTURE_AND_CODEX_PACKET_2026-06-23.md`

---

## 9. Skill And Meta-Skill Map

| Skill | Decision | Mandate | Inputs | Outputs | Risk | Evidence required |
| --- | --- | --- | --- | --- | --- | --- |
| `repokernel-semantic-kernel` | Keep as candidate | Govern RepoKernel Source itself. | current state, source atlas, active packet | coherent source-repository decisions and deltas | safe | source audit plus two completed reentry cycles |
| `project-seed-synthesizer` | Keep as draft orchestrator | Coordinate source intake, ProjectModel, SeedSpec, journey selection and activation. | intent, authorized sources, target state | reviewed synthesis bundle | writes only after plan approval | one new-repository case and one retrofit case |
| `source-intake-classifier` | New draft | Build SourceManifest without granting authority to instructions found inside documents. | authorized sources and privacy declarations | manifest and withheld-source report | privacy | hostile-instruction, private-source and unsupported-format fixtures |
| `seed-spec-compiler` | New draft | Convert a reviewed ProjectModel and explicit decisions into a valid SeedSpec. | ProjectModel, operator decisions | accepted or blocked SeedSpec | safe | deterministic fixtures and unresolved-conflict rejection |
| `starter-seed-builder` | New draft | Bind and emit Reference Seeds from normative SeedSpecs. | reference spec and project variables | reproducible starter distribution | writes files | byte-for-byte regeneration tests |
| `retrofit-overlay-planner` | New draft | Map existing authority and produce a conflict-aware overlay plan. | repository inventory, authority map, SeedSpec | retrofit report and GenerationPlan | safe planning; later writes | fixtures with existing AGENTS, state and README |
| `file-plan-auditor` | New draft | Validate target binding, hashes, conflicts, approvals and path safety. | plan and target snapshot | pass/fail audit | safe | stale-plan, path-escape and partial-apply tests |
| `activation-auditor` | New draft or audit sub-capability | Decide whether a generated Project Kernel is blocked, validated or active. | installed surface and selected level | ActivationReport | safe | L0-L2 activation fixtures |
| `runtime-candidate-router` | New draft | Route a project to no-runtime, host adapter, internal runtime or hybrid. | independence needs, host limits and risks | route and validation plan | runtime | two justified runtime routes and one explicit rejection |
| `memory-delta-writer` | Keep draft | Preserve the smallest durable verified project change. | verified result and previous state | delta | writes files | three reentry/readback tests |
| `skill-lifecycle-auditor` | Keep draft | Classify skill maturity from actual evidence. | skill folder, registry and evidence | lifecycle report | safe | overclaim and underclaim fixtures |
| `skill-promotion-router` | Keep draft | Route a proven capability to local, public, Seed, private or residue. | normalized evidence packet | promotion decision | safe | accepted and rejected promotion examples |
| `create-repokernel-project` | Deprecate as public skill | Preserve only as a compatibility wrapper during migration. | name and mission | legacy scaffold | writes files | replacement parity test before removal |
| `create-skill-repo` | Move to future `skill-repo` Domain Pack | Specialize RepoKernel for repository-shaped skills. | SeedSpec plus domain pack | skill-repository seed | writes files | domain-pack reproducibility test |

No skill becomes `candidate` merely because its `SKILL.md` exists. Candidate status requires a resolvable example, validation result and current limitations.

---

## 10. Final Repository Structures

### 10.1 RepoKernel Source target

```text
RepoKernel/
  README.md
  LICENSE
  AGENTS.md                       # source-repository host adapter
  CURRENT_STATE.md                # temporary compatibility surface
  pyproject.toml

  .repokernel/                    # self-hosted canonical control plane
    manifest.json
    state/current.md
    packets/active.md
    sources/manifest.json
    sources/atlas.md
    spec/seed.spec.json
    reports/activation.json

  src/repokernel/
    __init__.py
    cli.py
    canonical.py
    models.py
    paths.py
    intake.py
    project_model.py
    seed_spec.py
    planner.py
    emitter.py
    inventory.py
    retrofit.py
    apply.py
    rollback.py
    activation.py
    audit.py
    adapters/

  schemas/
    source-manifest.v1.schema.json
    project-model.v1.schema.json
    seed-spec.v1.schema.json
    generation-plan.v1.schema.json
    retrofit-report.v1.schema.json
    activation-report.v1.schema.json
    skill-registry.v1.schema.json
    runtime.v1.schema.json

  specs/reference/
    starter-l0.seed.json
    starter-l1.seed.json
    starter-l2.seed.json

  dist/reference/                 # generated output; never edited manually
    starter-l0/
    starter-l1/
    starter-l2/

  adapters/
    codex/
    claude-code/
    opencode/
    chat-project/
    generic/

  domain-packs/
    registry.json

  skills/
  registry/
  docs/
  examples/
  tests/
    unit/
    integration/
    fixtures/
  packets/
    FOR_CODEX/
    FOR_GPT_PRO/
    archive/
  process/
  scripts/                        # temporary compatibility wrappers
```

### 10.2 Generated L1 Project Kernel

```text
project/
  AGENTS.md                       # optional generated host adapter
  README.md                       # existing or user-owned; never auto-overwritten

  .repokernel/
    manifest.json
    state/current.md
    sources/manifest.json
    sources/atlas.md
    model/project.model.json
    spec/seed.spec.json
    packets/active.md
    skills/<project-id>-kernel/SKILL.md
    reports/activation.json
    plans/last-applied.json
    adapters/registry.json
```

L0 is a subset. L2 adds `registry/`, `evidence/`, `deltas/` and `proposals/`. L3 adds only `runtime/manifest.json` in the first stable line.

---

## 11. Migration From Current Main

Codex must first produce a recursive tracked-file inventory and fail Phase 0 if any discovered path is not classified below or in the generated migration report.

### 11.1 Root

| Path | Action | Reason |
| --- | --- | --- |
| `README.md` | modify | Align with final namespace, journeys and stable-release scope. |
| `LICENSE` | keep | MIT decision is active. |
| `AGENTS.md` | modify | Make it the source-repository adapter to the self-hosted `.repokernel/` plane. |
| `CURRENT_STATE.md` | modify, later adapter/deprecate | Move authoritative state to `.repokernel/state/current.md`; retain compatibility during one release. |
| `repokernel.json` | replace/migrate | Canonical manifest becomes `.repokernel/manifest.json`; preserve a temporary pointer if required. |

### 11.2 Documentation

| Path | Action |
| --- | --- |
| `docs/distribution-model.md` | keep and normalize terminology |
| `docs/seed-synthesis-pipeline.md` | keep; add explicit semantic-reasoning versus deterministic-emission boundary |
| `docs/retrofit-model.md` | rename to `docs/existing-repository-integration.md` after references migrate |
| `docs/readiness-levels.md` | modify for canonical `.repokernel/` surfaces and L3 contract-only decision |
| `docs/runtime-adapters.md` | keep and expand adapter output contracts |
| `docs/internal-runtime-architecture.md` | keep as RFC/roadmap, not shipped executable-runtime claim |
| `docs/pi-reference.md` | keep; pin reviewed source revision when adapter work begins |
| `docs/claim-boundaries.md` | keep |
| `docs/skill-repo-lifecycle.md` | keep; align maturity evidence with registry schema |
| `docs/repokernel-promotion-rules.md` | keep; align with Promotion Packet contract |
| `docs/codex-operating-guide.md` | replace after CLI implementation |
| `docs/quickstart.md` | replace with Direct, Synthesis and Retrofit journeys |
| `docs/concept.md` | merge durable concepts into distribution model, then reduce or deprecate |
| `docs/context-surface.md` | replace; incomplete content must not remain canonical |

### 11.3 Templates and distributions

| Paths | Action |
| --- | --- |
| `templates/AGENTS.template.md` | move into compiler adapter templates |
| `templates/CURRENT_STATE.template.md` | replace with canonical state template; root state becomes optional adapter |
| `templates/FIRST_PACKET.template.md` | move into canonical packet templates |
| `templates/MEMORY_DELTA.template.md` | keep and move into L2 templates |
| `templates/SOURCE_ATLAS.template.md` | replace with SourceManifest and atlas templates |
| `templates/SKILL_REPO.template.md` | move to future `skill-repo` Domain Pack |
| `templates/META_SKILL.template.md` | keep as source-authoring aid, not installed core |
| `dist/reference/*` | generate; never hand-author |

### 11.4 Skills

Apply Section 9. Record deprecation and supersession in the registry before deleting or moving any skill.

### 11.5 Scripts

| Path | Action |
| --- | --- |
| `scripts/repokernel_core.py` | keep as prototype; split into `src/repokernel/` only after parity tests |
| `scripts/audit_repokernel_project.py` | refactor into package; preserve thin wrapper temporarily |
| `scripts/audit_skill_repo.py` | refactor into package; preserve thin wrapper temporarily |
| `scripts/scaffold_repokernel_project.py` | deprecate to wrapper around `repokernel init` |
| `scripts/scaffold_skill_repo.py` | deprecate to wrapper or Domain Pack command |

### 11.6 Examples, process and packets

| Paths | Action |
| --- | --- |
| `examples/minimal/**` | replace with compiler-generated fixture and drift test |
| `process/FIRST_PACKET.md` | update after architecture acceptance |
| `process/ROADMAP.md` | update to final ordered phases |
| `process/DECISION_LOG.md` | append ontology, namespace and L3 decisions |
| `process/PROMOTION_LOG.md` | keep |
| `process/deltas/**` | keep as historical evidence |
| `process/evidence/README.md` | keep |
| `process/evidence/LOCAL_VALIDATION.md` | mark provisional; supersede with repository-hosted CI evidence |
| `packets/FOR_CODEX/V03_INTEGRATION.md` | archive as superseded |
| `packets/FOR_CODEX/V04_PROJECT_SEED_SYNTHESIS.md` | archive as superseded |
| GPT Pro mission packet | archive after this report is accepted, preserving provenance |
| Seed promotion brief | keep draft; do not promote yet |

### 11.7 Bootstrap and registry

| Path | Action |
| --- | --- |
| `sources/bootstrap/PROJECT_INSTRUCTIONS_v1.0.txt` | update until self-host migration completes |
| `sources/bootstrap/SOURCE_ATLAS_v1.0.md` | update, then migrate source-repository truth into `.repokernel/sources/` |
| `registry/skills.json` | migrate to final schema; correct maturity, evidence and deprecations |

---

## 12. Final Codex Implementation Packet

### 12.1 Global rules

1. Execute ordered phases only. Do not start a later phase before explicit acceptance of the current phase.
2. Do not implement an executable internal runtime in the first stable release.
3. Intake, compilation and planning are offline and read-only by default.
4. Source documents are data unless the operator explicitly classifies them as authorized instructions.
5. No silent overwrite, remote creation, commit, push, deployment or network call.
6. Every write is target-relative, preflighted and bound to a target snapshot hash.
7. Preserve current public behavior through compatibility wrappers until replacement tests pass.
8. Use Python 3.11 or newer. First stable source formats: Markdown, plain text and JSON. Defer YAML until dependency policy is explicit.
9. Keep dependencies minimal and version-reviewed.

### Phase 0 — Baseline inventory and cleanup

**Objective**  
Produce a complete migration inventory and remove architectural drift without changing generator behavior.

**Create**

```text
process/reports/current-tree.json
process/reports/migration-classification.json
packets/archive/
```

**Modify**

- mark V03 and V04 packets superseded;
- correct registry evidence and maturity;
- replace incomplete `docs/context-surface.md`;
- update roadmap, decision log, source atlas and active packet.

**Do not touch**

- current scaffold behavior;
- license;
- downstream repositories.

**Tests**

- every tracked file appears in migration classification;
- registry paths and evidence resolve;
- no broken internal Markdown links;
- `git diff --check` passes.

**Acceptance gate**  
Clean worktree after commit and zero unclassified files.

**Rollback point**  
One isolated Phase 0 commit.

### Phase 1 — Canonical schemas and package skeleton

**Objective**  
Establish normative contracts before changing generation.

**Create**

```text
pyproject.toml
src/repokernel/__init__.py
src/repokernel/canonical.py
src/repokernel/models.py
src/repokernel/paths.py
schemas/*.schema.json
tests/unit/test_schemas.py
tests/unit/test_canonical.py
```

**Implement**

- canonical JSON serialization;
- normalized UTF-8, newlines and path separators;
- SHA-256 hashing;
- path traversal rejection;
- schema-version dispatch.

**Acceptance gate**  
All v1 schemas validate good fixtures and reject malformed fixtures. Identical logical input has identical canonical hash.

### Phase 2 — Deterministic planner/emitter and Reference Seeds

**Objective**  
Ship the smallest stable direct-start product.

**Create**

```text
src/repokernel/seed_spec.py
src/repokernel/planner.py
src/repokernel/emitter.py
src/repokernel/activation.py
src/repokernel/cli.py
specs/reference/starter-l0.seed.json
specs/reference/starter-l1.seed.json
specs/reference/starter-l2.seed.json
dist/reference/**
tests/integration/test_reference_seeds.py
```

**Commands**

```bash
python -m repokernel init --starter l1 --target <path> --dry-run
python -m repokernel verify-dist
python -m repokernel audit <path>
```

**Rules**

- `.repokernel/` is canonical;
- root adapters are generated selectively;
- README is never overwritten;
- no partial write occurs when conflicts exist;
- distributions are generated only.

**Acceptance gate**  
L0, L1 and L2 Reference Seeds rebuild byte-for-byte and direct init activates each expected level.

### Phase 3 — Source intake, ProjectModel and synthesis

**Objective**  
Support custom intent/document synthesis while preserving the semantic/deterministic boundary.

**Create**

```text
src/repokernel/intake.py
src/repokernel/project_model.py
src/repokernel/compiler.py
skills/source-intake-classifier/SKILL.md
skills/seed-spec-compiler/SKILL.md
tests/fixtures/synthesis/**
tests/integration/test_synthesis.py
```

**Commands**

```bash
python -m repokernel intake --intent <file> --source <file> --output <build-dir>
python -m repokernel validate-model <project.model.json>
python -m repokernel compile --model <project.model.json> --output <seed.spec.json>
```

The package need not call an LLM. GPT, Codex or another reasoner uses the meta-skill to produce an evidence-bearing ProjectModel; the CLI validates provenance and compiles an accepted SeedSpec.

**Acceptance gate**  
Conflicts, unknowns, privacy and embedded document instructions survive intake correctly. Accepted SeedSpec compilation is reproducible.

### Phase 4 — Existing repository inventory, retrofit and safe apply

**Objective**  
Integrate without replacing project canon.

**Create**

```text
src/repokernel/inventory.py
src/repokernel/retrofit.py
src/repokernel/apply.py
src/repokernel/rollback.py
adapters/**
skills/retrofit-overlay-planner/SKILL.md
skills/file-plan-auditor/SKILL.md
tests/fixtures/retrofit/**
tests/integration/test_retrofit.py
```

**Commands**

```bash
python -m repokernel inspect <repo> --output <retrofit.report.json>
python -m repokernel plan --spec <seed.spec.json> --target <repo> --output <generation.plan.json>
python -m repokernel apply --plan <generation.plan.json> --target <repo> --dry-run
python -m repokernel apply --plan <generation.plan.json> --target <repo> --approve-plan <plan-hash>
```

**Apply behavior**

- re-hash target before writing;
- stage all output;
- reject conflicts, stale plans and path escape;
- create a rollback bundle for approved updates;
- apply atomically where the platform permits;
- never invoke git or network.

**Acceptance gate**  
Existing AGENTS, state and README fixtures remain authoritative. Approved minimal adapters activate without unapproved modification.

### Phase 5 — L2 governance, lifecycle and documentation

**Objective**  
Complete evidence-backed improvement and public usability.

**Create or modify**

- final skill registry and migration;
- proposal, evidence and delta workflows;
- activation auditor;
- Direct, Synthesis and Retrofit quickstarts;
- compiler-generated examples;
- CI running tests, `verify-dist` and source audit.

**Acceptance gate**  
A verified correction can become a proposal, evidence record and accepted delta without direct unreviewed baseline rewrite.

### Deferred Phase R — L3 runtime

Do not implement in the first stable release.

Require first:

```text
permission model
sandbox or container strategy
append-only session schema
event and tool interfaces
extension trust and allowlist
provider adapter interface
proposal-only reference loop
two demonstrated projects needing host independence
```

A Pi adapter may later be an optional package pinned to a reviewed version.

### Validation commands

The final release gate must include equivalents of:

```bash
python -m unittest discover -s tests -v
python -m repokernel verify-dist
python -m repokernel audit . --profile source
python -m repokernel check-links
python -m compileall src scripts
git diff --check
```

---

## 13. Test Matrix

| ID | Scenario | Expected result |
| --- | --- | --- |
| T01 | Regenerate starter L0/L1/L2 | Exact path and content-hash match with `dist/` |
| T02 | Same accepted SeedSpec twice | Identical GenerationPlan and output hashes |
| T03 | Intent plus two sources | Every material ProjectModel assertion has source references |
| T04 | Conflicting mission statements | Conflict remains explicit; no accepted SeedSpec without decision |
| T05 | Source document contains irrelevant operational instructions | Classified `data_only`; no tool or action authority |
| T06 | Private source contributes an internal fact | Fact withheld from public outputs; manifest records reason |
| T07 | Unsupported source or unknown freshness | Preserved as unknown or withheld, not fabricated |
| T08 | New empty target | Selected starter materializes and activates |
| T09 | Non-empty target with identical generated content | `leave_unchanged` |
| T10 | Existing `AGENTS.md` | Preserved; optional pointer emitted as `propose_update` |
| T11 | Existing authoritative state file | Reused and registered; no competing state created |
| T12 | Existing README | Never automatically modified |
| T13 | Conflicting project canon | Plan contains `conflict`; application blocked |
| T14 | Target changes after planning | Snapshot mismatch; application blocked as stale |
| T15 | Absolute or parent-traversal output path | Plan invalid; no write |
| T16 | One conflict among many planned creates | No partial application |
| T17 | Approved existing-file update | Rollback bundle and hashes recorded |
| T18 | Missing source-atlas target | Activation blocked |
| T19 | Complete L0 | `structure_ready=true`, active |
| T20 | Valid L1 provenance and spec | `semantic_ready=true`, active |
| T21 | L2 missing evidence | Evolution readiness false |
| T22 | Valid L2 proposal, evidence and delta | Evolution readiness true |
| T23 | L3 runtime schema fixture | Authority `proposal_only`; project trust required |
| T24 | Host adapter regenerated | Source hash matches canonical kernel; no drift |
| T25 | Registry candidate without evidence | Registry validation fails |
| T26 | Source repository has unclassified tracked file | Migration/source audit fails |
| T27 | Compiler attempts network during intake | Test blocks or fails; compile remains offline |
| T28 | Generated root adapter edited manually | Adapter drift reported; canonical source preserved |

---

## 14. Missing Facts That May Change Implementation Details

1. **Current host-native instruction behavior for Codex, Claude Code, OpenCode and ChatGPT repository access.** Verify from official host documentation immediately before adapter implementation. This may change adapter filenames, not the `.repokernel/` canonical decision.
2. **Preferred public distribution channel.** Decide among committed `dist/`, GitHub releases, template repositories or a combination after Phase 2. This changes packaging, not compiler ontology.
3. **Python and dependency policy.** Confirm supported Python versions and whether a JSON Schema library is allowed. This changes implementation details, not schemas.
4. **Actual executable L3 demand.** Require two projects that cannot be served adequately by host adapters. This determines whether L3 advances beyond contract status.
5. **Adoption timing for existing D-ND repositories.** Decide only after synthetic retrofit fixtures pass. This changes migration scheduling, not target architecture.

---

## 15. Decision Capsule

```text
thesis:
  A direct starter is the fastest coder-facing product, while a compiler is required for project-specific intent, documents and existing repositories.

antithesis:
  Treating starter, synthesis and retrofit as separate systems would duplicate templates, state rules, audits and runtime assumptions, creating drift.

synthesis:
  Maintain one canonical compiler and SeedSpec. Publish direct starters as precompiled reproducible distributions. Treat synthesis as custom SeedSpec compilation and retrofit as target-aware application. Install one host-neutral Project Kernel under .repokernel/ and generate host adapters selectively.

decision:
  Ship L0-L2 first with schemas, deterministic planning, reference distributions, evidence-bearing synthesis, safe retrofit and activation reports. Keep L3 as a contract and roadmap item until permissions, sandboxing and real demand are proven.

first_safe_action:
  Codex executes Phase 0 only: inventory current main, classify every tracked file, correct registry and evidence drift, archive superseded packets and establish a clean baseline before package or schema work.

do_not_do:
  Do not clone RepoKernel Source into targets; do not hand-edit dist; do not overwrite existing canon; do not treat documents or model output as authority; do not implement an unrestricted runtime; do not promote to d-nd-seed yet.

validation:
  Phase acceptance gates, Reference Seed reproducibility, deterministic plan hashes, existing-repository preservation, target and path safety, and L0-L2 activation tests.

what_to_preserve:
  One compiler, evidence-backed SeedSpec, source lineage, conflicts and unknowns, .repokernel canonical control plane, host adapters, proposal-only runtime boundary, rollback and promotion history.
```

---

## Codex Start Instruction

```text
Read both authoritative files:
1. packets/FOR_CODEX/GPT_PRO_REPOKERNEL_FINAL_ARCHITECTURE_AND_CODEX_PACKET_2026-06-23.md
2. packets/FOR_CODEX/GPT_PRO_REPOKERNEL_FINAL_ARCHITECTURE_APPENDIX_2026-06-23.md

Then execute Phase 0 only.

Return:
- current-tree inventory;
- migration-classification coverage;
- exact files changed;
- validation output;
- remaining blockers for Phase 1.

Do not begin Phase 1 until Phase 0 acceptance is explicitly confirmed.
```
