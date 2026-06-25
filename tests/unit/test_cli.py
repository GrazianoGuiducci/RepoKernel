import contextlib
import io
import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "src"))

from repokernel.cli import main


def seed_spec():
    return {
        "schema": "repokernel.seed-spec.v1",
        "version": "repokernel.seed-spec.v1",
        "seed_id": "demo-seed",
        "source_manifest_hash": "0" * 64,
        "project_model_hash": "0" * 64,
        "canonical_namespace": ".repokernel",
        "project": {"name": "Demo", "intent": "Test continuity", "product": "Kernel"},
        "target": {"mode": "new_repository", "path": "demo"},
        "readiness_level": "L2",
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
        "disclosure": {"public": {"name": True, "intent": True, "product": False}},
    }


def source_manifest():
    return {
        "schema": "repokernel.source-manifest.v1",
        "sources": [
            {
                "source_id": "readme",
                "public_label": "README",
                "authority": "operator",
                "privacy": "public",
                "used_for": ["public_guide"],
            },
            {
                "source_id": "private-notes",
                "path_or_origin": "private.md",
                "authority": "operator",
                "privacy": "private",
                "used_for": ["model"],
            },
        ],
    }


class CliTests(unittest.TestCase):
    def test_validate_spec_reports_valid_seed(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "seed.json"
            path.write_text(json.dumps(seed_spec()), encoding="utf-8")
            code, data = self._run_json(["validate-spec", "--kind", "seed-spec", "--input", str(path)])
            self.assertEqual(code, 0)
            self.assertTrue(data["valid"])

    def test_plan_outputs_generation_plan_without_writing(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            path = root / "seed.json"
            path.write_text(json.dumps(seed_spec()), encoding="utf-8")
            code, data = self._run_json(["plan", "--seed-spec", str(path)])
            self.assertEqual(code, 0)
            self.assertEqual(data["schema"], "repokernel.generation-plan.v1")
            self.assertFalse(any(child.name != "seed.json" for child in root.iterdir()))

    def test_stage_writes_only_to_explicit_staging_dir(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            seed_path = root / "seed.json"
            plan_path = root / "plan.json"
            stage_dir = root / "staged"
            target_dir = root / "target"
            target_dir.mkdir()
            seed_path.write_text(json.dumps(seed_spec()), encoding="utf-8")
            code, plan = self._run_json(["plan", "--seed-spec", str(seed_path)])
            self.assertEqual(code, 0)
            plan_path.write_text(json.dumps(plan), encoding="utf-8")

            code, report = self._run_json(["stage", "--plan", str(plan_path), "--output-dir", str(stage_dir)])

            self.assertEqual(code, 0)
            self.assertEqual(report["boundary"], "staging_only_not_apply")
            self.assertEqual(report["target_writes_performed"], [])
            self.assertTrue((stage_dir / ".repokernel" / "state" / "CURRENT_STATE.md").is_file())
            self.assertFalse(any(target_dir.iterdir()))

    def test_stage_rejects_non_empty_output_dir(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            seed_path = root / "seed.json"
            plan_path = root / "plan.json"
            stage_dir = root / "staged"
            stage_dir.mkdir()
            (stage_dir / "existing.txt").write_text("keep", encoding="utf-8")
            seed_path.write_text(json.dumps(seed_spec()), encoding="utf-8")
            code, plan = self._run_json(["plan", "--seed-spec", str(seed_path)])
            self.assertEqual(code, 0)
            plan_path.write_text(json.dumps(plan), encoding="utf-8")

            stderr = io.StringIO()
            with contextlib.redirect_stderr(stderr):
                code = main(["stage", "--plan", str(plan_path), "--output-dir", str(stage_dir)])

            self.assertEqual(code, 2)
            self.assertIn("output directory must be empty", stderr.getvalue())

    def test_guides_withhold_private_sources(self):
        with tempfile.TemporaryDirectory() as tmp:
            seed_path = Path(tmp) / "seed.json"
            manifest_path = Path(tmp) / "manifest.json"
            seed_path.write_text(json.dumps(seed_spec()), encoding="utf-8")
            manifest_path.write_text(json.dumps(source_manifest()), encoding="utf-8")
            code, data = self._run_json(["guides", "--seed-spec", str(seed_path), "--source-manifest", str(manifest_path)])
            self.assertEqual(code, 0)
            text = "\n".join(data["guides"].values())
            self.assertIn("README", text)
            self.assertNotIn("private.md", text)

    def test_inspect_is_read_only(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            code, data = self._run_json(["inspect", "--path", str(root)])
            self.assertEqual(code, 0)
            self.assertEqual(data["boundary"], "read_only")
            self.assertIn("target_snapshot", data)
            self.assertFalse(any(root.iterdir()))

    def _run_json(self, argv):
        stdout = io.StringIO()
        with contextlib.redirect_stdout(stdout):
            code = main(argv)
        return code, json.loads(stdout.getvalue())


if __name__ == "__main__":
    unittest.main()
