import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "src"))

from repokernel.guide_model import build_guides, public_source_titles


class GuideModelTests(unittest.TestCase):
    def test_private_sources_are_excluded(self):
        manifest = {
            "schema": "repokernel.source-manifest.v1",
            "sources": [
                {"source_id": "public", "path_or_origin": "README.md", "authority": "source", "privacy": "public", "used_for": ["guide"]},
                {"source_id": "secret", "path_or_origin": ".env", "authority": "source", "privacy": "private", "used_for": ["none"]},
            ],
        }
        self.assertEqual(public_source_titles(manifest), ["README.md"])
        guides = build_guides({
            "project": {"name": "Demo", "intent": "Test", "product": "Guide output"}
        }, manifest)
        all_text = "\n".join(guides.values())
        self.assertIn("README.md", all_text)
        self.assertNotIn(".env", all_text)
        self.assertIn("do not redefine authority", all_text)


if __name__ == "__main__":
    unittest.main()
