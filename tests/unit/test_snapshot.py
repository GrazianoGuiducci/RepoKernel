import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "src"))

from repokernel.snapshot import build_target_snapshot
from repokernel.models import validate_target_snapshot


class SnapshotTests(unittest.TestCase):
    def test_snapshot_hash_changes_with_content(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            path = root / "README.md"
            path.write_text("one", encoding="utf-8")
            first = build_target_snapshot(root)
            path.write_text("two", encoding="utf-8")
            second = build_target_snapshot(root)
            self.assertNotEqual(first["tree_hash"], second["tree_hash"])

    def test_snapshot_excludes_git_directory(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / ".git").mkdir()
            (root / ".git" / "config").write_text("secret", encoding="utf-8")
            snapshot = build_target_snapshot(root)
            self.assertFalse(any(entry["path"].startswith(".git/") for entry in snapshot["entries"]))

    def test_snapshot_excludes_sensitive_paths_without_leaking_name(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / ".env").write_text("SECRET=value", encoding="utf-8")
            snapshot = build_target_snapshot(root)
            self.assertFalse(snapshot["entries"])
            self.assertEqual(snapshot["excluded"][0]["path"], "<withheld-sensitive-path>")
            self.assertNotIn("SECRET", str(snapshot))

    def test_duplicate_snapshot_path_is_invalid(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "README.md").write_text("one", encoding="utf-8")
            snapshot = build_target_snapshot(root)
            snapshot["entries"].append(dict(snapshot["entries"][0]))
            self.assertTrue(any("duplicate" in error for error in validate_target_snapshot(snapshot)))

    def test_forged_snapshot_hash_is_invalid(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "README.md").write_text("one", encoding="utf-8")
            snapshot = build_target_snapshot(root)
            snapshot["tree_hash"] = "f" * 64
            from repokernel.snapshot import snapshot_integrity_errors

            self.assertTrue(snapshot_integrity_errors(snapshot))


if __name__ == "__main__":
    unittest.main()
