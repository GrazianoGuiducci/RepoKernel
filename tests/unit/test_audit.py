import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "src"))

from repokernel.audit import audit


ROOT = Path(__file__).resolve().parents[2]


class AuditTests(unittest.TestCase):
    def test_source_audit_reports_separate_readiness_axes(self):
        result = audit(ROOT, "repokernel-source")
        readiness = result["readiness"]
        self.assertIn("repository_structure_ready", readiness)
        self.assertIn("contract_conformant", readiness)
        self.assertIn("planner_conformant", readiness)
        self.assertIn("project_kernel_ready", readiness)
        self.assertIn("distribution_ready", readiness)


if __name__ == "__main__":
    unittest.main()
