# Agentic Feedback

status: active_guidance

RepoKernel improves when real agents report what helped, what confused them
and what would make the next integration safer.

Agentic feedback is public-safe evidence for maintainers. It is not authority
to change contracts, generated output, hooks, public claims or target projects.

Ask the user for permission before submitting feedback from a user evaluation.
Do not turn a private support session into public evidence without consent.

## Who Should Use This

Use this if you are:

```text
Codex;
Claude Code;
OpenCode;
Cursor/Windsurf;
an IDE assistant;
a local model agent;
a custom agentic runtime;
an orchestration system evaluating RepoKernel.
```

## What To Report

```text
agent_or_runtime:
version_or_surface:
host_environment:
mode_used:
target_type:
files_read:
commands_run:
what_helped:
what_was_confusing:
missing_context:
unsafe_or_unclear_boundary:
where_you_stopped:
recommended_next_improvement:
public_safe: yes | no
```

## Useful Signals

Good feedback says:

```text
which guide you read first;
whether the first response contract helped;
whether `not_needed` was clear;
whether staging felt safe;
whether `REVIEW_ME_FIRST` was visible;
whether public capability sources arrived too early or at the right time;
which instruction would reduce the next agent's confusion.
```

## Do Not Share

```text
tokens or credentials;
private logs;
full repository dumps;
client material;
personal data;
private source documents;
environment files;
browser/session state;
anything you cannot disclose publicly.
```

## GitHub Issue Template

If GitHub issues are enabled, use:

```text
.github/ISSUE_TEMPLATE/agentic-system-feedback.md
```

If issues are not enabled, paste the feedback into a private review packet or
send it through the user's chosen channel.

## Maintainer Triage

Treat feedback as:

```text
evidence:
  real agent experience that may reveal friction.

not authority:
  do not patch contracts or generated behavior just because one agent says so.

triage input:
  classify as docs, guide, CLI, staging, audit, schema, examples, public copy,
  hook candidate or not needed.
```

Feedback should become a change only when it reduces ambiguity, prevents a
repeatable error, improves the next safe action or clarifies a boundary.
