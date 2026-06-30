# RepoKernel Operational Procedure

This procedure tells an AI coder how to use RepoKernel to understand, evaluate
and prepare a Project Kernel for a new or existing repository.

It is the current operating procedure for Phase 1. It is proposal-first and
write-safe: the procedure can inspect, validate, plan and produce guide output,
but it does not install files into a target repository.

## Operating Principle

```text
observe -> identify authority -> validate sources -> plan -> review -> evidence -> next gate
```

RepoKernel is not a template copy. It is a semantic kernel compiler that helps
a coder preserve project continuity, source lineage, state, packets, evidence,
guides, boundaries and future reentry.

When the procedure is driven by a new experience, correction or downstream
system signal, apply the minimum-action improvement contract before adding a
file, feature, hook or public claim. A durable change is justified only when it
reduces more ambiguity, rework or unsafe authority drift than it adds. Otherwise
the correct output is `no_cycle`.

## Roles

```text
operator: chooses target, authorizes sources and approves gates
AI coder: observes, validates, plans and reports
RepoKernel: provides contracts, planner, CLI, guide model and audit
target repository: remains authoritative over existing files
reviewer: checks the proposal before any write-capable gate
```

One process should not silently choose intent, generate changes, apply them,
evaluate them and promote them.

## Required Inputs

Before running RepoKernel on a target, collect:

```text
target_path_or_url:
target_owner:
target_identity:
intended_mode: new_repository | existing_repository_retrofit | A1 observe-and-propose
operator_authorization:
allowed_sources:
private_or_withheld_sources:
write_authority: none | future_reviewed_gate
publication_boundary:
```

For external people, clients, partners or public repositories, add:

```text
identity_check:
omonimia_check:
source_provenance:
relationship_context:
privacy_notes:
```

Do not infer that a repository belongs to a person only because names or topics
look similar.

## Procedure

### 1. Select Mode

Use:

```text
new_repository
existing_repository_retrofit
A1 observe-and-propose
```

Use A1 when the repository belongs to another person, a client, a partner, a
friend or any case where write authority has not been explicitly granted.

### 2. Inspect The Target

Run:

```bash
PYTHONPATH=src python -m repokernel.cli inspect --path /path/to/project
```

Record whether the target has:

```text
git repository
root AGENTS.md
root CURRENT_STATE.md
legacy process/FIRST_PACKET.md
.repokernel/ control plane
existing project conventions
```

This step is read-only.

### 3. Build SourceManifest

Classify every source that will influence the plan:

```text
source_id
authority
privacy: public | internal | private | withheld
used_for
public_label, only when safe for public guides
withheld_reason, when relevant
```

Public guide output may include a source only when:

```text
privacy: public
used_for includes public_guide
```

### 4. Build SeedSpec

The SeedSpec must name:

```text
seed_id
project.name
project.intent
project.product
target.mode
target.path, when local
readiness_level
authority_mode
```

In Phase 1, `authority_mode` must not exceed:

```text
none | read | propose | proposal_only
```

### 5. Validate Contracts

Run:

```bash
PYTHONPATH=src python -m repokernel.cli validate-spec --kind source-manifest --input sources.json
PYTHONPATH=src python -m repokernel.cli validate-spec --kind seed-spec --input seed.json
```

Stop if validation fails. Do not repair by weakening the contract unless the
contract itself is demonstrably wrong.

### 6. Plan

For a new repository:

```bash
PYTHONPATH=src python -m repokernel.cli validate-bundle --source-manifest sources.json --project-model project-model.json --seed-spec seed.json
PYTHONPATH=src python -m repokernel.cli plan --seed-spec seed.json --source-manifest sources.json --project-model project-model.json > plan.json
```

For an existing repository, provide known existing paths:

```bash
PYTHONPATH=src python -m repokernel.cli plan --seed-spec seed.json --source-manifest sources.json --project-model project-model.json --existing-paths-file paths.txt > plan.json
```

Review item actions:

```text
create: safe candidate for missing file
propose_update: existing authority requires review
conflict: do not write
withhold: source or target condition blocks output
leave_unchanged: no operation
```

Existing root authority must never be overwritten silently.

### 7. Stage For Review

Render proposed files into a separate empty review directory:

```bash
PYTHONPATH=src python -m repokernel.cli stage --plan plan.json --output-dir ./repokernel-staging
```

Check:

```text
the staging directory was empty before the command;
the staged files match the GenerationPlan;
target_writes_performed is [];
no target repository files changed.
```

This step is optional for pure JSON review, but required before asking external
testers to inspect generated files.

### 8. Generate Guides

Run:

```bash
PYTHONPATH=src python -m repokernel.cli guides --seed-spec seed.json --source-manifest sources.json
```

Check:

```text
private labels absent
withheld sources absent
guide text does not grant authority
guide text points to review and boundaries
```

### 9. Audit

For RepoKernel itself:

```bash
PYTHONPATH=src python -m repokernel.cli audit --path . --profile repokernel-source
```

For a target project where a Project Kernel already exists:

```bash
PYTHONPATH=src python -m repokernel.cli audit --path /path/to/project --profile project
```

Audit is evidence, not automatic promotion.

### 10. Produce Review Packet

Before any write-capable step, produce a review packet with:

```text
target identity and owner
mode
source manifest summary
SeedSpec hash or path
GenerationPlan summary
propose_update and conflict list
privacy/withheld-source check
no-write evidence
operator decision needed
```

### 11. Stop Before Apply

Phase 1 has no `apply` command.

The procedure stops at:

```text
validated proposal
human-readable review packet
evidence that no target files were written
```

Writing to a target repository requires a later reviewed apply gate with:

```text
confirmed plan hash
snapshot or rollback strategy
explicit target path
explicit write authorization
post-write audit
memory delta
```

## New Repository Path

For a new repository, the default proposed control plane is:

```text
AGENTS.md
.repokernel/state/CURRENT_STATE.md
.repokernel/packets/FIRST_PACKET.md
.repokernel/sources/SOURCE_ATLAS.md
.repokernel/skills/
.repokernel/registry/
.repokernel/evidence/
.repokernel/deltas/
```

Root files are adapters or project-native files. The canonical Project Kernel
state lives under `.repokernel/`.

## Existing Repository Path

For an existing repository:

```text
inspect first
preserve current conventions
classify root authority
propose updates, do not overwrite
keep RepoKernel state under .repokernel/
report conflicts instead of resolving them silently
```

## External Repository Safeguards

Before observing a real external repository:

```text
confirm repository URL
confirm owner identity
check for omonimia
record relationship context
use only public or authorized sources
do not clone private material without authorization
do not write or open PRs without a later explicit gate
```

This protects against wrong-person assumptions, biased source selection and
accidental disclosure of private context.

## Output Checklist

A complete procedure run should leave:

```text
inspect report
valid SourceManifest
valid SeedSpec
GenerationPlan
guide JSON or guide draft
privacy check
no-write proof
review packet
next gate decision
```

For experience-driven improvement, also leave either:

```text
no_cycle
```

or a receipt with:

```text
source;
surface owner;
tension;
minimum artifact;
expected fitness gain;
boundary;
validation;
next gate.
```

## Current Boundary

```text
allowed: read, validate, inspect, plan, guide, audit, report
blocked: apply, overwrite, deploy, publish, Seed promotion, runtime activation
```
