import contextlib
import io
import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "src"))

from repokernel.cli import main
from fixtures import project_model, seed_spec, source_manifest


class CliTests(unittest.TestCase):
    def test_validate_spec_reports_valid_seed(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "seed.json"
            path.write_text(json.dumps(seed_spec()), encoding="utf-8")
            code, data = self._run_json(["validate-spec", "--kind", "seed-spec", "--input", str(path)])
            self.assertEqual(code, 0)
            self.assertTrue(data["valid"])

    def test_validate_bundle_reports_valid_linkage(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            seed_path, manifest_path, model_path = self._write_bundle(root)
            code, data = self._run_json([
                "validate-bundle",
                "--source-manifest", str(manifest_path),
                "--project-model", str(model_path),
                "--seed-spec", str(seed_path),
            ])
            self.assertEqual(code, 0)
            self.assertTrue(data["valid"])

    def test_plan_outputs_generation_plan_without_writing(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            seed_path, manifest_path, model_path = self._write_bundle(root)
            code, data = self._run_json([
                "plan",
                "--seed-spec", str(seed_path),
                "--source-manifest", str(manifest_path),
                "--project-model", str(model_path),
            ])
            self.assertEqual(code, 0)
            self.assertEqual(data["schema"], "repokernel.generation-plan.v1")
            self.assertIn("bundle_provenance", data)
            self.assertFalse(any(child.name not in {"seed.json", "manifest.json", "model.json"} for child in root.iterdir()))

    def test_stage_writes_only_to_explicit_staging_dir(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            plan_path = root / "plan.json"
            stage_dir = root / "staged"
            target_dir = root / "target"
            target_dir.mkdir()
            seed_path, manifest_path, model_path = self._write_bundle(root)
            code, plan = self._run_json([
                "plan",
                "--seed-spec", str(seed_path),
                "--source-manifest", str(manifest_path),
                "--project-model", str(model_path),
            ])
            self.assertEqual(code, 0)
            plan_path.write_text(json.dumps(plan), encoding="utf-8")

            code, report = self._run_json(["stage", "--plan", str(plan_path), "--output-dir", str(stage_dir)])

            self.assertEqual(code, 0)
            self.assertEqual(report["boundary"], "staging_only_not_apply")
            self.assertEqual(report["target_writes_performed"], [])
            self.assertIn("REVIEW_ME_FIRST.md", report["writes_performed"])
            self.assertTrue((stage_dir / "REVIEW_ME_FIRST.md").is_file())
            self.assertTrue((stage_dir / ".repokernel" / "state" / "CURRENT_STATE.md").is_file())
            self.assertFalse(any(target_dir.iterdir()))

    def test_stage_rejects_non_empty_output_dir(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            plan_path = root / "plan.json"
            stage_dir = root / "staged"
            stage_dir.mkdir()
            (stage_dir / "existing.txt").write_text("keep", encoding="utf-8")
            seed_path, manifest_path, model_path = self._write_bundle(root)
            code, plan = self._run_json([
                "plan",
                "--seed-spec", str(seed_path),
                "--source-manifest", str(manifest_path),
                "--project-model", str(model_path),
            ])
            self.assertEqual(code, 0)
            plan_path.write_text(json.dumps(plan), encoding="utf-8")

            stderr = io.StringIO()
            with contextlib.redirect_stderr(stderr):
                code = main(["stage", "--plan", str(plan_path), "--output-dir", str(stage_dir)])

            self.assertEqual(code, 2)
            self.assertIn("output directory must be empty", stderr.getvalue())

    def test_stage_rejects_blocked_plan(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            plan_path = root / "blocked-plan.json"
            stage_dir = root / "staged"
            seed_path, manifest_path, model_path = self._write_bundle(root)
            code, plan = self._run_json([
                "plan",
                "--seed-spec", str(seed_path),
                "--source-manifest", str(manifest_path),
                "--project-model", str(model_path),
            ])
            self.assertEqual(code, 0)
            plan["blocked"] = True
            plan["blocked_reasons"] = ["test block"]
            plan_path.write_text(json.dumps(plan), encoding="utf-8")
            stderr = io.StringIO()
            with contextlib.redirect_stderr(stderr):
                code = main(["stage", "--plan", str(plan_path), "--output-dir", str(stage_dir)])
            self.assertEqual(code, 2)
            self.assertIn("blocked plan cannot be staged", stderr.getvalue())

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

    def test_plan_rejects_unbound_seed_hashes(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            seed_path, manifest_path, model_path = self._write_bundle(root)
            bad = seed_spec()
            bad["source_manifest_hash"] = "f" * 64
            seed_path.write_text(json.dumps(bad), encoding="utf-8")
            stderr = io.StringIO()
            with contextlib.redirect_stderr(stderr):
                code = main([
                    "plan",
                    "--seed-spec", str(seed_path),
                    "--source-manifest", str(manifest_path),
                    "--project-model", str(model_path),
                ])
            self.assertEqual(code, 2)
            self.assertIn("source_manifest_hash", stderr.getvalue())

    def _run_json(self, argv):
        stdout = io.StringIO()
        with contextlib.redirect_stdout(stdout):
            code = main(argv)
        return code, json.loads(stdout.getvalue())

    def _write_bundle(self, root: Path):
        seed_path = root / "seed.json"
        manifest_path = root / "manifest.json"
        model_path = root / "model.json"
        seed_path.write_text(json.dumps(seed_spec()), encoding="utf-8")
        manifest_path.write_text(json.dumps(source_manifest()), encoding="utf-8")
        model_path.write_text(json.dumps(project_model()), encoding="utf-8")
        return seed_path, manifest_path, model_path


if __name__ == "__main__":
    unittest.main()
