# Review Triage — RK-RVW-20260625-01

Status: proposed for operator acceptance  
Source review: `process/reports/REPOKERNEL_FULL_SURFACE_AND_PILOT_REVIEW_2026-06-25.md`

| Finding | Disposition | Rationale | Target | Acceptance |
| --- | --- | --- | --- | --- |
| JSON Schema execution and validator parity | accept | Current tests only parse schema JSON; contracts can drift | core completion | valid/invalid fixture parity suite passes |
| Reviewed/version-bound SeedSpec | accept | Planner must not treat an unreviewed spec as accepted intent | core completion | unaccepted spec blocked; hashes/review required |
| TargetSnapshot and content-aware retrofit | accept | Existing-path lists cannot prove stale/no-change behavior | core completion | identical content -> leave_unchanged; stale snapshot blocked |
| Opaque extension semantics | adapt | Preserve extensions but remove authority blacklist as the main defense | core completion | planner behavior unchanged by unknown extension payloads |
| Disclosure profiles | accept | Public labels are safer, but project fields still need policy | core completion | deny-by-default public guide fixture passes |
| Canonical `.repokernel/` project audit | accept | Current audit is root-first and source audit is partly self-attested | core completion | project-kernel profile passes/fails on real canonical fixtures |
| Clean package/CLI proof | accept | Console entry point exists but installed-wheel path is unproven | core completion | clean venv install/smoke/uninstall passes |
| Hosted CI | defer | Required before public experimental use, not required to prepare private pilot | pre-public gate | workflow tied to commit passes supported Python matrix |
| Reference Seed reproducibility | accept | Core ontology depends on reproducible Reference Seeds | completion gate | verify-dist passes byte-for-byte/normalized comparison |
| Version-locked private pilot | accept | Provides the missing real existing-kernel no-write fixture | pilot completion | before/after tree hashes equal; independent evaluation complete |
| Runtime/L3 implementation | reject for current cycle | Outside L0-L2 and safety evidence | deferred | separate future review required |
| Apply command | reject for current cycle | Snapshot/rollback transaction not yet implemented | deferred | separate apply safety gate required |
| Seed/THIA/Lab promotion | reject for current cycle | Core and pilot evidence incomplete | deferred | stable compatibility and promotion packet later |
| Public tester request | defer | Distribution verdict remains private-pilot-first | post-pilot | accurate public scope plus reviewer feedback |
| `jsonschema` dependency selection | needs_verification | Actual Draft 2020-12 validation is needed; dependency policy must be explicit | core completion | operator accepts dependency and version pin |
| Pilot use of private relationship context | reject | Technical evidence must remain neutral | pilot boundary | withheld source fixture has zero leakage |

## Operator Decision

```text
accepted_items:
adapted_items:
deferred_items:
rejected_items:
needs_verification_decisions:
authority_granted:
accepted_at:
```

Codex must not begin implementation until this section or an equivalent operator
decision explicitly accepts the active scope.
