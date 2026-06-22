# RepoKernel

AI-readable repositories for long-running projects.

RepoKernel is a repository pattern for projects that need to be continued by AI tools over time. It helps the next AI session understand what the project is, where the current state lives, which sources matter, what changed, what should not be followed, what can be changed freely, what needs confirmation, and what the next useful move is.

RepoKernel turns a repository into a semantic context kernel: a structure that supports operational context awareness, source lineage and iterative improvement.

## Search Summary

RepoKernel helps developers, researchers, writers, product teams and AI agencies build context-aware GitHub repositories for Codex, Claude Code, OpenCode, ChatGPT projects and other AI coding or writing agents.

Use RepoKernel when you need:

- AI-readable repository structure;
- project reentry without starting from zero;
- `AGENTS.md` and `CURRENT_STATE.md` templates;
- semantic-kernel skills for long-running projects;
- memory-delta rules instead of raw chat history;
- audit and scaffold scripts for agentic workflows;
- a promotion path from local skill to reusable repository pattern.

## The Problem

Most AI-assisted work loses context between sessions.

Chats contain decisions, corrections, assumptions and intent. The next model often sees only files, or has to reconstruct the project from scattered memory. A normal repository stores artifacts; it does not always explain how those artifacts should be read, continued or improved.

RepoKernel adds that missing layer.

## What It Adds

```text
AGENTS.md
CURRENT_STATE.md
sources/bootstrap/
skills/<project>-semantic-kernel/
process/FIRST_PACKET.md
templates/
audit and scaffold scripts
```

The repository becomes readable as a working field, not only as a file tree.

## Repository Pattern

RepoKernel is designed for:

- context engineering;
- AI workflow continuity;
- agentic coding;
- AI-assisted writing and research;
- repository bootstrapping;
- semantic project memory;
- skill and meta-skill lifecycle management.

## Who It Is For

RepoKernel can be used by developers, writers, researchers, product teams, consultants and agencies using AI tools across long-running projects.

It works with coding-agent environments such as Codex, OpenCode and Claude Code, and with ChatGPT or other systems that can read a GitHub repository or similar project source.

It is not only for code. A repository can become a semantic support medium for any project that must preserve context, intent and direction across tools, devices, media and sessions.

## Core Loop

```text
state -> sources -> semantic kernel -> packet -> action -> delta -> new state
```

This loop helps the project preserve useful learning without accumulating raw chat history.

## Quick Start

Audit an existing repository:

```bash
python scripts/audit_repokernel_project.py --path /path/to/repo
```

Create a minimal RepoKernel structure in a new directory:

```bash
python scripts/scaffold_repokernel_project.py --path /path/to/MyProject --name MyProject --mission "The mission of this project"
```

Create a repository-shaped skill project:

```bash
python scripts/scaffold_skill_repo.py --path /path/to/my-skill --name my-skill --mission "What this skill helps an AI do"
```

## Operational Awareness

RepoKernel uses "context awareness" in an operational sense. It is not a claim about consciousness. It means that a project can expose enough state, sources, boundaries and next actions for a future AI session to reenter responsibly.

## Status

Starter repository. The first release goal is a public-safe set of templates, audit scripts, a minimal example and internal meta-skills for creating and promoting repository-aware skills.

## Keywords

```text
ai-readable repositories, context engineering, agentic workflow, Codex, Claude Code,
OpenCode, ChatGPT GitHub, AGENTS.md, CURRENT_STATE.md, semantic kernel,
AI project continuity, repository bootstrap, memory delta, skill lifecycle
```
