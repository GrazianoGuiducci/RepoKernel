---
name: skill-promotion-router
description: Use when deciding whether a capability should stay draft, become candidate, be accepted, be promoted to a broader package, remain private or be classified as residue.
---

# Skill Promotion Router

This is the central RepoKernel meta-skill.

## Decision

Route a capability to one of:

```text
draft
candidate
accepted
public_repo
seed_candidate
private
documentation_only
residue
```

## Promotion Packet

Before promotion, write:

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

## Boundary

Do not promote private assumptions, credentials, local paths, internal logs, client material or unverified claims.

