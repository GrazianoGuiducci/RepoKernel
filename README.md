# RepoKernel

Generate project-specific operational seeds for AI-assisted work.

RepoKernel assimilates project intent, supplied documents, existing repository state and environment constraints, then compiles a custom project kernel. The result is not a generic template copy: it is RepoKernel reconfigured for the target project's mission, product, sources, terminology, boundaries and validation needs.

GitHub is the first public carrier. The RepoKernel contract is host-neutral.

## Target Modes

```text
new_repository
existing_repository_retrofit
```

For a new project, RepoKernel produces a complete reviewed file plan. For an existing repository, it inspects current files and proposes only the smallest conflict-safe additions or updates.

## Synthesis Pipeline

```text
intent + documents + instructions + repository state
-> source intake
-> project model
-> seed specification
-> file plan
-> review gate
-> generation or retrofit
-> validation
-> activated local kernel
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

Create the current minimal project structure:

```bash
python scripts/scaffold_repokernel_project.py --path /path/to/project --name "Project Name" --mission "Project mission"
```

Audit a project:

```bash
python scripts/audit_repokernel_project.py --path /path/to/project --profile project
```

The shared L0-L3 generation library is in `scripts/repokernel_core.py`. Intent/document assimilation, command integration and repository-hosted regression tests are the current implementation track.

## Evidence Rule

```text
files present != semantics valid
semantics valid != improvement governed
runtime present != authority granted
```

## Optional Internal Runtime

An L3 seed may receive a replaceable runtime contract with context preparation, model/provider adapters, an event lifecycle, action and result gates, append-only session lineage, trusted project extensions and a candidate-improvement surface.

The initial mode is proposal-only. Candidate changes still pass through project review before becoming part of the accepted baseline.

## What RepoKernel Is Not

RepoKernel is not unrestricted autonomous modification, a guarantee that an AI action is correct, or a requirement to place a runtime in every repository.

## Status

`v0.4.0-dev`: project-seed synthesis from intent and documents is now specified; compiler and retrofit implementation remain under validation.

## License

MIT. See [LICENSE](LICENSE).
