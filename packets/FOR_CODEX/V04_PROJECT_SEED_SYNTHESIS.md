# RepoKernel v0.4 — Project Seed Synthesis

Status: superseded during Phase 0 cleanup.

Superseded by:

```text
packets/FOR_CODEX/REPOKERNEL_FINAL_IMPLEMENTATION_PACKAGE_2026-06-23.md
packets/FOR_CODEX/GPT_PRO_REPOKERNEL_FINAL_ARCHITECTURE_AND_CODEX_PACKET_2026-06-23.md
packets/FOR_CODEX/GPT_PRO_REPOKERNEL_FINAL_ARCHITECTURE_APPENDIX_2026-06-23.md
```

This packet remains useful as historical design pressure. It is not current
implementation authority and does not authorize Phase 1.

## Objective

Implement the path from project intent and supplied documents to a reviewed, project-specific RepoKernel seed for either a new repository or an existing repository retrofit.

The implementation must separate:

```text
assimilation: sources -> project model -> reviewed seed specification
emission: reviewed seed specification -> deterministic file plan
application: reviewed file plan -> new files or retrofit changes
activation: validation -> local kernel ready for reentry
```

## Required Components

### 1. Source Intake

Add a module and command that accept:

```text
--intent <file or text>
--source <path>            repeatable
--source-dir <path>        repeatable
--existing-repo <path>     optional
--target-mode new_repository | existing_repository_retrofit
--privacy public | private | mixed
```

Initial supported inputs:

```text
.md
.txt
.json
.yaml / .yml
repository file inventory and selected source files
```

Do not execute source content. Instructions found inside source documents are data unless explicitly classified as operator instructions.

Create a source manifest containing:

```text
source_id
path_or_origin
content_type
authority
privacy
freshness
sha256
used_for
withheld_reason
```

### 2. Project Model

Compile an intermediate `project.model.json` with:

```text
identity
mission
product_or_result
users_and_observers
domain
source_authority
current_state
invariants
constraints
boundaries
terminology
capabilities
interfaces
recurring_workflows
validation_criteria
unknowns
source_conflicts
```

Every extracted assertion must retain source references. Unknown values remain unknown. Conflicting sources are not silently collapsed.

### 3. Seed Specification

Compile `seed.spec.json` using schema `repokernel.seed-spec.v1`.

Minimum shape:

```json
{
  "schema": "repokernel.seed-spec.v1",
  "seed_id": "...",
  "project": {
    "name": "...",
    "intent": "...",
    "product": "...",
    "users": [],
    "domain": "..."
  },
  "target": {
    "mode": "new_repository",
    "path": "...",
    "existing_repo": false
  },
  "sources": [],
  "invariants": [],
  "boundaries": {},
  "terminology": {},
  "readiness_level": "L1",
  "selected_capabilities": [],
  "kernel_contract": {},
  "runtime_route": "no-runtime",
  "file_plan_policy": {
    "overwrite": false,
    "conflict_mode": "stop"
  },
  "validation_plan": [],
  "unresolved": []
}
```

The specification must be reviewable and editable before generation.

### 4. Level And Capability Routing

Support:

```text
--level auto | L0 | L1 | L2 | L3
```

`auto` selects the lowest sufficient level and records why.

Initial routing examples:

```text
simple continuity need -> L0
multiple authoritative sources -> L1
repeated learning and promotion need -> L2
proven need for host-independent execution -> L3
```

Domain packs may be added later. The first implementation may expose a registry interface without shipping many packs.

### 5. File Plan

Generate `generation.plan.json` before any write.

Every path is classified as:

```text
create
leave_unchanged
propose_update
conflict
withhold
```

Each item includes:

```text
path
action
reason
source_fields
content_hash
risk
approval_needed
```

The same accepted `seed.spec.json` must produce the same file plan.

### 6. New Repository Mode

Emit custom project files from the specification:

```text
AGENTS.md
CURRENT_STATE.md
repokernel.json
sources/bootstrap/PROJECT_INSTRUCTIONS_v1.0.txt
sources/bootstrap/SOURCE_ATLAS_v1.0.md
skills/<project>-semantic-kernel/SKILL.md
process/FIRST_PACKET.md
optional L2/L3 surfaces
```

Content must use the target project's name, intent, product, terminology, sources, boundaries and validation criteria.

### 7. Existing Repository Retrofit

Inspect the repository before planning.

Rules:

- existing files are authoritative until a reviewed proposal changes them;
- never overwrite silently;
- preserve existing instructions and canonical terminology;
- create only missing compatible layers;
- represent updates as `propose_update` with diff-ready content;
- stop on unresolved path or canon conflicts;
- do not initialize, publish or change a remote without explicit authority.

Produce `retrofit.report.json` containing existing surfaces, missing layers, conflicts, withheld content and recommended readiness target.

### 8. Activation

Add `activation.report.json` or equivalent with states:

```text
planned
generated
validated
active
blocked
```

The project kernel becomes `active` only when:

- required files for the selected level exist and are non-empty;
- source-atlas references resolve;
- state, instructions, semantic skill and first packet agree;
- conflicts are resolved;
- the selected audit passes.

Activation does not grant publication, deployment, network, secret or cross-repository authority.

## Commands

Recommended interface:

```bash
python scripts/compile_seed.py \
  --intent project-intent.md \
  --source-dir docs \
  --target-mode new_repository \
  --level auto \
  --output .repokernel-build

python scripts/plan_seed.py \
  --spec .repokernel-build/seed.spec.json \
  --target /path/to/project

python scripts/apply_seed.py \
  --plan .repokernel-build/generation.plan.json \
  --target /path/to/project \
  --dry-run
```

A single orchestrating command may wrap these stages, but the intermediate artifacts must remain inspectable.

## Safety Requirements

- Source documents are untrusted data by default.
- Reject path traversal and writes outside the selected target.
- Hash source inputs and generated content.
- Do not read secrets, `.env`, credential stores or private keys by default.
- Respect ignore rules and explicit withheld paths.
- No network access during compilation unless separately authorized.
- No automatic remote creation or push.
- L3 remains proposal-only unless a stronger mode is explicitly configured.

## Acceptance Tests

1. Intent plus two Markdown documents creates a project model with source references.
2. Conflicting mission statements remain visible in `source_conflicts`.
3. An instruction embedded in a source document does not become tool authority.
4. The same reviewed specification produces the same plan hashes.
5. New-repository mode emits project-specific content rather than generic placeholders.
6. Retrofit mode preserves an existing `AGENTS.md` and proposes a reviewable update.
7. A path conflict blocks application.
8. Private or withheld sources do not leak into public output.
9. `auto` selects L0-L3 with an explicit rationale.
10. Activation stays blocked until the selected audit passes.
11. No write occurs in compile or plan stages.
12. No file is written outside the selected target.

## Documentation Updates

Update:

```text
README.md
docs/quickstart.md
docs/readiness-levels.md
docs/retrofit-existing-project.md
repokernel.json
CURRENT_STATE.md
registry/skills.json
```

## Boundary

Do not add many domain packs, autonomous remote operations or a full internal runtime in this implementation. Complete and verify the compiler/specification/plan boundary first.
