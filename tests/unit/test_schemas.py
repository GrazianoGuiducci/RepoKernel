import json
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "src"))

from repokernel.models import (
    validate_activation_report,
    validate_generation_plan,
    validate_project_model,
    validate_seed_spec,
    validate_skill_registry,
    validate_source_manifest,
    validate_target_snapshot,
)
from repokernel.schema_validation import schema_errors_as_text
from fixtures import project_model, seed_spec, source_manifest


ROOT = Path(__file__).resolve().parents[2]
HASH = "0" * 64


def accepted_seed_spec():
    return {
        "schema": "repokernel.seed-spec.v1",
        "version": "repokernel.seed-spec.v1",
        "seed_id": "demo",
        "source_manifest_hash": HASH,
        "project_model_hash": HASH,
        "canonical_namespace": ".repokernel",
        "project": {"name": "Demo", "intent": "Test", "product": "Kernel"},
        "target": {"mode": "new_repository"},
        "readiness_level": "L1",
        "authority_mode": "propose",
        "review": {
            "status": "accepted",
            "accepted_by_role": "operator",
            "accepted_at": "2026-06-25",
            "review_cycle": "RK-RVW-20260625-01",
        },
        "compiler_compatibility": {"package_version": "0.3.0.dev0"},
        "file_plan_policy": "stage_only",
        "validation_plan": ["validate-spec", "plan", "stage"],
    }


class SchemaTests(unittest.TestCase):
    def test_schema_files_are_json(self):
        for path in (ROOT / "schemas").glob("*.schema.json"):
            with self.subTest(path=path.name):
                self.assertIsInstance(json.loads(path.read_text(encoding="utf-8")), dict)

    def test_minimal_contracts_validate(self):
        self.assertEqual(validate_source_manifest(source_manifest()), [])
        self.assertEqual(validate_project_model(project_model()), [])
        self.assertEqual(validate_seed_spec(seed_spec()), [])
        self.assertEqual(validate_generation_plan({
            "schema": "repokernel.generation-plan.v1",
            "plan_id": HASH,
            "compiler_version": "0.3.0.dev0",
            "seed_hash": HASH,
            "bundle_hash": HASH,
            "bundle_provenance": {},
            "target_identity": "target",
            "target_snapshot_hash": "none",
            "before_hash": "none",
            "after_hash": HASH,
            "after_hash_kind": "projected_after_state.v1",
            "apply_policy": "stage_only",
            "items": [],
            "blocked": False,
            "blocked_reasons": [],
        }), [])
        self.assertEqual(validate_activation_report({
            "schema": "repokernel.activation-report.v1",
            "state": "blocked",
            "checks": [],
        }), [])
        self.assertEqual(validate_skill_registry({
            "schema": "repokernel.skill-registry.v1",
            "skills": [],
        }), [])
        self.assertEqual(validate_target_snapshot({
            "schema": "repokernel.target-snapshot.v1",
            "target_snapshot_id": HASH,
            "target_identity": "target",
            "tree_hash": HASH,
            "entries": [],
        }), [])

    def test_seed_spec_requires_seed_id_and_safe_target_path(self):
        spec = accepted_seed_spec()
        spec.pop("seed_id")
        spec["target"] = {"mode": "new_repository", "path": "C:/unsafe"}
        errors = validate_seed_spec(spec)
        self.assertIn("seed_id is required", errors)
        self.assertTrue(any(error.startswith("target.path invalid") for error in errors))

    def test_schema_and_python_acceptance_match_for_valid_contracts(self):
        cases = {
            "seed-spec": (seed_spec(), validate_seed_spec),
            "source-manifest": (source_manifest(), validate_source_manifest),
            "target-snapshot": ({
                "schema": "repokernel.target-snapshot.v1",
                "target_snapshot_id": HASH,
                "target_identity": "target",
                "tree_hash": HASH,
                "entries": [],
            }, validate_target_snapshot),
        }
        for kind, (data, validator) in cases.items():
            with self.subTest(kind=kind):
                self.assertEqual(validator(data), [])
                self.assertEqual(schema_errors_as_text(kind, data), [])

    def test_schema_and_python_reject_unaccepted_seed(self):
        spec = accepted_seed_spec()
        spec["review"]["status"] = "draft"
        self.assertTrue(validate_seed_spec(spec))
        self.assertTrue(schema_errors_as_text("seed-spec", spec))

    def test_duplicate_source_ids_rejected(self):
        manifest = {
            "schema": "repokernel.source-manifest.v1",
            "sources": [
                {"source_id": "dup", "authority": "operator", "privacy": "public", "used_for": ["model"]},
                {"source_id": "dup", "authority": "operator", "privacy": "public", "used_for": ["model"]},
            ],
        }
        self.assertTrue(any("duplicate" in error for error in validate_source_manifest(manifest)))


if __name__ == "__main__":
    unittest.main()
