# Phase 1 Packet Amendment Proposal

date: 2026-06-24
status: proposed_amendment
authority: do_not_modify_authoritative_packet_until_operator_acceptance

## Proposed Amendment

Replace the Phase 1 section of the final architecture packet with this scoped
implementation order.

## Phase 1 - Canonical Core, Planner And Guides

Objective:

```text
Establish normative contracts, canonical serialization, deterministic planning
and guide surfaces before changing generator behavior.
```

Create:

```text
pyproject.toml
src/repokernel/__init__.py
src/repokernel/canonical.py
src/repokernel/models.py
src/repokernel/paths.py
src/repokernel/planner.py
src/repokernel/guide_model.py
schemas/source-manifest.schema.json
schemas/project-model.schema.json
schemas/seed-spec.schema.json
schemas/generation-plan.schema.json
schemas/activation-report.schema.json
schemas/skill-registry.schema.json
docs/guides/README.md
docs/guides/architecture.md
docs/guides/user-guide.md
docs/guides/coder-guide.md
docs/guides/use-cases.md
docs/guides/application-types.md
docs/guides/examples/minimal-project.md
tests/unit/test_schemas.py
tests/unit/test_canonical.py
tests/unit/test_planner.py
tests/unit/test_guide_model.py
```

Rules:

```text
no project writes except generated fixtures/tests inside RepoKernel;
dry-run only for target application;
no network;
no Seed mutation;
no runtime implementation;
no autonomous cycle implementation;
unknown namespaced extensions round-trip but cannot affect authority;
guides explain contracts and examples without redefining authority.
```

Acceptance:

```text
all unit tests pass;
source audit passes;
same SeedSpec yields same canonical hash and plan;
retrofit preserves existing files and proposes updates;
private/withheld sources do not leak into public guides;
guide set is understandable for user and coder;
operator accepts before Phase 2.
```
