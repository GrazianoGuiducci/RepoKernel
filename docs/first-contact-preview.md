# First Contact Preview

status: active_guidance

Users may need to see RepoKernel safely before allowing it near real work.
The first integration should therefore offer a preview path, not only an
architecture explanation.

## Purpose

Give the user a concrete, low-risk experience:

```text
what RepoKernel would notice;
what it would propose;
where review happens;
what remains untouched;
what permission would be needed next.
```

The preview is not an install, an apply step, a hook activation or a production
claim.

## Evaluator Profiles

Ask which profile best matches the current user:

```text
fast evaluator:
  wants a quick demo, likely on sample data, then decides whether to continue.

careful creator:
  wants to understand the internal logic before touching real projects.

project owner:
  has a specific repository/folder and wants a read-only setup report.

agentic integrator:
  wants to map RepoKernel into a larger host system, skill layer, hook system
  or workflow runtime.

non-development operator:
  wants continuity for business, research, editorial, monitoring or operations.
```

Do not force every user through the same explanation depth.

## Preview Ladder

Use the smallest preview that builds trust:

```text
P0 plain explanation:
  no commands; explain value and limits.

P1 included-fixture demo:
  run or describe RepoKernel against included examples only.

P2 synthetic-context demo:
  use a small user-approved fictional scenario; no private project read.

P3 read-only folder assessment:
  inspect a user-approved folder and produce a setup report; no writes.

P4 external staged preview:
  stage proposed continuity files into an empty review directory outside the
  target; target remains untouched.
```

If the user is a reviewer, creator or public evaluator, P1/P2 is often enough.
If the user owns a real project and wants practical value, P3/P4 may be useful
after explicit consent.

## Coder Procedure

Before touching a target project:

```text
1. identify evaluator profile;
2. choose preview level P0-P4;
3. state what will remain untouched;
4. state which files or commands will be used;
5. produce a short preview receipt;
6. ask whether the user wants to continue, stop, or leave feedback.
```

## Preview Receipt

```text
preview_level:
evaluator_profile:
target_or_fixture:
mode:
sources_read:
commands_run:
what_was_demonstrated:
what_remained_untouched:
next_possible_step:
approval_needed:
feedback_permission_asked: yes | no
```

## Feedback Permission

At the end of a preview, ask gracefully:

```text
Would you like me to leave public-safe feedback for the RepoKernel maintainers
about what was clear, confusing or useful in this evaluation?
```

If the user says yes, use `docs/agentic-feedback.md` or the GitHub issue
template. If the user says no, do not create feedback.

## Boundary

Do not use a preview to smuggle in:

```text
target writes;
hook activation;
background automation;
credential handling;
public claims;
adjacent repository imports;
private source disclosure;
full repository dumps.
```
