"""Validate linked SourceManifest, ProjectModel and SeedSpec bundles."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from .canonical import canonical_hash
from .models import validate_project_model, validate_seed_spec, validate_source_manifest
from .schema_validation import schema_errors_as_text
from .version import package_version


@dataclass(frozen=True)
class BundleValidation:
    valid: bool
    errors: list[str]
    provenance: dict[str, Any]


def validate_bundle(
    source_manifest: dict[str, Any],
    project_model: dict[str, Any],
    seed_spec: dict[str, Any],
) -> BundleValidation:
    errors: list[str] = []
    errors.extend(_contract_errors("source-manifest", source_manifest, validate_source_manifest(source_manifest)))
    errors.extend(_contract_errors("project-model", project_model, validate_project_model(project_model)))
    errors.extend(_contract_errors("seed-spec", seed_spec, validate_seed_spec(seed_spec)))

    source_hash = canonical_hash(source_manifest)
    model_hash = canonical_hash(project_model)
    if seed_spec.get("source_manifest_hash") != source_hash:
        errors.append("seed_spec.source_manifest_hash does not match SourceManifest canonical hash")
    if seed_spec.get("project_model_hash") != model_hash:
        errors.append("seed_spec.project_model_hash does not match ProjectModel canonical hash")

    source_ids = {
        source.get("source_id")
        for source in source_manifest.get("sources", [])
        if isinstance(source, dict) and isinstance(source.get("source_id"), str)
    }
    for ref in _project_model_refs(project_model):
        if ref not in source_ids:
            errors.append(f"project_model source reference not present in SourceManifest: {ref}")

    running_version = package_version()
    required_version = seed_spec.get("compiler_compatibility", {}).get("package_version")
    if required_version != running_version:
        errors.append(f"compiler package version mismatch: seed requires {required_version}, running {running_version}")

    review = seed_spec.get("review", {})
    if not isinstance(review, dict) or review.get("status") != "accepted":
        errors.append("seed_spec review.status must be accepted")

    return BundleValidation(
        valid=not errors,
        errors=errors,
        provenance={
            "schema": "repokernel.bundle-validation.v1",
            "package_version": running_version,
            "source_manifest_hash": source_hash,
            "project_model_hash": model_hash,
            "seed_spec_hash": canonical_hash(seed_spec),
            "review_cycle": review.get("review_cycle") if isinstance(review, dict) else None,
        },
    )


def _contract_errors(kind: str, value: dict[str, Any], python_errors: list[str]) -> list[str]:
    errors = [f"{kind}: {error}" for error in python_errors]
    errors.extend(f"{kind}: schema: {error}" for error in schema_errors_as_text(kind, value))
    return errors


def _project_model_refs(model: dict[str, Any]) -> set[str]:
    refs: set[str] = set()
    global_refs = model.get("source_refs", [])
    if isinstance(global_refs, list):
        refs.update(ref for ref in global_refs if isinstance(ref, str))
    assertions = model.get("assertions", [])
    if isinstance(assertions, list):
        for assertion in assertions:
            if not isinstance(assertion, dict):
                continue
            for ref in assertion.get("source_refs", []):
                if isinstance(ref, str):
                    refs.add(ref)
    conflicts = model.get("source_conflicts", [])
    if isinstance(conflicts, list):
        for conflict in conflicts:
            if not isinstance(conflict, dict):
                continue
            for ref in conflict.get("source_refs", []):
                if isinstance(ref, str):
                    refs.add(ref)
    return refs
