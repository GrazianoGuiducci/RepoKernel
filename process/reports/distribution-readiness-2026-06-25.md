# Distribution Readiness Verdict

date: 2026-06-25
updated: 2026-06-26
status: experimental_diagnostic_repo_ok_public_claims_limited

## Verdict

```text
experimental_diagnostic_repo_ok_public_claims_limited
```

RepoKernel now has enough evidence to be visible as an experimental diagnostic
repository, but not enough proof for production, installer, runtime or broad
non-technical public-alpha claims.

## Verified

```text
python -m pytest tests/unit -q
  47 passed

PYTHONPATH=src python -m repokernel.cli validate-spec --kind seed-spec --input examples/minimal/seed-spec.json
  valid: true

PYTHONPATH=src python -m repokernel.cli validate-bundle --source-manifest examples/minimal/source-manifest.json --project-model examples/minimal/project-model.json --seed-spec examples/minimal/seed-spec.json
PYTHONPATH=src python -m repokernel.cli plan --seed-spec examples/minimal/seed-spec.json --source-manifest examples/minimal/source-manifest.json --project-model examples/minimal/project-model.json > plan.json
PYTHONPATH=src python -m repokernel.cli stage --plan plan.json --output-dir <temp-dir>
  target_writes_performed: []
  staged files include .repokernel/state/CURRENT_STATE.md

PYTHONPATH=src python -m repokernel.cli verify-dist --seed-spec specs/reference/starter-l1.seed.json --dist-dir dist/reference/starter-l1
  valid: true

PYTHONPATH=src python -m repokernel.cli audit --path . --profile repokernel-source
  ready: true

git diff --check
  no errors

AIMAIL A2 semantic retrofit replay
  before_hash == after_hash
  target_writes_performed: []
  semantic staged state/source content improved from ProjectModel
```

## Safe To Show Privately

```text
README.md
docs/quickstart.md
docs/guides/cli-reference.md
docs/guides/operational-procedure.md
docs/guides/private-review-brief.md
docs/feedback.md
examples/minimal/seed-spec.json
examples/minimal/source-manifest.json
```

## Still Missing Before Broad Public Tester Post

```text
hosted CI result after GitHub Actions workflow activation;
one additional public/non-sensitive repository proof, if selected and based on
a current approved target;
human reviewer feedback on the current quickstart and no-write procedure;
clear decision on whether to include the GitHub link in the LinkedIn post;
confirmation that no public text implies installer, apply, runtime or
autonomous repo modification readiness.
```

Reviewer instruction block:

```text
docs/guides/private-review-brief.md
docs/guides/private-pilot-instructions.md
```

## Boundary

No LinkedIn post, broad public tester request, external repo write, Seed
promotion, THIA/Lab integration or runtime activation is authorized by this
verdict.

## Next Action

The CI workflow has been prepared from `docs/ci/github-actions-ci.yml` and is
being activated under `.github/workflows/ci.yml`. After the hosted CI run is
visible and passing, prepare a controlled public-safe overview and optional
one-page HTML explanation. A new repository-observation proof requires a
separate approved current target.
