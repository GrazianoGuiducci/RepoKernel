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
)


ROOT = Path(__file__).resolve().parents[2]


class SchemaTests(unittest.TestCase):
    def test_schema_files_are_json(self):
        for path in (ROOT / "schemas").glob("*.schema.json"):
            with self.subTest(path=path.name):
                self.assertIsInstance(json.loads(path.read_text(encoding="utf-8")), dict)

    def test_minimal_contracts_validate(self):
        self.assertEqual(validate_source_manifest({
            "schema": "repokernel.source-manifest.v1",
            "sources": [{"source_id": "s1", "authority": "operator", "privacy": "public", "used_for": ["model"]}],
        }), [])
        self.assertEqual(validate_project_model({
            "schema": "repokernel.project-model.v1",
            "identity": {"name": "Demo"},
            "mission": "Test",
            "product_or_result": "Kernel",
            "source_refs": ["s1"],
            "boundaries": {},
            "unknowns": [],
        }), [])
        self.assertEqual(validate_seed_spec({
            "schema": "repokernel.seed-spec.v1",
            "seed_id": "demo",
            "project": {"name": "Demo", "intent": "Test", "product": "Kernel"},
            "target": {"mode": "new_repository"},
            "readiness_level": "L1",
            "authority_mode": "propose",
        }), [])
        self.assertEqual(validate_generation_plan({
            "schema": "repokernel.generation-plan.v1",
            "seed_hash": "abc",
            "items": [],
            "blocked": False,
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

    def test_seed_spec_requires_seed_id_and_safe_target_path(self):
        errors = validate_seed_spec({
            "schema": "repokernel.seed-spec.v1",
            "project": {"name": "Demo", "intent": "Test", "product": "Kernel"},
            "target": {"mode": "new_repository", "path": "C:/unsafe"},
            "readiness_level": "L1",
            "authority_mode": "propose",
        })
        self.assertIn("seed_id is required", errors)
        self.assertTrue(any(error.startswith("target.path invalid") for error in errors))


if __name__ == "__main__":
    unittest.main()
