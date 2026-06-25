import contextlib
import io
import json
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "src"))

from repokernel.cli import main


ROOT = Path(__file__).resolve().parents[2]


class VerifyDistTests(unittest.TestCase):
    def test_reference_seed_distribution_verifies(self):
        stdout = io.StringIO()
        with contextlib.redirect_stdout(stdout):
            code = main([
                "verify-dist",
                "--seed-spec",
                str(ROOT / "specs/reference/starter-l1.seed.json"),
                "--dist-dir",
                str(ROOT / "dist/reference/starter-l1"),
            ])
        self.assertEqual(code, 0)
        self.assertTrue(json.loads(stdout.getvalue())["valid"])

    def test_reference_seed_distribution_rejects_extra_file(self):
        with tempfile.TemporaryDirectory() as tmp:
            dist = Path(tmp) / "starter-l1"
            shutil.copytree(ROOT / "dist/reference/starter-l1", dist)
            (dist / "extra.txt").write_text("not generated", encoding="utf-8")
            stdout = io.StringIO()
            with contextlib.redirect_stdout(stdout):
                code = main([
                    "verify-dist",
                    "--seed-spec",
                    str(ROOT / "specs/reference/starter-l1.seed.json"),
                    "--dist-dir",
                    str(dist),
                ])
            self.assertEqual(code, 1)
            self.assertIn("extra dist file", "\n".join(json.loads(stdout.getvalue())["errors"]))


if __name__ == "__main__":
    unittest.main()
