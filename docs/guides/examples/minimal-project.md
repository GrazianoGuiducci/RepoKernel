# Minimal Project Example

SeedSpec fixture:

```text
examples/minimal/seed-spec.json
```

Equivalent JSON:

```json
{
  "schema": "repokernel.seed-spec.v1",
  "seed_id": "minimal-project-seed",
  "project": {
    "name": "Minimal Project",
    "intent": "Preserve AI-assisted project continuity",
    "product": "A minimal project kernel"
  },
  "target": {
    "mode": "new_repository",
    "path": "MinimalProject"
  },
  "readiness_level": "L1",
  "authority_mode": "propose"
}
```

Run:

```bash
PYTHONPATH=src python -m repokernel.cli validate-spec --kind seed-spec --input examples/minimal/seed-spec.json
PYTHONPATH=src python -m repokernel.cli validate-bundle --source-manifest examples/minimal/source-manifest.json --project-model examples/minimal/project-model.json --seed-spec examples/minimal/seed-spec.json
PYTHONPATH=src python -m repokernel.cli plan --seed-spec examples/minimal/seed-spec.json --source-manifest examples/minimal/source-manifest.json --project-model examples/minimal/project-model.json > plan.json
PYTHONPATH=src python -m repokernel.cli guides --seed-spec examples/minimal/seed-spec.json --source-manifest examples/minimal/source-manifest.json
```

GenerationPlan proposal:

```text
AGENTS.md -> create
.repokernel/state/CURRENT_STATE.md -> create
.repokernel/packets/FIRST_PACKET.md -> create
README.md -> create
.repokernel/sources/SOURCE_ATLAS.md -> create
.repokernel/skills/minimal-project-semantic-kernel/SKILL.md -> create
```

Optional review staging:

```bash
PYTHONPATH=src python -m repokernel.cli stage --plan plan.json --output-dir ./repokernel-staging
```

Activation remains blocked until generated files exist and audit passes.
