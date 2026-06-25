# Private Review Brief

Use this brief with one trusted reviewer before any public tester request.

## What You Are Looking At

RepoKernel is a reviewable planner for AI-assisted project continuity.

In this phase it can:

```text
validate a project SeedSpec;
inspect a repository;
create a proposed GenerationPlan;
stage proposed files in a separate review directory;
show guide output from approved public/source manifests.
```

It is not an installer yet. It does not apply files to the target repository.

## What To Test First

Run the smoke path from a RepoKernel checkout:

```bash
PYTHONPATH=src python -m repokernel.cli validate-spec --kind seed-spec --input examples/minimal/seed-spec.json
PYTHONPATH=src python -m repokernel.cli plan --seed-spec examples/minimal/seed-spec.json > plan.json
PYTHONPATH=src python -m repokernel.cli stage --plan plan.json --output-dir ./repokernel-staging
PYTHONPATH=src python -m repokernel.cli guides --seed-spec examples/minimal/seed-spec.json --source-manifest examples/minimal/source-manifest.json
```

Expected result:

```text
the SeedSpec validates;
plan.json is created in the RepoKernel checkout;
proposed files are staged under ./repokernel-staging;
no files are written to the target path named by the SeedSpec.
```

## Optional Repository Observation

Only use a public or non-sensitive repository that you are allowed to inspect.

Run:

```bash
PYTHONPATH=src python -m repokernel.cli inspect --path /path/to/project
```

Use the result only to discuss what RepoKernel should propose. Do not copy
private logs, secrets, `.env` files, client material or full source dumps.

## Feedback I Need

Short answers are enough:

```text
Which command was unclear?
Did staging feel safe?
Was the no-write boundary obvious?
Were the proposed files understandable?
What example would make this easier to test?
What did you expect that was not there?
```

Use `docs/feedback.md` if you want the longer feedback shape.

## Stop Rule

Stop the review if:

```text
you expect an apply/install command;
the target repository contains sensitive material;
a command appears to write outside the explicit staging directory;
feedback would require sharing private project details.
```

## Boundary

This review does not authorize public posting, repository writes, pull
requests, Seed/THIA/Lab integration or runtime activation.

