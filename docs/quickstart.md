# Quickstart

## Audit An Existing Repository

```bash
python scripts/audit_repokernel_project.py --path /path/to/repo
```

Read the missing layers and add only what improves reentry.

## Create A Minimal RepoKernel Project

```bash
python scripts/scaffold_repokernel_project.py --path /path/to/MyProject --name MyProject --mission "The mission of this project"
```

This creates:

```text
AGENTS.md
CURRENT_STATE.md
sources/bootstrap/PROJECT_INSTRUCTIONS_v1.0.txt
sources/bootstrap/SOURCE_ATLAS_v1.0.md
process/FIRST_PACKET.md
skills/<project>-semantic-kernel/SKILL.md
```

## Create A Skill Repository

```bash
python scripts/scaffold_skill_repo.py --path /path/to/my-skill --name my-skill --mission "What this skill helps an AI do"
```

Use this when a reusable capability should live as a small repository rather than as an unstructured prompt.

