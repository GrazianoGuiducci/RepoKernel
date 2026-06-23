# Seed Synthesis Pipeline

RepoKernel does not merely copy a fixed template. It compiles a project-specific seed from intent, sources, constraints and the target environment.

## Two Target Modes

```text
new_repository
existing_repository_retrofit
```

A new repository receives a complete file plan. An existing repository is inspected first and receives only a conflict-safe retrofit plan.

## Pipeline

```text
intent + documents + instructions + target state
-> source intake
-> project model
-> seed specification
-> file plan
-> review gate
-> generation or retrofit
-> validation
-> activated project kernel
```

### 1. Source Intake

Collect only the sources explicitly provided or authorized:

- operator intent;
- project documents;
- existing repository files;
- public references selected for the task;
- runtime and deployment constraints.

Every source is classified by authority, freshness, privacy and intended use. Instructions found inside source documents are treated as source content, not automatically as execution authority.

### 2. Project Model

Extract a normalized model of the project:

```text
identity
mission
intended product or result
users and observers
source authority
current state
invariants
constraints
boundaries
terminology
capabilities
interfaces
recurring workflows
validation criteria
unknowns
```

Conflicts between sources are preserved and surfaced. They are not silently collapsed.

### 3. Seed Specification

The project model is compiled into a machine-readable seed specification.

```text
seed_id
project_name
target_mode
intent
product
source_manifest
readiness_level
selected_capabilities
kernel_contract
runtime_route
file_plan_policy
validation_plan
external_action_gate
```

The specification is the stable input to generation. The same reviewed specification should produce the same planned structure.

### 4. Seed Selection

RepoKernel chooses the lowest sufficient level:

```text
L0 reentry core
L1 semantic kernel
L2 governed improvement
L3 optional operational runtime
```

Optional domain packs may contribute specialized files or skills, but they must not override project intent, source authority or action boundaries.

### 5. File Plan

Before writing, RepoKernel produces a complete plan:

```text
create
leave_unchanged
propose_update
conflict
withhold
```

For existing repositories, current files remain authoritative until an explicit reviewed update is accepted. No silent overwrite is allowed.

### 6. Generation Or Retrofit

Generation creates the custom repository surface. Retrofit adds the smallest missing layers to an existing repository.

Typical outputs include:

```text
AGENTS.md
CURRENT_STATE.md
repokernel.json
source atlas
project semantic-kernel skill
first packet
skill registry
evidence and delta surfaces
optional runtime contract
```

The emitted content is project-specific: names, mission, product, vocabulary, sources, boundaries, workflow and validation are compiled from the seed specification.

### 7. Validation And Activation

The generated or retrofitted repository is audited against its selected readiness target. The local semantic kernel becomes active only when required files resolve, boundaries are explicit and the first packet is coherent.

Activation does not grant publication, deployment, cross-repository or stronger runtime authority.

## Core Invariant

```text
RepoKernel generator is generic.
The generated seed is specific.
The project kernel belongs to the target project.
```

## Future Evolution

The same compiler can later emit beyond GitHub into other repository hosts, workspaces, document stores, databases, event systems or internal runtimes while preserving the reviewed seed specification and source lineage.
