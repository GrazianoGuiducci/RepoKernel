# RepoKernel Seed/Lab Promotion Brief

date: 2026-06-24
status: candidate_brief_no_seed_patch

## Candidate

```text
candidate_name: RepoKernel
candidate_type: repository-context kernel capability
current_authority: RepoKernel repository only
promotion_status: not promoted
```

## Function

RepoKernel teaches a repository how to present its state, sources, boundaries
and next move to future AI systems.

As a Seed/Lab capability, it would provide a normalized way to:

```text
inspect a new or existing repository
validate source and project contracts
propose a Project Kernel
generate guides
audit continuity/readiness
stop before write authority unless an explicit apply gate exists
```

## Inputs

```text
target repository path or URL
target owner and identity
mode: new_repository | existing_repository_retrofit | A1 observe-and-propose
operator authorization
SourceManifest
SeedSpec
existing path list or repository snapshot
privacy/withheld-source rules
tool environment capability
```

## Outputs

```text
inspect report
validated SourceManifest
validated SeedSpec
GenerationPlan
guide projection
audit report
review packet
no-write proof
```

## Minimal Project Kernel Shape

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

Root files are adapters or host-native authorities. The canonical installed
control plane is `.repokernel/`.

## What Must Not Travel

```text
tokens, credentials, .env contents or private logs
Editoriali-specific source deposits
private D-ND paths as public defaults
THIA or Lab internals not explicitly selected
raw chat transcripts
unverified market/adoption claims
write authority
runtime/L3 authority
automatic Seed promotion
```

## Evidence So Far

```text
Editoriali incubation:
  AGENTS gate, CURRENT_STATE, bootstrap sources, editorial semantic kernel,
  memory-delta rule, RepoKernel product capsule and boundary audit.

RepoKernel Phase 1:
  CLI read-only commands: validate-spec, inspect, plan, guides, audit.
  Operational procedure for new/existing/external repositories.
  Local A1 no-write proof passed.
```

Evidence files:

```text
process/reports/editoriali-incubation-transfer-2026-06-24.md
process/reports/a1-local-no-write-proof-2026-06-24.md
docs/guides/operational-procedure.md
docs/guides/cli-reference.md
```

## Recommended First Promotion Form

Do not promote as an autonomous installer yet.

Recommended first form:

```text
Seed/Lab documentation pattern + read-only CLI capability + review packet template
```

Possible later forms:

```text
template pack
Seed function
Lab capability
controlled apply installer
service/audit offer
```

## Required Before Seed/Lab Patch

```text
external-style A1 protocol
one real public/authorized repository review with no writes
identity and omonimia safeguards
review packet template
operator acceptance of promotion scope
decision on whether Seed receives docs, templates, CLI wrapper or installer
```

## Business/Collaboration Routing

Business Manager may use RepoKernel as an offer and relationship wrapper:

```text
repo audit
AI-readable project setup
collaboration call preparation
follow-up plan
proposal language
```

Business Manager does not own the technical compiler, planner or Project Kernel
installation logic.

## Decision Needed Later

```text
Promote RepoKernel to d-nd-seed as:
  A. documentation pattern only
  B. templates + procedure
  C. read-only CLI wrapper
  D. controlled apply installer
  E. Lab/THIA capability contract
```

Current recommendation:

```text
B now after external-style A1 proof, C after package/CLI stability, D only after apply gate and rollback proof.
```
