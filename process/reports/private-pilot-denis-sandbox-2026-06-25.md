# Private Pilot Report - Denis Sandbox

date: 2026-06-25
status: passed_no_write_private_sandbox
target: C:\PVSC\ANTI_G\denis-repokernel-pilot
mode: existing_repository_retrofit

## Purpose

Run one controlled private pilot before any public LinkedIn tester request.
The target was the local private Denis sandbox, not a third-party project and
not a live Denis repository.

## Target State Before Pilot

```text
denis-repokernel-pilot: main...origin/main, clean
```

Relevant target facts from `inspect`:

```text
exists: true
likely_mode: existing_repository_retrofit
git: true
root_agents: true
root_current_state: false
legacy_first_packet: true
repokernel_control_plane: true
repokernel_state: true
repokernel_packet: false
boundary: read_only
```

## Input Contracts

SeedSpec:

```text
schema: repokernel.seed-spec.v1
seed_id: denis-sandbox-retrofit-pilot
project.name: Denis RepoKernel Pilot Sandbox
project.intent: Evaluate a no-write RepoKernel observe-and-propose flow on a private sandbox
project.product: A staged RepoKernel setup proposal for review
target.mode: existing_repository_retrofit
target.path: denis-repokernel-pilot
readiness_level: L1
authority_mode: propose
```

SourceManifest:

```text
schema: repokernel.source-manifest.v1
sources:
  - denis-sandbox-readme, internal, planning
  - denis-sandbox-current-state, internal, planning
```

Both contracts validated successfully.

## Plan Result

The planner produced a GenerationPlan with `blocked: true`.

This is the correct result for a retrofit target with existing authority:

```text
create:
  .repokernel/packets/FIRST_PACKET.md
  .repokernel/skills/denis-repokernel-pilot-sandbox-semantic-kernel/SKILL.md

propose_update:
  AGENTS.md
  README.md

conflict:
  .repokernel/sources/SOURCE_ATLAS.md
  .repokernel/state/CURRENT_STATE.md
```

The important behavior is that existing root and `.repokernel` authorities were
not overwritten silently.

## Stage Result

Staging was run into an explicit temporary directory outside the target repo.

```text
writes_performed:
  .repokernel/packets/FIRST_PACKET.md
  .repokernel/skills/denis-repokernel-pilot-sandbox-semantic-kernel/SKILL.md
  AGENTS.md
  README.md

skipped:
  .repokernel/sources/SOURCE_ATLAS.md -> conflict
  .repokernel/state/CURRENT_STATE.md -> conflict

target_writes_performed: []
boundary: staging_only_not_apply
```

## Target State After Pilot

```text
denis-repokernel-pilot: main...origin/main, clean
```

No files were written to the target repository.

## What This Proves

```text
RepoKernel can inspect a private sandbox target.
The SeedSpec and SourceManifest contracts validate.
The retrofit planner detects existing authority and blocks unsafe overwrite.
The stage command produces a review bundle outside the target.
The stage report records target_writes_performed: [].
Internal sources are withheld from public guide output.
```

## What Is Still Missing

```text
public LinkedIn tester post approval;
GitHub link decision for public request;
one human reviewer feedback cycle;
external public/non-sensitive repository proof, if selected later;
clearer UX for saving plan.json without shell redirection;
review of whether blocked GenerationPlans should have a friendlier summary.
```

## Verdict

```text
private_pilot_first: passed for local private sandbox
public_tester_request: still gated
next_recommended_action: refine private pilot feedback flow or run one approved
public/non-sensitive repository observe-and-propose proof before LinkedIn
```

## Boundary

This report does not authorize:

```text
LinkedIn publication;
public tester request;
external repository writes;
pull requests or issues;
Seed/THIA/Lab promotion;
runtime or apply implementation.
```

