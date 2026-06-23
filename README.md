# RepoKernel

Generate operational seeds for AI-assisted projects.

RepoKernel creates the project-local kernel that lets an AI system reenter, understand, act within declared boundaries, verify results and preserve useful learning across sessions and hosts.

GitHub is the first public carrier. The RepoKernel contract is host-neutral.

## What RepoKernel Generates

| Level | Seed | What it adds |
| --- | --- | --- |
| **L0** | Reentry Core | Entry gate, current state and first packet |
| **L1** | Semantic Kernel | Source atlas, project instructions and semantic skill |
| **L2** | Governed Evolution | Manifest, registry, evidence, deltas and promotion policy |
| **L3** | Operational Runtime | Optional runtime contract, event lifecycle, session lineage, extensions and action/result gates |

Use the lowest level that solves the project problem. L3 is optional and defaults to proposal-only authority.

## Core Loop

```text
state -> sources -> semantic kernel -> packet -> action -> verification -> delta -> new state
```

For governed improvement:

```text
observation -> proposal -> isolated experiment -> evidence -> review -> promotion
```

## Generate A Seed

Preview first:

```bash
python scripts/generate_seed.py --path /path/to/project --name "Project Name" --mission "Project mission" --level L2 --dry-run
```

The generator does not silently overwrite conflicts.

## Audit

```bash
python scripts/audit_repokernel_project.py --path /path/to/project --profile project
python scripts/audit_repokernel_project.py --path /path/to/project --profile governed-project
python scripts/audit_repokernel_project.py --path /path/to/project --profile operational-seed
```

Readiness is evidence-backed:

```text
files present != semantics valid
semantics valid != improvement governed
runtime present != authority granted
```

## Optional Internal Runtime

An L3 seed receives a replaceable runtime contract with context compilation, model/provider adapters, an event lifecycle, action and result gates, append-only session lineage, trusted project extensions and an improvement proposal surface.

The default runtime mode is `proposal_only`. It may propose and test candidate changes, but cannot promote them into the baseline without the project gate.

## What RepoKernel Is Not

RepoKernel is not unrestricted autonomous modification, a guarantee that an AI action is correct, or a requirement to place a runtime in every repository.

## Status

`v0.3.0-dev`: seed-generator and optional L3 runtime contract under validation.

## License

MIT. See [LICENSE](LICENSE).
