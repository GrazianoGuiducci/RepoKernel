# RepoKernel Architecture Guide

RepoKernel is a host-neutral Project Kernel compiler.

It is not a template to copy into every repository. It compiles an authorized
project description and source set into a reviewed `SeedSpec`, then produces a
deterministic `GenerationPlan` for a Project Kernel.

```text
SourceManifest
-> ProjectModel
-> reviewed SeedSpec
-> GenerationPlan
-> dry-run / reviewed application
-> ActivationReport
```

Core does not depend on cognition, cycle, runtime or departments.

Phase 1 authority is proposal-oriented:

```text
authority_mode: none | read | propose | proposal_only
```

No schema, guide, extension or planner output can grant writes, deployment,
network access, Seed promotion or autonomous execution.
