# A1 Local No-Write Proof

date: 2026-06-24
status: passed

## Scope

Local synthetic existing-repository proof for A1 observe-and-propose.

This proof does not use a third-party repository and does not write generated
RepoKernel files to the target.

## Setup

Temporary target:

```text
%TEMP%/repokernel-a1-local-proof/target-existing
```

Initial target files:

```text
AGENTS.md
README.md
```

SeedSpec:

```text
target.mode: existing_repository_retrofit
readiness_level: L2
authority_mode: propose
```

SourceManifest:

```text
public source: readme, public_label Existing README, used_for public_guide
private source: private-notes.md, privacy private
```

## Commands

```powershell
$env:PYTHONPATH='src'
python -m repokernel.cli inspect --path <target>
python -m repokernel.cli validate-spec --kind seed-spec --input <seed.json>
python -m repokernel.cli plan --seed-spec <seed.json> --existing-paths-file <existing-paths.txt>
python -m repokernel.cli guides --seed-spec <seed.json> --source-manifest <manifest.json>
```

## Result

```json
{
  "inspect_exists": true,
  "inspect_boundary": "read_only",
  "validate_valid": true,
  "plan_schema": "repokernel.generation-plan.v1",
  "plan_blocked": false,
  "agents_action": "propose_update",
  "readme_action": "propose_update",
  "private_label_leaked": false,
  "target_files_after": ["AGENTS.md", "README.md"],
  "no_extra_target_files": true
}
```

## Decision

The local synthetic A1 proof passes:

```text
no target writes
existing root authority classified as propose_update
.repokernel/ remains the generated control plane
private source label withheld from guides
```

External-style repository review remains blocked until a separate gate defines
identity checks, source boundaries, omonimia safeguards, network policy and
human approval of the target repository.
