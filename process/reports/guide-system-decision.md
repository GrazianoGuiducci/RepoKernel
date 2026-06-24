# Guide System Decision

date: 2026-06-24
status: convergence_gate_output

## Decision

Guides are essential RepoKernel surfaces for both users and coders. They must
be part of `repokernel-core`, but as applications/projections of canonical
contracts, not as duplicated project authority.

## Guide Set For Phase 1

```text
docs/guides/README.md
docs/guides/architecture.md
docs/guides/user-guide.md
docs/guides/coder-guide.md
docs/guides/use-cases.md
docs/guides/application-types.md
docs/guides/examples/minimal-project.md
```

## Required Coverage

Each guide set must explain:

```text
what RepoKernel is
what it is not
compiler/generator architecture
Direct Start
Synthesis from sources
Existing Repository Retrofit
A1 observe-and-propose
readiness L0-L3
authority and autonomy boundaries
file layout and generated artifacts
how a coder works with schemas, planner and tests
how a user chooses a mode
use cases and application types
example walkthrough
```

## Guide Authority Rule

```text
guides explain canonical contracts;
guides do not redefine canonical contracts;
guides may include examples;
examples are not authority;
guide statements must cite source contract, schema or packet when they affect
behavior.
```

## User/Coder Split

User guide:

```text
problem-first language
mode selection
expected outputs
what approval is needed
what not to do
```

Coder guide:

```text
schemas
canonical serialization
planner behavior
dry-run/apply boundaries
tests
extension handling
compatibility wrappers
```

## Application Types

Phase 1 guides should cover at least:

```text
software repository
AI/RAG or model project
editorial/book project
business operating function
research/lab project
portfolio/creator project
multi-repo system as future/deferred constellation
```

## Example Requirement

The first example must show:

```text
project intent
source manifest
ProjectModel summary
reviewed SeedSpec
GenerationPlan dry run
generated guide excerpt
ActivationReport blocked/active result
```
No example may imply autonomous writes, Seed install or runtime operation.
