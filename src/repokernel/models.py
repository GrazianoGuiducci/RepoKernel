"""Minimal RepoKernel contract validation."""
from __future__ import annotations

from typing import Any

from .canonical import validate_namespaced_extensions
from .paths import normalize_relative_path


VALID_LEVELS = {"L0", "L1", "L2", "L3"}
VALID_MODES = {"new_repository", "existing_repository_retrofit"}
VALID_AUTHORITY = {"none", "read", "propose", "proposal_only"}
VALID_PRIVACY = {"public", "internal", "private", "withheld"}
VALID_SOURCE_AUTHORITY = {"operator", "maintainer", "repo", "example", "external_review", "generated"}
VALID_FRESHNESS = {"current", "stale", "historical", "unknown"}
VALID_INSTRUCTION_HANDLING = {"data_only", "trusted_instruction", "operator_instruction"}
VALID_REVIEW_STATUS = {"accepted"}
VALID_FILE_PLAN_POLICY = {"stage_only", "proposal_only"}


def require_object(value: Any, name: str) -> dict[str, Any]:
    if not isinstance(value, dict):
        raise ValueError(f"{name} must be an object")
    return value


def validate_source_manifest(manifest: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    require_object(manifest, "SourceManifest")
    if manifest.get("schema") != "repokernel.source-manifest.v1":
        errors.append("schema must be repokernel.source-manifest.v1")
    sources = manifest.get("sources")
    if not isinstance(sources, list) or not sources:
        errors.append("sources must be a non-empty list")
    else:
        seen_ids: set[str] = set()
        for index, source in enumerate(sources):
            if not isinstance(source, dict):
                errors.append(f"sources[{index}] must be an object")
                continue
            for key in ("source_id", "authority", "privacy", "used_for"):
                if key not in source:
                    errors.append(f"sources[{index}] missing {key}")
            if "source_id" in source and not _non_empty_string(source.get("source_id")):
                errors.append(f"sources[{index}].source_id must be a non-empty string")
            elif "source_id" in source:
                source_id = source["source_id"]
                if source_id in seen_ids:
                    errors.append(f"sources[{index}].source_id duplicate")
                seen_ids.add(source_id)
            if "authority" in source and source.get("authority") not in VALID_SOURCE_AUTHORITY:
                errors.append(f"sources[{index}].authority invalid")
            if "privacy" in source and source.get("privacy") not in VALID_PRIVACY:
                errors.append(f"sources[{index}].privacy invalid")
            if source.get("freshness", "unknown") not in VALID_FRESHNESS:
                errors.append(f"sources[{index}].freshness invalid")
            if source.get("instruction_handling", "data_only") not in VALID_INSTRUCTION_HANDLING:
                errors.append(f"sources[{index}].instruction_handling invalid")
            if "used_for" in source and not isinstance(source.get("used_for"), list):
                errors.append(f"sources[{index}].used_for must be a list")
            if source.get("privacy") != "public" and source.get("public_label"):
                errors.append(f"sources[{index}].public_label requires privacy public")
    errors.extend(validate_namespaced_extensions(manifest.get("extensions")))
    return errors


def validate_project_model(model: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    require_object(model, "ProjectModel")
    if model.get("schema") != "repokernel.project-model.v1":
        errors.append("schema must be repokernel.project-model.v1")
    for key in ("identity", "mission", "product_or_result", "source_refs", "boundaries", "unknowns"):
        if key not in model:
            errors.append(f"missing {key}")
    errors.extend(validate_namespaced_extensions(model.get("extensions")))
    return errors


def validate_seed_spec(spec: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    require_object(spec, "SeedSpec")
    if spec.get("schema") != "repokernel.seed-spec.v1":
        errors.append("schema must be repokernel.seed-spec.v1")
    if spec.get("version") != "repokernel.seed-spec.v1":
        errors.append("version must be repokernel.seed-spec.v1")
    if not _non_empty_string(spec.get("seed_id")):
        errors.append("seed_id is required")
    for key in ("source_manifest_hash", "project_model_hash"):
        if not _hex_sha256(spec.get(key)):
            errors.append(f"{key} must be a sha256 hex string")
    if spec.get("canonical_namespace") != ".repokernel":
        errors.append("canonical_namespace must be .repokernel")
    project = spec.get("project")
    target = spec.get("target")
    if not isinstance(project, dict):
        errors.append("project must be an object")
    else:
        for key in ("name", "intent", "product"):
            if not _non_empty_string(project.get(key)):
                errors.append(f"project.{key} must be a non-empty string")
    if not isinstance(target, dict):
        errors.append("target must be an object")
    else:
        if target.get("mode") not in VALID_MODES:
            errors.append("target.mode must be new_repository or existing_repository_retrofit")
        if "path" in target:
            try:
                normalize_relative_path(target["path"])
            except ValueError as exc:
                errors.append(f"target.path invalid: {exc}")
    if spec.get("readiness_level") not in VALID_LEVELS:
        errors.append("readiness_level must be L0, L1, L2 or L3")
    if spec.get("authority_mode", "propose") not in VALID_AUTHORITY:
        errors.append("authority_mode cannot exceed propose in Phase 1")
    review = spec.get("review")
    if not isinstance(review, dict):
        errors.append("review must be an object")
    else:
        if review.get("status") not in VALID_REVIEW_STATUS:
            errors.append("review.status must be accepted")
        for key in ("accepted_by_role", "accepted_at", "review_cycle"):
            if not _non_empty_string(review.get(key)):
                errors.append(f"review.{key} must be a non-empty string")
    compiler_compatibility = spec.get("compiler_compatibility")
    if not isinstance(compiler_compatibility, dict):
        errors.append("compiler_compatibility must be an object")
    elif not _non_empty_string(compiler_compatibility.get("package_version")):
        errors.append("compiler_compatibility.package_version must be a non-empty string")
    if spec.get("file_plan_policy") not in VALID_FILE_PLAN_POLICY:
        errors.append("file_plan_policy must be stage_only or proposal_only")
    if not isinstance(spec.get("validation_plan"), list) or not spec.get("validation_plan"):
        errors.append("validation_plan must be a non-empty list")
    errors.extend(validate_namespaced_extensions(spec.get("extensions")))
    return errors


def validate_generation_plan(plan: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    require_object(plan, "GenerationPlan")
    if plan.get("schema") != "repokernel.generation-plan.v1":
        errors.append("schema must be repokernel.generation-plan.v1")
    for key in ("plan_id", "compiler_version", "target_snapshot_hash", "before_hash", "after_hash", "apply_policy"):
        if not _non_empty_string(plan.get(key)):
            errors.append(f"{key} must be a non-empty string")
    if plan.get("apply_policy") != "stage_only":
        errors.append("apply_policy must be stage_only")
    items = plan.get("items")
    if not isinstance(items, list):
        errors.append("items must be a list")
    else:
        for index, item in enumerate(items):
            if not isinstance(item, dict):
                errors.append(f"items[{index}] must be an object")
                continue
            if item.get("action") not in {"create", "leave_unchanged", "propose_update", "conflict", "withhold"}:
                errors.append(f"items[{index}].action invalid")
            if item.get("action") in {"create", "propose_update"} and item.get("authority_effect") != "none":
                errors.append(f"items[{index}] must not carry authority effect")
            if item.get("authority_effect") != "none":
                errors.append(f"items[{index}].authority_effect must be none")
            if "path" in item:
                try:
                    normalize_relative_path(item["path"])
                except ValueError as exc:
                    errors.append(f"items[{index}].path invalid: {exc}")
    errors.extend(validate_namespaced_extensions(plan.get("extensions")))
    return errors


def validate_activation_report(report: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    require_object(report, "ActivationReport")
    if report.get("schema") != "repokernel.activation-report.v1":
        errors.append("schema must be repokernel.activation-report.v1")
    if report.get("state") not in {"planned", "generated", "validated", "active", "blocked"}:
        errors.append("state is invalid")
    checks = report.get("checks")
    if not isinstance(checks, list):
        errors.append("checks must be a list")
    if report.get("state") == "active":
        if not checks:
            errors.append("active ActivationReport requires checks")
        elif any(not isinstance(check, dict) or check.get("ok") is not True for check in checks):
            errors.append("active ActivationReport requires every check ok")
    errors.extend(validate_namespaced_extensions(report.get("extensions")))
    return errors


def validate_skill_registry(registry: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    require_object(registry, "SkillRegistry")
    if registry.get("schema") not in {"repokernel.skill-registry.v1", "repokernel.skill-registry.v2"}:
        errors.append("schema must be repokernel.skill-registry.v1 or v2")
    if not isinstance(registry.get("skills"), list):
        errors.append("skills must be a list")
    errors.extend(validate_namespaced_extensions(registry.get("extensions")))
    return errors


def validate_target_snapshot(snapshot: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    require_object(snapshot, "TargetSnapshot")
    if snapshot.get("schema") != "repokernel.target-snapshot.v1":
        errors.append("schema must be repokernel.target-snapshot.v1")
    if not _non_empty_string(snapshot.get("target_snapshot_id")):
        errors.append("target_snapshot_id must be a non-empty string")
    if not _non_empty_string(snapshot.get("tree_hash")):
        errors.append("tree_hash must be a non-empty string")
    entries = snapshot.get("entries")
    if not isinstance(entries, list):
        errors.append("entries must be a list")
    else:
        for index, entry in enumerate(entries):
            if not isinstance(entry, dict):
                errors.append(f"entries[{index}] must be an object")
                continue
            if not _non_empty_string(entry.get("path")):
                errors.append(f"entries[{index}].path must be a non-empty string")
            if entry.get("kind") not in {"file", "directory", "symlink", "other"}:
                errors.append(f"entries[{index}].kind invalid")
    errors.extend(validate_namespaced_extensions(snapshot.get("extensions")))
    return errors


def _non_empty_string(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _hex_sha256(value: Any) -> bool:
    return isinstance(value, str) and len(value) == 64 and all(ch in "0123456789abcdef" for ch in value.lower())
