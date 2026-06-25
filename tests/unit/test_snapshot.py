import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "src"))

from repokernel.snapshot import build_target_snapshot


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


if __name__ == "__main__":
    unittest.main()
