# Delta: Public Capability Source Pass

date: 2026-06-30
status: active_design_candidate

## Trigger

The operator proposed that RepoKernel, after auditing a target project and
before generating or regenerating its Project Kernel, could look at other
public neutral repositories that contain useful THIA-derived capabilities:

```text
GrazianoGuiducci/d-nd-ux-ai-seed
GrazianoGuiducci/d-nd-seed
GrazianoGuiducci/D-ND_LAB
GrazianoGuiducci/KPhi1-EN
```

## Decision

Add a documented optional pass that reads public capability sources and
produces a target-specific recommendation report.

## Change

```text
added:
  docs/public-capability-source-pass.md
  docs/public/linkedin-repokernel-intro-draft.md

updated:
  README.md
  docs/public/repokernel-project-page.md
  sources/bootstrap/SOURCE_ATLAS_v1.0.md
  process/DECISION_LOG.md
  CURRENT_STATE.md
```

## Preserved Rule

```text
RepoKernel may recommend public neutral capabilities after target audit.
RepoKernel must not import private state or install capabilities by default.
```

## Boundary

No private clone, no automatic install, no target mutation, no hook activation,
no Lab run, no publishing and no claim that public capability sources are
universally appropriate.

## Next Safe Action

Use the public capability source pass manually on the next suitable target and
evaluate whether its report shape is stable enough to become a schema or CLI
option later.
