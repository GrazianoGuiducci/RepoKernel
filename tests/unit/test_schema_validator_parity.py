import copy
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "src"))

from repokernel.models import validate_seed_spec, validate_source_manifest
from repokernel.schema_validation import schema_errors_as_text


HASH = "0" * 64


def valid_seed():
    return {
        "schema": "repokernel.seed-spec.v1",
        "version": "repokernel.seed-spec.v1",
        "seed_id": "demo",
        "source_manifest_hash": HASH,
        "project_model_hash": HASH,
        "canonical_namespace": ".repokernel",
        "project": {"name": "Demo", "intent": "Test", "product": "Kernel"},
        "target": {"mode": "new_repository", "path": "demo"},
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


class SchemaValidatorParityTests(unittest.TestCase):
    def test_seed_spec_validity_matches(self):
        seed = valid_seed()
        self.assertEqual(validate_seed_spec(seed) == [], schema_errors_as_text("seed-spec", seed) == [])

    def test_seed_spec_invalid_review_matches(self):
        seed = copy.deepcopy(valid_seed())
        seed["review"]["status"] = "draft"
        self.assertEqual(validate_seed_spec(seed) == [], schema_errors_as_text("seed-spec", seed) == [])

    def test_source_manifest_validity_matches(self):
        manifest = {
            "schema": "repokernel.source-manifest.v1",
            "sources": [
                {
                    "source_id": "s1",
                    "authority": "operator",
                    "privacy": "public",
                    "used_for": ["model"],
                    "instruction_handling": "data_only",
                }
            ],
        }
        self.assertEqual(validate_source_manifest(manifest) == [], schema_errors_as_text("source-manifest", manifest) == [])


if __name__ == "__main__":
    unittest.main()
