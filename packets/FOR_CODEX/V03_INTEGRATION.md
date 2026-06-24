# RepoKernel v0.3 Integration Packet

Status: superseded during Phase 0 cleanup.

Superseded by:

```text
packets/FOR_CODEX/REPOKERNEL_FINAL_IMPLEMENTATION_PACKAGE_2026-06-23.md
packets/FOR_CODEX/GPT_PRO_REPOKERNEL_FINAL_ARCHITECTURE_AND_CODEX_PACKET_2026-06-23.md
packets/FOR_CODEX/GPT_PRO_REPOKERNEL_FINAL_ARCHITECTURE_APPENDIX_2026-06-23.md
```

This packet is retained for provenance only. It is not current implementation
authority.

## Objective

Connect the committed `scripts/repokernel_core.py` library to the existing command and validation surfaces.

## Required Changes

1. Add a command wrapper accepting `--path`, `--name`, `--mission`, `--level`, `--dry-run`, `--merge` and `--json`.
2. Route `scaffold_repokernel_project.py` and `scaffold_skill_repo.py` through the shared core.
3. Extend the repository audit with an `operational-seed` profile and L3 checks.
4. Add regression checks for L1, L2, L3, invalid identifiers, empty files, dry-run and merge conflicts.
5. Confirm that a generated skill remains draft until it has a substantive example and passing validation record.
6. Run the source audit and record the result under `process/evidence/`.

## Invariants

- Existing files are not overwritten silently.
- A conflict prevents partial application.
- L3 is optional.
- Project-local executable additions require trust review.
- The initial L3 mode remains proposal-only.

## Validation

```bash
python -m unittest discover -s tests -v
python scripts/audit_repokernel_project.py --path . --profile repokernel-source --json
git diff --check
```
