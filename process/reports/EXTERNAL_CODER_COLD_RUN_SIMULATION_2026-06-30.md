# External Coder Cold-Run Simulation

date: 2026-06-30
status: passed_with_notes
mode: public_repo_read

## Scenario

A user asks an external AI coder:

```text
What is useful in RepoKernel, and should we use it on my project?
```

Assume the coder has no prior RepoKernel context and has not been granted
permission to clone adjacent repositories, inspect private folders, run
diagnostics or write to a target project.

## Read Path Simulated

```text
README.md
docs/guides/coder-first-evaluation-flow.md
docs/guides/external-assistant-playbook.md
docs/integration-surfaces.md
docs/agentic-feedback.md
docs/claim-boundaries.md
```

## Expected First Answer

```text
mode_used: public_repo_read
RepoKernel fit: useful_if_context_loss_or_authority_problems_exist
why: it gives projects a reviewable continuity layer for AI-assisted work
what_not_to_do: no clone, no private inspection, no diagnostics, no target write
safe_next_step: ask whether the user wants explanation only, read-only assessment or staged preview
approval_needed: target path or repo, read permission, diagnostic permission if needed, staging output path
```

## Result

The current funnel is understandable enough for a cold external coder to avoid
the main failure modes:

```text
no premature clone;
no automatic adjacent capability import;
no hook or runtime assumption;
no target write;
`RepoKernel not needed` remains valid;
feedback is evidence, not authority.
```

The new `docs/integration-surfaces.md` answers the user's likely next question:

```text
How does this enter my system?
```

The answer is now explicit:

```text
A0 explain only
A1 read-only assessment
A2 no-write diagnostic
A3 external staged preview
A4 reviewed target integration
A5 host-specific hooks or runtime automation
```

## Notes

The package should not claim that hooks, skills or runtime automation are
available by default. RepoKernel can generate or inform those forms later, but
only after the host runtime, lifecycle event, authority boundary and review
gate are known.

For non-development projects, explain RepoKernel in functional terms:

```text
source files -> authoritative sources
tests -> validation checks
commits -> accepted decisions
issues -> open questions or tasks
skills -> reusable procedures
hooks -> workflow checkpoints
```

## Next Improvement Candidate

If repeated external feedback shows confusion, add a one-page
`docs/first-contact.md` that combines the shortest user explanation, consent
gate and first answer template.
