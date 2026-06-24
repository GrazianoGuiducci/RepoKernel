# RepoKernel Distribution Readiness Gate

date: 2026-06-25
status: draft_gate_for_morning_work
authority: review_only

## Purpose

Before asking public LinkedIn testers to try RepoKernel, verify exactly what is
safe and honest to test.

## Current Public Claim

Allowed:

```text
RepoKernel is a public Phase 1 project-kernel planner/contract surface.
It can validate specs, inspect a repo, produce a plan, generate guide
projections and run audits without writing to the target repository.
```

Blocked:

```text
finished installer;
apply command;
autonomous repo modification;
production runtime;
Seed/THIA/Lab integration;
guaranteed correctness;
unreviewed external writes.
```

## Required Checks

Run:

```powershell
python -m pytest
$env:PYTHONPATH="src"; python -m repokernel.cli audit --path . --profile repokernel-source
python scripts\phase0_inventory.py --root . --out process\reports
git diff --check
git status --short --branch
```

Review:

```text
README.md
docs/guides/user-guide.md
docs/guides/coder-guide.md
docs/guides/operational-procedure.md
docs/feedback.md
packets/FOR_CODEX/A1_EXTERNAL_STYLE_PILOT_PACKET_2026-06-24.md
```

## Tester-Safe Scope

Testers may be asked to:

```text
read README and guides;
run read-only CLI commands locally;
try observe-and-propose on a public or non-sensitive repo;
review the generated proposal;
send privacy-safe feedback.
```

Testers must not be asked to:

```text
share secrets or private logs;
run on client/confidential repositories without permission;
expect automatic installation;
allow writes into target repos;
judge production readiness from Phase 1 P0.
```

## Publish Decision

Choose one:

```text
publish:
  readiness checks pass and post wording is accurate.

hold:
  README/guides still overpromise or test path is unclear.

private_pilot_first:
  use one selected trusted tester before LinkedIn.
```

## First Safe Morning Move

Run the checks, then produce a short readiness verdict before editing or
publishing any LinkedIn post.
