import copy
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "src"))

from fixtures import project_model, seed_spec, source_manifest
from repokernel.bundle import validate_bundle
from repokernel.models import (
    validate_activation_report,
    validate_generation_plan,
    validate_project_model,
    validate_seed_spec,
    validate_skill_registry,
    validate_source_manifest,
    validate_target_snapshot,
)
from repokernel.planner import build_generation_plan
from repokernel.schema_validation import schema_errors_as_text
from repokernel.snapshot import build_target_snapshot


def activation_report():
    return {
        "schema": "repokernel.activation-report.v1",
        "state": "active",
        "checks": [{"id": "unit", "ok": True}],
    }


def skill_registry():
    return {
        "schema": "repokernel.skill-registry.v1",
        "skills": [
            {
                "id": "demo-skill",
                "state": "draft",
                "path": "skills/demo-skill/SKILL.md",
                "risk": "low",
                "evidence": ["tests/unit/test_schema_validator_parity.py"],
            }
        ],
    }


def target_snapshot(tmp_path: Path):
    (tmp_path / "README.md").write_text("demo", encoding="utf-8")
    return build_target_snapshot(tmp_path)


class SchemaValidatorParityTests(unittest.TestCase):
    def test_valid_contracts_match(self):
        with self.subTest("source-manifest"):
            self._assert_valid("source-manifest", source_manifest(), validate_source_manifest)
        with self.subTest("project-model"):
            self._assert_valid("project-model", project_model(), validate_project_model)
        with self.subTest("seed-spec"):
            self._assert_valid("seed-spec", seed_spec(), validate_seed_spec)
        with self.subTest("activation-report"):
            self._assert_valid("activation-report", activation_report(), validate_activation_report)
        with self.subTest("skill-registry"):
            self._assert_valid("skill-registry", skill_registry(), validate_skill_registry)
        with self.subTest("generation-plan"):
            bundle = validate_bundle(source_manifest(), project_model(), seed_spec())
            plan = build_generation_plan(seed_spec(), bundle_provenance=bundle.provenance)
            self._assert_valid("generation-plan", plan, validate_generation_plan)
        import tempfile

        with tempfile.TemporaryDirectory() as tmp:
            with self.subTest("target-snapshot"):
                self._assert_valid("target-snapshot", target_snapshot(Path(tmp)), validate_target_snapshot)

    def test_invalid_contracts_match(self):
        cases = []
        manifest = copy.deepcopy(source_manifest())
        manifest["sources"][0]["privacy"] = "secret"
        cases.append(("source-manifest", manifest, validate_source_manifest))

        model = copy.deepcopy(project_model())
        model["assertions"][0]["source_refs"] = []
        cases.append(("project-model", model, validate_project_model))

        seed = copy.deepcopy(seed_spec())
        seed["review"]["status"] = "draft"
        cases.append(("seed-spec", seed, validate_seed_spec))

        report = activation_report()
        report["checks"][0]["ok"] = False
        cases.append(("activation-report", report, validate_activation_report))

        registry = skill_registry()
        registry["skills"][0]["risk"] = "unknown"
        cases.append(("skill-registry", registry, validate_skill_registry))

        bundle = validate_bundle(source_manifest(), project_model(), seed_spec())
        plan = build_generation_plan(seed_spec(), bundle_provenance=bundle.provenance)
        plan["apply_policy"] = "apply"
        cases.append(("generation-plan", plan, validate_generation_plan))

        import tempfile

        with tempfile.TemporaryDirectory() as tmp:
            snapshot = target_snapshot(Path(tmp))
            snapshot["entries"][0]["path"] = "C:\\bad"
            cases.append(("target-snapshot", snapshot, validate_target_snapshot))

            for kind, value, validator in cases:
                with self.subTest(kind):
                    self._assert_invalid(kind, value, validator)

    def _assert_valid(self, kind, value, validator):
        self.assertEqual([], validator(value), kind)
        self.assertEqual([], schema_errors_as_text(kind, value), kind)

    def _assert_invalid(self, kind, value, validator):
        self.assertNotEqual([], validator(value), kind)
        self.assertNotEqual([], schema_errors_as_text(kind, value), kind)


if __name__ == "__main__":
    unittest.main()
