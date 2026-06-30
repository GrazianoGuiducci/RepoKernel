# External Assistant Playbook

Status: assistant-facing guide

Use this guide when a user asks a coding assistant:

```text
What is useful in the RepoKernel repository?
Should we clone it and use it on my project?
```

The goal is to explain the value clearly, show concrete examples and ask for
permission before cloning, inspecting or staging anything.

If the assistant/coder is not already familiar with RepoKernel, first read
[`coder-first-evaluation-flow.md`](coder-first-evaluation-flow.md). This guide
explains how a Codex-like agent, Claude Code-like assistant, OpenCode-style CLI
agent or custom agentic system should orient its own runtime and authority
before talking to the user.

## Read First

Before answering, read:

```text
README.md
docs/guides/user-guide.md
docs/guides/coder-first-evaluation-flow.md
docs/guides/use-cases.md
docs/claim-boundaries.md
docs/pre-public-checklist.md
docs/feedback.md
```

If you will run commands, also read:

```text
docs/quickstart.md
docs/guides/cli-reference.md
```

Do not introduce optional public capability source repositories in the first
answer unless the user asks what adjacent capabilities may help a specific
project. First explain RepoKernel itself, the no-apply boundary and the consent
gate.

## Plain Explanation

RepoKernel is useful when a project needs to be easier for AI assistants and
humans to reenter later.

It does not try to make a project autonomous. It adds a reviewable project
memory layer: current state, source atlas, first packet, boundaries, local
rules, skills, evidence, deltas and cleanup notes.

In plain terms:

```text
RepoKernel helps a project tell the next AI:
where we are,
what sources matter,
what is safe to do,
what changed,
what not to follow,
and what the next useful action is.
```

## What Is Useful Right Now

Current useful pieces:

```text
inspect:
  read a target repository without writing to it.

audit:
  check whether a project has enough entry/state/source/skill/delta structure.

plan:
  create a target-bound GenerationPlan from authorized source contracts.

stage:
  render proposed files into a separate review directory, not into the target.

guides:
  produce user/coder/architecture/use-case guide material from reviewed inputs.

reference distribution:
  verify a generated Starter L1 Project Kernel.

learning protocol:
  teach a generated Project Kernel how to preserve useful corrections without
  storing ordinary chat.

clarity cleanup:
  classify dirty, stale or unclear files before any cleanup decision.
```

Current limits:

```text
no apply command;
no runtime/daemon;
no credential handling;
no autonomous repository modification;
no production-ready installer claim;
no write to the user's project without a later explicit gate.
```

## Example Answers By User Need

### Software Repository

```text
Useful because RepoKernel can add a local continuity layer: what the repo is,
what files and tests matter, what the current safe next action is, and what an
assistant must not overwrite. It is especially helpful if several AI sessions
or different coding tools touch the same project.
```

### AI/RAG Or Model Project

```text
Useful because model/data assumptions, evaluation notes, source lineage and
failure memory often get scattered across chats and notebooks. RepoKernel can
stage a source atlas, current state and delta area so those assumptions become
reviewable project memory.
```

### Editorial Or Research Project

```text
Useful because it can preserve corpus sources, open questions, accepted claims,
discarded hypotheses and the next writing or review packet without mixing them
into a normal README.
```

### Business Or Operations Project

```text
Useful because it can preserve offers, decision capsules, follow-up boundaries,
source evidence and next actions in a way the next assistant can read without
reconstructing everything from chat.
```

### Existing External Repository

```text
Useful in observe-and-propose mode. RepoKernel can inspect, produce a setup
capsule and stage proposed continuity files outside the target. It should stop
before writing to the repository.
```

## Response Template

Use this shape when answering a user:

```text
RepoKernel is useful if your project suffers from lost context between AI
sessions, unclear source authority, repeated re-explaining, stale decisions or
unsafe assistant edits.

What it can do now:
- inspect or audit a repo without writing to it;
- generate a reviewable plan for a Project Kernel;
- stage proposed continuity files outside the target;
- show where current state, sources, rules, evidence and next actions should
live;
- classify unclear files before cleanup.

What it cannot claim yet:
- it is not a production installer;
- it does not apply changes to your repo;
- it does not run as an autonomous agent;
- it does not handle secrets or credentials.

For your project, the likely first useful step is:
[choose one: read-only audit / observe-and-propose setup / staged Project
Kernel preview / no action yet].

Before I clone or run anything, please confirm:
1. Which repository or folder should be considered?
2. Is it okay to clone/read it locally?
3. Should I stay read-only and produce a setup report first?
```

## Consent Gate

Do not clone, fetch, inspect private content, run commands, stage files or write
to a target until the user has answered the relevant consent questions.

Minimum consent for a public repository:

```text
repo URL:
permission to clone/read locally:
desired mode: read-only audit | observe-and-propose | staged preview
private data boundary:
```

Minimum consent for a local folder:

```text
folder path:
permission to read:
permission to run RepoKernel diagnostics:
write permission: no by default
where to place reports or staging output:
```

If the user says "just look", stay read-only and produce a setup report.

## First Setup Report

After consent and read-only inspection, report:

```text
project:
mode_used:
what_repo_kernel_found:
useful_next_layer: L0 | L1 | L2 | none
proposed_files_or_sections:
what_would_improve_next_AI_reentry:
risks_or_unknowns:
what_requires_approval:
recommended_next_step:
```

## Good Questions To Ask

Ask only questions that affect the first safe action:

```text
What do you want the next AI/coder to understand without asking you again?
Which sources are authoritative for this project?
What should an assistant never overwrite or publish?
Do you want a read-only diagnosis or a staged preview?
Where should generated review output go?
```

## Do Not Say

Do not say:

```text
RepoKernel makes your repository autonomous.
RepoKernel will safely modify your project.
RepoKernel is production-ready for arbitrary repos.
RepoKernel guarantees correct AI behavior.
RepoKernel can handle your secrets safely.
```

Use practical language first. The meta structure matters because it prevents
lost context and unsafe action, not because the user needs to understand every
recursive layer.
