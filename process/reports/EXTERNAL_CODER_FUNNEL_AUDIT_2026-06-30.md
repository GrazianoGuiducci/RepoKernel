# External Coder Funnel Audit

date: 2026-06-30
status: implemented_corrections

## Purpose

Simulate how an external coder or AI agent would enter RepoKernel from the
README and decide whether the onboarding funnel is effective.

## Simulated Reader

```text
runtime:
  Codex-like or Claude Code-like external coding assistant

initial knowledge:
  knows normal repositories and coding-agent workflows;
  does not yet understand RepoKernel;
  may be asked only to evaluate usefulness for a user.

allowed authority:
  public repo read only until user grants a stronger gate.
```

## Finding 1: README Introduced CLI Before Coder-First Mode

The repository already had the right safety logic in
`docs/guides/coder-first-evaluation-flow.md`, but a cold reader of the README
encountered CLI paths before the coder-first evaluation flow.

Risk:

```text
external coder may run commands or think the next action is technical setup
before explaining value, authority and consent.
```

Correction:

```text
Added "Start Here For External Coders And Agents" near the top of README.md.
Moved coder-first and external assistant guides to the top of the guide list.
```

## Finding 2: Public Capability Sources Could Look Like A First Step

The public capability source pass is useful, but adjacent repositories such as
`d-nd-ux-ai-seed`, `d-nd-seed`, `D-ND_LAB` and `KPhi1-EN` can create confusion
if introduced before the target project need is clear.

Risk:

```text
coder may start touring adjacent repos instead of evaluating RepoKernel fit.
user may think RepoKernel installs or imports those capabilities by default.
```

Correction:

```text
Marked the public capability source pass as not a first-contact step.
Clarified that external capability sources run only after target audit and
produce recommendations only.
```

## Finding 3: The Correct Funnel Is Two-Stage

The safe funnel is:

```text
stage_1:
  RepoKernel explanation, coder self-orientation, consent gate, target fit.

stage_2:
  optional public capability source pass after target audit.
```

This prevents the external packages from adding noise before the user and coder
understand the base object.

## Implemented Files

```text
README.md
docs/guides/coder-first-evaluation-flow.md
docs/guides/external-assistant-playbook.md
docs/public-capability-source-pass.md
process/reports/EXTERNAL_CODER_FUNNEL_AUDIT_2026-06-30.md
```

## Boundary

No external repositories were mutated. No package install, clone, target audit,
staging, apply, hook activation, public publish or runtime behavior was
authorized by this audit.

## Next Safe Action

Test the funnel again with a fresh external-coder prompt:

```text
Read the RepoKernel README and tell me whether this is useful for my project.
Stay read-only and do not inspect adjacent repositories unless you explain why
and ask first.
```
