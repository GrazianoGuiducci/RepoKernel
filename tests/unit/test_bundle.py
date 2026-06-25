import copy
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "src"))

from fixtures import project_model, seed_spec, source_manifest
from repokernel.bundle import validate_bundle


class BundleTests(unittest.TestCase):
    def test_valid_bundle_links_hashes_and_refs(self):
        result = validate_bundle(source_manifest(), project_model(), seed_spec())
        self.assertTrue(result.valid, result.errors)
        self.assertEqual(result.provenance["package_version"], "0.3.0.dev0")

    def test_wrong_seed_hash_is_rejected(self):
        seed = seed_spec()
        seed["source_manifest_hash"] = "f" * 64
        result = validate_bundle(source_manifest(), project_model(), seed)
        self.assertFalse(result.valid)
        self.assertTrue(any("source_manifest_hash" in error for error in result.errors))

    def test_project_model_unknown_source_ref_is_rejected(self):
        model = copy.deepcopy(project_model())
        model["assertions"][0]["source_refs"] = ["missing-source"]
        result = validate_bundle(source_manifest(), model, seed_spec())
        self.assertFalse(result.valid)
        self.assertTrue(any("missing-source" in error for error in result.errors))


if __name__ == "__main__":
    unittest.main()
