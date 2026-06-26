"""RepoKernel Phase 1 command line interface."""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path
from typing import Any, Callable

from .audit import PROFILES, audit, inspect_repository, report_as_json
from .bundle import validate_bundle
from .canonical import canonical_hash
from .guide_model import build_guides
from .models import (
    validate_activation_report,
    validate_generation_plan,
    validate_project_model,
    validate_seed_spec,
    validate_skill_registry,
    validate_source_manifest,
    validate_target_snapshot,
)
from .planner import build_generation_plan, render_seed_files
from .schema_validation import schema_errors_as_text
from .snapshot import build_target_snapshot
from .version import package_version
from .staging import stage_generation_plan


VALIDATORS: dict[str, Callable[[dict[str, Any]], list[str]]] = {
    "activation-report": validate_activation_report,
    "generation-plan": validate_generation_plan,
    "project-model": validate_project_model,
    "seed-spec": validate_seed_spec,
    "skill-registry": validate_skill_registry,
    "source-manifest": validate_source_manifest,
    "target-snapshot": validate_target_snapshot,
}


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        return args.handler(args)
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"repokernel: {exc}", file=sys.stderr)
        return 2


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="repokernel", description="RepoKernel Phase 1 read-only compiler tools.")
    sub = parser.add_subparsers(dest="command", required=True)

    validate = sub.add_parser("validate-spec", help="validate a RepoKernel JSON contract")
    validate.add_argument("--kind", choices=sorted(VALIDATORS), required=True)
    validate.add_argument("--input", required=True)
    validate.set_defaults(handler=_cmd_validate_spec)

    validate_bundle_cmd = sub.add_parser("validate-bundle", help="validate linked SourceManifest, ProjectModel and SeedSpec")
    validate_bundle_cmd.add_argument("--source-manifest", required=True)
    validate_bundle_cmd.add_argument("--project-model", required=True)
    validate_bundle_cmd.add_argument("--seed-spec", required=True)
    validate_bundle_cmd.set_defaults(handler=_cmd_validate_bundle)

    inspect_cmd = sub.add_parser("inspect", help="inspect a repository without writing")
    inspect_cmd.add_argument("--path", required=True)
    inspect_cmd.set_defaults(handler=_cmd_inspect)

    plan = sub.add_parser("plan", help="build a deterministic GenerationPlan without writing")
    plan.add_argument("--seed-spec", required=True)
    plan.add_argument("--source-manifest", required=True)
    plan.add_argument("--project-model", required=True)
    plan.add_argument("--existing-paths-file")
    plan.add_argument("--target-snapshot")
    plan.set_defaults(handler=_cmd_plan)

    stage = sub.add_parser("stage", help="render plan content into an empty staging directory")
    stage.add_argument("--plan", required=True)
    stage.add_argument("--output-dir", required=True)
    stage.set_defaults(handler=_cmd_stage)

    guides = sub.add_parser("guides", help="project guide text to stdout as JSON")
    guides.add_argument("--seed-spec", required=True)
    guides.add_argument("--source-manifest", required=True)
    guides.set_defaults(handler=_cmd_guides)

    audit_cmd = sub.add_parser("audit", help="run a read-only RepoKernel audit")
    audit_cmd.add_argument("--path", required=True)
    audit_cmd.add_argument("--profile", choices=sorted(PROFILES), default="project")
    audit_cmd.set_defaults(handler=_cmd_audit)

    verify_dist = sub.add_parser("verify-dist", help="verify a reference seed distribution")
    verify_dist.add_argument("--seed-spec", required=True)
    verify_dist.add_argument("--dist-dir", required=True)
    verify_dist.set_defaults(handler=_cmd_verify_dist)
    return parser


def _cmd_validate_spec(args: argparse.Namespace) -> int:
    data = _read_json(Path(args.input))
    python_errors = VALIDATORS[args.kind](data)
    schema_errors = schema_errors_as_text(args.kind, data)
    errors = python_errors + [f"schema: {error}" for error in schema_errors]
    report = {
        "schema": "repokernel.cli.validate-result.v1",
        "kind": args.kind,
        "input": args.input,
        "valid": not errors,
        "errors": errors,
        "python_errors": python_errors,
        "schema_errors": schema_errors,
    }
    print(report_as_json(report))
    return 0 if not errors else 1


def _cmd_validate_bundle(args: argparse.Namespace) -> int:
    manifest = _read_json(Path(args.source_manifest))
    model = _read_json(Path(args.project_model))
    spec = _read_json(Path(args.seed_spec))
    result = validate_bundle(manifest, model, spec)
    report = {
        "schema": "repokernel.cli.validate-bundle-result.v1",
        "valid": result.valid,
        "errors": result.errors,
        "provenance": result.provenance,
    }
    print(report_as_json(report))
    return 0 if result.valid else 1


def _cmd_inspect(args: argparse.Namespace) -> int:
    root = Path(args.path).expanduser().resolve()
    report = inspect_repository(root)
    report["target_snapshot"] = build_target_snapshot(root)
    print(report_as_json(report))
    return 0 if root.is_dir() else 1


def _cmd_plan(args: argparse.Namespace) -> int:
    spec = _read_json(Path(args.seed_spec))
    manifest = _read_json(Path(args.source_manifest))
    model = _read_json(Path(args.project_model))
    bundle = validate_bundle(manifest, model, spec)
    if not bundle.valid:
        raise ValueError("; ".join(bundle.errors))
    existing_paths = _read_existing_paths(Path(args.existing_paths_file)) if args.existing_paths_file else None
    target_snapshot = _read_json(Path(args.target_snapshot)) if args.target_snapshot else None
    if isinstance(target_snapshot, dict) and target_snapshot.get("schema") != "repokernel.target-snapshot.v1":
        nested = target_snapshot.get("target_snapshot")
        if isinstance(nested, dict):
            target_snapshot = nested
    print(report_as_json(build_generation_plan(
        spec,
        project_model=model,
        existing_paths=existing_paths,
        target_snapshot=target_snapshot,
        bundle_provenance=bundle.provenance,
    )))
    return 0


def _cmd_stage(args: argparse.Namespace) -> int:
    plan = _read_json(Path(args.plan))
    print(report_as_json(stage_generation_plan(plan, Path(args.output_dir))))
    return 0


def _cmd_guides(args: argparse.Namespace) -> int:
    spec = _read_json(Path(args.seed_spec))
    manifest = _read_json(Path(args.source_manifest))
    errors = VALIDATORS["seed-spec"](spec) + [f"seed-spec schema: {error}" for error in schema_errors_as_text("seed-spec", spec)]
    errors.extend(VALIDATORS["source-manifest"](manifest))
    errors.extend(f"source-manifest schema: {error}" for error in schema_errors_as_text("source-manifest", manifest))
    if errors:
        raise ValueError("; ".join(errors))
    print(report_as_json({
        "schema": "repokernel.cli.guides-result.v1",
        "package_version": package_version(),
        "seed_spec_hash": canonical_hash(spec),
        "guides": build_guides(spec, manifest),
    }))
    return 0


def _cmd_audit(args: argparse.Namespace) -> int:
    root = Path(args.path).expanduser().resolve()
    result = audit(root, args.profile)
    print(report_as_json(result))
    return 0 if result["ready"] else 1


def _cmd_verify_dist(args: argparse.Namespace) -> int:
    seed = _read_json(Path(args.seed_spec))
    dist_dir = Path(args.dist_dir).expanduser().resolve()
    errors: list[str] = []
    try:
        generated = render_seed_files(seed)
    except ValueError as exc:
        errors.append(str(exc))
        generated = {}
    expected_paths = set(generated)
    actual_paths = {
        path.relative_to(dist_dir).as_posix()
        for path in dist_dir.rglob("*")
        if path.is_file()
    } if dist_dir.is_dir() else set()
    for rel in sorted(expected_paths - actual_paths):
        errors.append(f"missing dist file: {rel}")
    for rel in sorted(actual_paths - expected_paths):
        errors.append(f"extra dist file: {rel}")
    for rel in sorted(expected_paths & actual_paths):
        expected_hash = _content_hash(generated[rel])
        actual_text = (dist_dir / rel).read_text(encoding="utf-8").replace("\r\n", "\n").replace("\r", "\n")
        actual_hash = _content_hash(actual_text)
        if actual_hash != expected_hash:
            errors.append(f"hash mismatch for {rel}: {actual_hash} != {expected_hash}")
    report = {
        "schema": "repokernel.cli.verify-dist-result.v1",
        "package_version": package_version(),
        "seed_spec": args.seed_spec,
        "dist_dir": str(dist_dir),
        "valid": not errors,
        "errors": errors,
    }
    print(report_as_json(report))
    return 0 if not errors else 1


def _read_json(path: Path) -> dict[str, Any]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError(f"expected JSON object: {path}")
    return data


def _read_existing_paths(path: Path) -> list[str]:
    return [line.strip() for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def _content_hash(content: str) -> str:
    return hashlib.sha256(content.replace("\r\n", "\n").replace("\r", "\n").encode("utf-8")).hexdigest()


if __name__ == "__main__":
    raise SystemExit(main())
