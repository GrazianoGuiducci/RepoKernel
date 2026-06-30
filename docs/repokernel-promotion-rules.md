# RepoKernel Promotion Rules

Promotion means turning a useful local pattern into a reusable public or portable asset.

## Promotion Gate

Before promotion, prepare a packet with:

```text
candidate_name:
function:
inputs:
outputs:
minimal_files:
what_must_not_travel:
proof:
open_risks:
recommended_layer:
```

## Do Not Promote

Do not promote:

- private paths;
- credentials;
- logs;
- client or personal material;
- unverified claims;
- local runtime assumptions;
- examples that only work in one private workspace.

## Promotion Targets

```text
public_repo
template_pack
project_skill
seed_candidate
internal_private_tool
documentation_only
residue
```

Promotion requires explicit owner approval when it changes a public surface, canon, external package or another repository.

## Experience Promotion Filter

An experience from a downstream system, local node, client context, private
assistant, Seed, THIA or Lab may become a RepoKernel improvement only after it
passes the minimum-action filter:

```text
does it reduce ambiguity, rework, unsafe authority drift or duplicated files?
can it be stated without private paths, secrets or product-specific claims?
does RepoKernel own the rule, or does it belong to the downstream system?
what is the smallest artifact that preserves the learning?
what validation proves the change stayed bounded?
```

If the rule belongs to a downstream system, prepare a promotion packet or
residue note instead of patching RepoKernel core. If the rule belongs to
RepoKernel, neutralize it before adding it to public docs, tests or contracts.
If the rule belongs to the generated Project Kernel pattern, it must be
projected into staged project output rather than left as RepoKernel-only
commentary.

Relevant gate:

```text
docs/minimum-action-improvement-contract.md
```
