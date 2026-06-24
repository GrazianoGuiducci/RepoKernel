import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "src"))

from repokernel.canonical import canonical_dumps, canonical_hash, validate_namespaced_extensions


class CanonicalTests(unittest.TestCase):
    def test_canonical_order_is_stable(self):
        left = {"b": 2, "a": {"d": 4, "c": 3}}
        right = {"a": {"c": 3, "d": 4}, "b": 2}
        self.assertEqual(canonical_dumps(left), canonical_dumps(right))
        self.assertEqual(canonical_hash(left), canonical_hash(right))

    def test_extensions_round_trip_and_cannot_raise_authority(self):
        good = {"dnd.note": {"value": "preserve me"}}
        self.assertEqual(validate_namespaced_extensions(good), [])
        bad = {"bad": {"authority_mode": "project_write"}}
        self.assertTrue(validate_namespaced_extensions(bad))


if __name__ == "__main__":
    unittest.main()
