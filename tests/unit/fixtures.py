from __future__ import annotations

import copy

from repokernel.canonical import canonical_hash


def source_manifest() -> dict:
    return {
        "schema": "repokernel.source-manifest.v1",
        "sources": [
            {
                "source_id": "minimal-readme",
                "path_or_origin": "examples/minimal/README.md",
                "authority": "example",
                "privacy": "public",
                "freshness": "current",
                "instruction_handling": "data_only",
                "public_label": "Minimal example README",
                "used_for": ["public_guide"],
            }
        ],
    }


def project_model() -> dict:
    return {
        "schema": "repokernel.project-model.v1",
        "identity": {"name": "Minimal Project"},
        "mission": "Preserve AI-assisted project continuity",
        "product_or_result": "A minimal project kernel",
        "source_refs": ["minimal-readme"],
        "assertions": [
            {
                "id": "identity",
                "status": "verified",
                "text": "The project is named Minimal Project.",
                "source_refs": ["minimal-readme"],
            }
        ],
        "boundaries": {"authority": "proposal_only", "writes": "staging_only"},
        "unknowns": [],
    }


def seed_spec() -> dict:
    manifest = source_manifest()
    model = project_model()
    return {
        "schema": "repokernel.seed-spec.v1",
        "version": "repokernel.seed-spec.v1",
        "seed_id": "minimal-project-seed",
        "source_manifest_hash": canonical_hash(manifest),
        "project_model_hash": canonical_hash(model),
        "canonical_namespace": ".repokernel",
        "project": {
            "name": "Minimal Project",
            "intent": "Preserve AI-assisted project continuity",
            "product": "A minimal project kernel",
        },
        "target": {"mode": "new_repository", "path": "MinimalProject"},
        "readiness_level": "L1",
        "authority_mode": "propose",
        "review": {
            "status": "accepted",
            "accepted_by_role": "operator",
            "accepted_at": "2026-06-25",
            "review_cycle": "RK-RVW-20260625-01",
        },
        "compiler_compatibility": {
            "package_version": "0.3.0.dev0",
            "contract_versions": {"seed_spec": "repokernel.seed-spec.v1"},
        },
        "file_plan_policy": "stage_only",
        "validation_plan": ["validate-spec", "validate-bundle", "plan", "stage"],
        "disclosure": {"public": {"name": True, "intent": True, "product": True}},
    }


def seed_with(**updates) -> dict:
    spec = copy.deepcopy(seed_spec())
    for key, value in updates.items():
        spec[key] = value
    return spec
