# Pre-Public Checklist

status: active
updated: 2026-06-30

Use this checklist before describing RepoKernel publicly beyond a controlled
experimental/research repository.

## Allowed Public Claim

```text
RepoKernel is an experimental no-apply Project Kernel compiler. It validates
authorized sources, builds target-bound generation plans, stages proposed files
outside the target repository and preserves review gates before any future
write-capable step.
```

## Do Not Claim Yet

```text
production-ready;
installer-ready;
safe for arbitrary repositories;
autonomous repo modification;
apply support;
runtime/daemon support;
public alpha for non-technical users;
trusted security boundary for secrets or private repos.
```

## Required Before A Public Tester Request

```text
hosted CI passing on GitHub;
README and quickstart aligned to current contracts;
verify-dist passing;
one current no-write diagnostic replay on a non-sensitive target;
review packet showing before_hash == after_hash;
clear feedback path;
operator-approved public wording.
```

## Current Evidence

```text
local unit suite: 50 passed on 2026-06-30
verify-dist: valid locally on 2026-06-30
non-sensitive no-write replay: before_hash == after_hash; target_writes_performed == []
CI workflow active path: .github/workflows/ci.yml
CI workflow template: docs/ci/github-actions-ci.yml
hosted CI result: needs current remote check before public tester request
first-contact preview: available in docs/first-contact-preview.md
agentic feedback channel: available, user permission required before submission
```

## Publication Asset

A single-page HTML overview now exists at `docs/overview.html`. It explains:

```text
what RepoKernel is;
what it does;
why no-write staging matters;
how SourceManifest, ProjectModel, SeedSpec and GenerationPlan connect;
what changed over time;
what is blocked;
how to try the minimal smoke path.
```

Draft public copy assets now exist for operator review:

```text
docs/public/repokernel-portfolio-card.md
docs/public/repokernel-project-page.md
```

These assets are not publication approval. Portfolio, site, LinkedIn, tester
requests and subdomain decisions remain separate operator gates.
