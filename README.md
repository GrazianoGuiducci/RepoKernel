# RepoKernel

Generate project-specific operational seeds for AI-assisted work.

RepoKernel now has a Phase 1 core package in `src/repokernel/`: canonical
contracts, deterministic planning, dry-run reporting and guide projections.

RepoKernel assimilates project intent, supplied documents, existing repository state and environment constraints, then compiles a custom project kernel. The result is not a generic template copy: it is RepoKernel reconfigured for the target project's mission, product, sources, terminology, boundaries and validation needs.

GitHub is the first public carrier. The RepoKernel contract is host-neutral.

## One Compiler, Two Distribution Forms

```text
RepoKernel Source / Compiler
        -> reviewed SeedSpec
        -> Project Kernel
```

A coder may consume RepoKernel in two forms:

- **Reference Seed** — a precompiled SeedSpec that can be copied or cloned directly;
- **Synthesized ProjectSeed** — a custom SeedSpec compiled from project intent and authorized sources.

These are not separate systems. Reference Seeds must be reproducible by the same compiler and schemas used for custom seeds.

## Application Modes

```text
new_repository
existing_repository_retrofit
```

For a new project, RepoKernel produces a complete reviewed file plan. For an existing repository, it maps current authority and proposes the smallest conflict-safe overlay. Retrofit is an application mode of the same SeedSpec, not a separate product.

## Synthesis Pipeline

```text
intent + documents + instructions + repository state
-> source intake
-> ProjectModel
-> reviewed SeedSpec
-> file plan
-> review gate
-> generation or retrofit
-> validation
-> activated Project Kernel
```

The generic generator remains stable. Each emitted seed belongs to its target project.

## What RepoKernel Generates

| Level | Seed | What it adds |
| --- | --- | --- |
| **L0** | Reentry Core | Entry gate, current state and first packet |
| **L1** | Semantic Kernel | Source atlas, project instructions and semantic skill |
| **L2** | Governed Improvement | Manifest, registry, evidence, deltas and review policy |
| **L3** | Operational Runtime | Optional runtime contract, event lifecycle, session lineage and action/result gates |

Use the lowest level that solves the project problem. L3 is optional and begins with proposal-only authority.

## Core Loop

```text
state -> sources -> semantic kernel -> packet -> action -> verification -> delta -> new state
```

For reviewed improvement:

```text
observation -> proposal -> test -> evidence -> review -> accepted change
```

## Current Usage

Read the Phase 1 guides first:

```text
docs/guides/user-guide.md
docs/guides/coder-guide.md
docs/guides/architecture.md
```

Create the current minimal project structure:

```bash
python scripts/scaffold_repokernel_project.py --path /path/to/project --name "Project Name" --mission "Project mission"
```

Audit a project:

```bash
python scripts/audit_repokernel_project.py --path /path/to/project --profile project
```

The Phase 1 core package is in `src/repokernel/`. The previous shared L0-L3
generation library in `scripts/repokernel_core.py` remains a compatibility
prototype until parity tests replace it.

## Evidence Rule

```text
files present != semantics valid
semantics valid != improvement governed
runtime present != authority granted
```

## Optional Internal Runtime

An L3 seed may receive a replaceable runtime contract with context preparation, model/provider adapters, an event lifecycle, action and result gates, append-only session lineage, trusted project extensions and a candidate-improvement surface.

The initial mode is proposal-only. Candidate changes still pass through project review before becoming part of the accepted baseline.

## Current Gate

The next implementation is intentionally paused until GPT Pro returns the final architecture and phased Codex packet defined in:

```text
packets/FOR_GPT_PRO/REPOKERNEL_FINAL_ARCHITECTURE_REVIEW_2026-06-23.md
```

## What RepoKernel Is Not

RepoKernel is not unrestricted autonomous modification, a guarantee that an AI action is correct, or a requirement to place a runtime in every repository.

## Status

`v0.3.0-dev`: Phase 1 core contracts, planner and guide surfaces under test.

## License

MIT. See [LICENSE](LICENSE).
