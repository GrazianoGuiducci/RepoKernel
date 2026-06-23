# Post-Phase-0 Schema Horizon

Date: 2026-06-23  
Status: review before Phase 1; not part of Phase 0 implementation

## Purpose

Prevent the first stable schemas from blocking high-value future capabilities while keeping L0-L2 narrow and testable.

Read after Phase 0 is accepted and before Phase 1 schema files are frozen:

```text
docs/possibility-horizon.md
packets/FOR_CODEX/GPT_PRO_REPOKERNEL_FINAL_ARCHITECTURE_AND_CODEX_PACKET_2026-06-23.md
packets/FOR_CODEX/GPT_PRO_REPOKERNEL_FINAL_ARCHITECTURE_APPENDIX_2026-06-23.md
```

## Required Decision

For each v1 contract, decide which future dimensions are:

```text
core required
core optional
reserved namespaced extension
post-v1 only
```

## Dimensions To Preserve

```text
lineage
lifecycle
authority_mode
operational_mode
scale
projections
evaluation_refs
disclosure_profiles
capability_requirements
federation_links
event_bindings
distribution_metadata
extensions
```

## Recommended Minimum

Every canonical object should have stable identity and versioning.

`SeedSpec` should support optional:

```json
{
  "lineage": {
    "parent_seed_ids": [],
    "fork_reason": null
  },
  "lifecycle": {
    "state": "genesis"
  },
  "authority_mode": "propose",
  "extensions": {}
}
```

Other future dimensions may live under namespaced `extensions` until promoted into a later schema version.

## Invariants

- Unknown extensions round-trip without data loss.
- Unknown extensions do not affect planning, writes or authority.
- Extension keys are namespaced.
- Canonical hashes include extension content unless an explicit non-semantic field policy excludes it.
- Core validation remains deterministic.
- No future capability is implemented merely because its field is preserved.

## Tests To Add In Phase 1

1. Unknown namespaced extension validates when allowed.
2. Extension survives parse, canonical serialization and re-emission unchanged.
3. Extension cannot raise authority or add a write action.
4. Two objects differing only in semantic extension content have different canonical hashes.
5. Non-semantic build metadata follows an explicit hashing policy.
6. Invalid lineage cycles are rejected when lineage validation is enabled.

## Boundary

Do not use this packet to expand Phase 1 into projections, federation, events, runtime or marketplace implementation.

The task is only to preserve the semantic space required for later versions.
