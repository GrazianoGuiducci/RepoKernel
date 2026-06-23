# RepoKernel Distribution Model

## Resultant

RepoKernel has one generative logic and multiple delivery forms.

```text
RepoKernel Source / Compiler
        ↓ compiles
      SeedSpec
        ↓ materializes
   Project Kernel
```

The apparent tension between “clone a seed directly” and “generate a custom seed” is resolved by treating the direct seed as a **precompiled distribution** of the same compiler.

## Core Objects

### RepoKernel Source

The mother repository containing:

- the semantic method;
- schemas and compiler contracts;
- meta-skills;
- deterministic emitters;
- audits and tests;
- reference distributions;
- runtime and adapter contracts.

It is not copied wholesale into every target project.

### SeedSpec

The reviewed intermediate contract from which a project seed is emitted.

A SeedSpec preserves:

```text
project identity
intent and product
source lineage
invariants
terminology
boundaries
selected readiness level
selected capabilities
runtime route
file-plan policy
validation and activation conditions
```

### Reference Seed

A precompiled SeedSpec and its materialized files for a common starting condition.

Examples:

```text
starter-l0
starter-l1
starter-l2
```

A coder may copy or clone a Reference Seed directly. It is not separate logic: it must be reproducible from the same generator and schemas used for custom seeds.

### Synthesized ProjectSeed

A custom SeedSpec compiled from operator intent, authorized documents, repository state and environment constraints.

It produces project-specific names, instructions, source atlas, semantic kernel, packets, validation and optional runtime contract.

### Application Mode

The SeedSpec is applied in one of two modes:

```text
new_repository
existing_repository_retrofit
```

`existing_repository_retrofit` produces a conflict-aware overlay plan. Retrofit is therefore an application mode, not a separate ontology.

### Project Kernel

The activated local result inside the target project. It belongs to that project and may evolve independently through evidence, deltas and reviewed promotion.

### Optional Runtime

A replaceable execution body around the Project Kernel. It is selected only when the project proves a need for host-independent operation. Runtime presence does not grant authority.

## Three User Journeys

### Direct Start

```text
choose Reference Seed
→ copy or clone
→ customize minimal project fields
→ audit
→ activate local Project Kernel
```

Use for new and relatively simple projects.

### Synthesis

```text
intent + sources
→ ProjectModel
→ reviewed SeedSpec
→ deterministic file plan
→ materialize new repository
→ audit
→ activate local Project Kernel
```

Use when source material, domain language or product structure must be assimilated.

### Retrofit

```text
existing repository + intent + selected sources
→ repository map
→ ProjectModel
→ reviewed SeedSpec
→ overlay plan
→ resolve conflicts
→ apply approved changes
→ audit
→ activate local Project Kernel
```

Use when a project already has canon, instructions, workflows or runtime surfaces.

## One Logic, No Duplication

The following must remain true:

```text
Reference Seed = precompiled SeedSpec
Synthesized ProjectSeed = custom SeedSpec
Retrofit Overlay = SeedSpec applied to an existing target
Project Kernel = validated materialization of a SeedSpec
```

Any starter distribution that cannot be reproduced by the compiler is drift and must fail validation.

## Product Boundary

The coder-facing product is the smallest consumable seed or command needed for the selected journey. The source repository remains the factory, proof system and evolutionary nucleus.
