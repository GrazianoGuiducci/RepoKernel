# GPT Pro — RepoKernel Final Architecture and Codex Packet

Date: 2026-06-23  
Status: final architecture decision / implementation authority packet  
Repository: `GrazianoGuiducci/RepoKernel`

---

## 1. Executive Verdict

RepoKernel should be one system, not a template product plus a separate generator.

Its canonical form is a **host-neutral project-kernel compiler**. It receives authorized intent, sources, existing project state and explicit operator decisions; it produces a reviewed `SeedSpec`; a deterministic toolchain then materializes or retrofits a project-local **Project Kernel**.

A direct starter is a precompiled, versioned `SeedSpec`, not a second architecture. A custom ProjectSeed is a project-specific `SeedSpec`. A Retrofit Overlay is the application plan for that same specification against an existing repository.

The canonical installed control plane should live under `.repokernel/`. Root and host-native files such as `AGENTS.md`, `.claude/` or equivalent instruction surfaces are generated adapters or registered existing authorities, not competing sources of truth.

The first stable release should ship L0-L2, deterministic planning/application, reference starters, source lineage, retrofit safety and activation audits. L3 should ship as schema and architecture only. An executable internal runtime should wait until permission, sandbox, session and extension-trust boundaries are proven separately.

GitHub remains the first carrier, not the identity of RepoKernel.

---

## 2. Final Ontology

### 2.1 Canonical objects

| Object | Definition | Canonical status | Producer | Consumer | Lifecycle | Not this |
| --- | --- | --- | --- | --- | --- | --- |
| **RepoKernel Source** | Mother repository containing schemas, compiler, planners, emitters, audits, meta-skills, reference specifications and tests. | Canonical source system | Maintainers and reviewed promotions | Coders and build pipeline | source → tested release → promoted capability | A folder copied wholesale into every project |
| **SourceManifest** | Inventory of authorized inputs with hashes, authority, privacy, freshness, permitted use and instruction-handling status. | Canonical compilation input | Source intake | ProjectModel compiler and audit | collected → reviewed → frozen per compile | A prompt or permission grant |
| **ProjectModel** | Evidence-bearing semantic model of identity, mission, product, users, invariants, conflicts, unknowns, boundaries, terminology and capabilities. | Canonical semantic intermediate | GPT/Codex or another reasoner following the synthesizer contract | SeedSpec compiler and human reviewer | draft → reviewed → superseded | Executable instructions or hidden reasoning |
| **SeedSpec** | Reviewed declarative build contract for one project kernel. | Primary canonical artifact | ProjectModel compiler plus explicit operator decisions | Deterministic planner/emitter | draft → reviewed → accepted → versioned | A generated tree or free-form prompt |
| **GenerationPlan** | Deterministic, target-bound plan classifying every path and recording before/after hashes, risks and approvals. | Canonical application artifact | Planner from SeedSpec plus target snapshot | Reviewer and apply engine | planned → approved → applied/rejected/stale | General external-action authority |
| **Project Kernel** | Validated local control plane materialized in the target project. | Canonical installed result | Emitter or retrofit apply engine | Project agents, adapters, audits | generated → validated → active → evolved/deprecated | RepoKernel Source itself |
| **ActivationReport** | Machine-readable proof that required surfaces, references, adapters and audits satisfy the selected level. | Canonical state-transition artifact | Audit/activation engine | Project operator and future reentry | blocked/planned → validated → active | Publication or deployment authority |

### 2.2 Distribution and application forms

| Object | Final interpretation |
| --- | --- |
| **Reference Seed / Starter Seed** | Precompiled `SeedSpec` plus generated files for a common starting condition. It must be reproducible by the current compiler. |
| **Synthesized ProjectSeed** | Project-specific `SeedSpec` and its planned materialization, compiled from authorized intent and sources. |
| **Retrofit Overlay** | A `GenerationPlan` produced by applying a SeedSpec to an existing target snapshot. It is an application mode, not a separate ontology. |
| **ProductGenesisPacket** | Retire as a canonical core term. Preserve only as an optional human-facing `IntentPacket` source ingested into the SourceManifest. |
| **Domain Pack** | Optional versioned bundle of schemas, extraction hints, capabilities, adapters and validation rules for one domain. It cannot override project authority or boundaries. |
| **Runtime Adapter** | Mapping from the Project Kernel contract to one host’s native instructions, tools, sessions or hooks. Generated and replaceable. |
| **Optional Internal Runtime** | L3 execution body around the Project Kernel. Separate from kernel identity and gated by trust, permissions and review. Contract now; implementation later. |
| **Promotion Packet** | Evidence-bearing proposal to move a proven local capability into RepoKernel Source, D-ND Seed or another registry. |

### 2.3 Invariant

```text
RepoKernel Source compiles SeedSpec.
SeedSpec materializes Project Kernel.
Reference Seeds are precompiled SeedSpecs.
Retrofit is an application mode.
Adapters pronounce one Project Kernel in different hosts.
```

---

## 3. Final Architecture

```text
AUTHORIZED INPUT FIELD
  operator intent
  selected documents
  existing repository state
  environment and privacy constraints
  explicit operator decisions
            |
            v
SOURCE INTAKE — read-only
  source.manifest.json
  hashes / authority / privacy / freshness / instruction handling
            |
            v
SEMANTIC ASSIMILATION — model-assisted, evidence-bearing
  project.model.json
  assertions + source references + status
  conflicts and unknowns preserved
            |
            v
REVIEW GATE
  operator corrects model and resolves required decisions
            |
            v
SEED COMPILATION
  seed.spec.json
  declarative, versioned, review status recorded
            |
            v
DETERMINISTIC PLANNING — no model reasoning
  target inventory + target snapshot hash
  generation.plan.json
  create / leave_unchanged / propose_update / conflict / withhold
            |
            v
APPLICATION GATE
  approve exact plan and exact target snapshot
            |
       +----+----+
       |         |
       v         v
 NEW REPO      RETROFIT
 materialize   stage reviewed overlay
       |         |
       +----+----+
            v
VALIDATION
  schema checks / source resolution / adapter checks / readiness audit
            |
            v
ACTIVATION REPORT
  blocked / validated / active
            |
            v
PROJECT KERNEL
  .repokernel/ canonical control plane + host adapters
            |
            v
OPERATING CYCLE
  orient -> act within boundary -> verify -> evidence -> delta
            |
            v
GOVERNED EVOLUTION
  proposal -> isolated test -> evidence -> review -> accepted SeedSpec delta
```

Semantic assimilation may use GPT, Codex or another model. Its outputs remain drafts until material assertions have provenance and the ProjectModel is reviewed.

After SeedSpec acceptance, planning and emission must be deterministic. A model may explain a plan but must not silently alter it during application.

```text
source content != operator instruction
model output != accepted project fact
plan approval != publish/deploy approval
runtime presence != action authority
```

---

## 4. Distribution Model

Create normative reference specifications:

```text
specs/reference/starter-l0.seed.json
specs/reference/starter-l1.seed.json
specs/reference/starter-l2.seed.json
```

Generate distributions only from these specs:

```text
dist/reference/starter-l0/
dist/reference/starter-l1/
dist/reference/starter-l2/
```

Each distribution records compiler version, SeedSpec hash and generated-tree hash. `dist/` is generated output and must not be hand-edited.

`verify-dist` regenerates every reference seed in a temporary directory and compares normalized paths and content hashes. CI fails when committed output differs.

The coder-facing direct path should be one command or one generated release bundle. Cloning a starter may be supported, but the canonical artifact remains compiler-produced.
