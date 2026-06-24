# Local Validation

Date: 2026-06-24

Repository-hosted validation: passed

## Phase 1 P0 Hardening Tests

Command:

```powershell
$env:PYTHONPATH='src'
python -m unittest discover -s tests/unit -v
```

Result:

```text
Ran 12 tests
OK
```

Covered behavior:

1. Canonical JSON order is stable.
2. Non-finite JSON numbers are rejected.
3. Namespaced extensions round-trip and cannot raise authority.
4. Private and non-public-guide sources are excluded from guide output.
5. Dry-run writes nothing.
6. Existing root `AGENTS.md` becomes a reviewable proposal, not an overwrite.
7. Plans use the `.repokernel/` control plane.
8. Same SeedSpec produces the same plan metadata and item hashes.
9. Unsafe Windows drive-style paths are rejected.
10. Contract validators accept minimal valid contracts.
11. Schema files parse as JSON.
12. SeedSpec validation requires `seed_id` and safe target paths.

## Historical Note

The previous 2026-06-23 overlay validation remains historical evidence only.
The active evidence for repository-hosted Phase 1 work is the command above plus
the current audit and inventory reports.
