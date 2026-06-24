# Minimal Project Example

SeedSpec:

```json
{
  "schema": "repokernel.seed-spec.v1",
  "seed_id": "writing-tool-seed",
  "project": {
    "name": "Writing Tool",
    "intent": "Preserve AI-assisted writing continuity",
    "product": "A writing project kernel"
  },
  "target": {
    "mode": "new_repository",
    "path": "WritingTool"
  },
  "readiness_level": "L1",
  "authority_mode": "propose"
}
```

GenerationPlan dry run:

```text
AGENTS.md -> create
CURRENT_STATE.md -> create
process/FIRST_PACKET.md -> create
README.md -> create
sources/bootstrap/SOURCE_ATLAS_v1.0.md -> create
skills/writing-tool-semantic-kernel/SKILL.md -> create
```

Activation remains blocked until generated files exist and audit passes.
