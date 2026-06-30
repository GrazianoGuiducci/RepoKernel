# Coder-First Evaluation Flow

Status: assistant/coder-facing guide

Use this guide when a user asks a coding assistant, AI IDE, CLI agent or
agentic system to evaluate RepoKernel before using it.

RepoKernel speaks primarily to the coder/agent layer. The user may only want a
plain assessment. The coder may not yet understand RepoKernel, may not have
read the repository, and may not have authority to clone, inspect private
folders or run commands.

The first contact must therefore produce two things:

```text
1. a clear user-facing explanation;
2. a context-aware next-step proposal for the coder/agent runtime.
```

## First Principle

Do not start by installing, cloning or pitching the whole architecture.

Start by locating the evaluation context:

```text
Who is asking?
What project or workflow is being considered?
Which coder/agent runtime is active?
What can be read?
What cannot be touched?
What output would help the user decide?
```

RepoKernel is useful only if it improves continuity, authority, reentry,
evidence, cleanup or safe next action. If the user only needs a normal README,
bug fix or one-off script, say that RepoKernel may be unnecessary.

`RepoKernel not needed` is not a failure. It is the correct answer when the
project does not show a continuity, authority, reentry, evidence or cleanup
problem that justifies a Project Kernel.

## Coder Self-Orientation

Before answering the user, the coder should identify itself in practical terms:

```text
runtime:
  Codex | Claude Code | OpenCode | Cursor/Windsurf | custom agent |

available_capabilities:
  read files?
  run shell?
  use git?
  access network?
  edit files?
  stage review output outside target?
  create commits or PRs?

authority:
  explain only?
  read public repo?
  read local folder?
  run no-write diagnostics?
  stage preview files?
  write to target?
```

If the coder cannot answer these questions, it must stay in `explain_only`
or `read_only_assessment` mode.

## Read Order For A Coder

If RepoKernel is already available locally, read:

```text
README.md
docs/guides/external-assistant-playbook.md
docs/guides/user-guide.md
docs/guides/use-cases.md
docs/claim-boundaries.md
docs/pre-public-checklist.md
```

If the user asks for command-level evaluation and grants permission, also read:

```text
docs/guides/cli-reference.md
docs/guides/operational-procedure.md
docs/runtime-adapters.md
```

If the coder is only browsing a public repository, do not assume local CLI
availability. Explain what RepoKernel can do from the docs, then ask whether a
local read-only checkout is allowed.

Do not open the public capability source pass during first contact unless the
user has already selected a target project and authorized a read-only target
assessment. External capability repositories can improve a later fit report,
but they can confuse the first evaluation if they appear before the project
need is clear.

## Evaluation Modes

Use one of these modes explicitly:

```text
explain_only:
  No clone, no commands. Explain what RepoKernel is useful for and when it is
  not needed.

public_repo_read:
  Read only public repository files. No private folders, no target project
  inspection.

local_read_only_assessment:
  Read a user-approved local folder or repo. No writes and no generated files.

no_write_diagnostic:
  Run RepoKernel diagnostics that inspect or audit without mutating the target.

staged_preview:
  Render proposed Project Kernel files into an empty external review directory.
  The target repository remains untouched.

write_gate:
  Any target write, commit, PR, apply step or automation requires a separate
  explicit approval. Current RepoKernel does not provide a general apply
  command.
```

External capability sources belong after `local_read_only_assessment` or
`no_write_diagnostic`, never before the user understands the base RepoKernel
fit.

## First Output Contract

Before clone, local inspection, diagnostics or staging, the first coder answer
must give the user a bounded decision object:

```text
mode_used:
repo_or_project:
runtime:
RepoKernel fit: useful | not_needed | defer
why:
what_not_to_do:
safe_next_step:
approval_needed:
if_staging: create or read REVIEW_ME_FIRST before any target write
```

This output is meant to protect both sides: the user gets a plain answer, and
the coder gets a mode boundary before using tools.

## User-Facing Explanation Shape

The coder should translate RepoKernel into user value:

```text
RepoKernel helps a project become easier for future AI sessions and human
maintainers to reenter. It records where the project is, which sources matter,
what is safe to do, what changed, what should not be repeated and what the next
useful action is.
```

Then adapt to the user's context:

```text
For your software repo:
  it can preserve current state, important files, test expectations and safe
  next action across AI coding sessions.

For your AI/RAG/model work:
  it can preserve source lineage, model/data assumptions, evaluation notes and
  failure memory.

For your business or operations folder:
  it can preserve decisions, offers, evidence, follow-ups and boundaries.

For your agentic system:
  it can make agent authority, read/write boundaries, receipts and memory
  deltas explicit before automation grows.
```

## Runtime-Specific Guidance

### Codex-Like Coding Agent

```text
Best first action:
  read docs, inspect git state, run no-write audit if authorized, stage outside
  target only after user consent.

Useful output:
  setup report plus proposed first Project Kernel layer.
```

### Claude Code-Like Assistant

```text
Best first action:
  summarize value and limits, ask for explicit read/write boundaries, use
  Todo/plan only after source authority is clear.

Useful output:
  plain-language decision memo for the user and a small file proposal.
```

### OpenCode Or Lightweight CLI Agent

```text
Best first action:
  stay simple: read README and guides, avoid complex boot assumptions, propose
  a read-only folder assessment before running commands.

Useful output:
  checklist of whether RepoKernel fits the project.
```

### Custom Agentic System

```text
Best first action:
  map capabilities and authority first. Separate read, propose, stage, write,
  publish and automate.

Useful output:
  adapter contract showing which RepoKernel modes are safe in that system.
```

## Fit Decision

After the first evaluation, choose one:

```text
not_needed:
  The project does not suffer from continuity, authority or reentry problems.

use_docs_only:
  The user only needs the idea or a lightweight checklist.

read_only_assessment:
  The coder should inspect an approved repo/folder and produce a setup report.

staged_project_kernel_preview:
  The project would benefit from generated continuity files, but only as an
  external staged preview.

defer:
  The project is too sensitive, authority is unclear or the coder cannot verify
  safe boundaries.
```

## First Report Template

Use this report before asking for any stronger action:

```text
repo_or_project:
active_runtime:
mode_used:
what_the_user_asked:
what_repokernel_could_help_with:
what_repokernel_should_not_do_here:
missing_context:
recommended_mode:
safe_next_step:
approval_needed:
fit_result: useful | not_needed | defer
```

## Consent Questions

Ask only what affects the next action:

```text
Do you want only an explanation, or should I evaluate a specific repo/folder?
If a repo/folder is involved, may I read it locally?
Should I stay read-only and produce a setup report first?
If a staged preview is useful, where should the external review output go?
Are there files, secrets, client data or private notes I must not read?
```

## Do Not Collapse Roles

Keep the roles separate:

```text
user:
  owns intent, consent, risk tolerance and final approval.

coder/agent:
  explains, reads only what is authorized, evaluates fit, proposes next steps
  and produces receipts.

RepoKernel:
  provides project-kernel structure, no-write diagnostics, staged proposal and
  continuity rules.

target project:
  remains authoritative. Existing files are not overwritten by assumption.
```

## Best First Response Pattern

When the user asks "what is useful in RepoKernel?", answer like this:

```text
RepoKernel is mainly useful for the coder/AI layer: it gives a project a
readable continuity structure so future assistants know where they are, what
sources matter, what they may do and what the next safe action is.

For you as the user, the value is less repeated explanation, safer AI sessions
and a clearer handoff between tools such as Codex, Claude Code, OpenCode or a
custom agent.

I should not clone, inspect private folders or run diagnostics yet. The best
first step is to decide whether you want an explanation only, a read-only
assessment of a specific repo/folder, or a staged preview outside the target.
```

This response gives the user something understandable and gives the coder the
next operating mode without pretending that RepoKernel is already installed or
authorized.
