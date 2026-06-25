"""JSON Schema validation for RepoKernel contracts."""
from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator, FormatChecker
from jsonschema.exceptions import ValidationError


SCHEMA_DIRS = [
    Path(__file__).resolve().parent / "schemas",
    Path.cwd() / "schemas",
    Path(__file__).resolve().parents[2] / "schemas",
]

SCHEMA_FILES = {
    "activation-report": "activation-report.schema.json",
    "generation-plan": "generation-plan.schema.json",
    "project-model": "project-model.schema.json",
    "seed-spec": "seed-spec.schema.json",
    "skill-registry": "skill-registry.schema.json",
    "source-manifest": "source-manifest.schema.json",
    "target-snapshot": "target-snapshot.schema.json",
}


@dataclass(frozen=True)
class SchemaValidationError:
    path: str
    code: str
    message: str

    def as_text(self) -> str:
        return f"{self.path or '$'}: {self.code}: {self.message}"


def validate_with_schema(kind: str, data: dict[str, Any]) -> list[SchemaValidationError]:
    """Validate `data` against a Draft 2020-12 schema."""
    schema = _load_schema(kind)
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    return [_format_error(error) for error in sorted(validator.iter_errors(data), key=lambda err: list(err.path))]


def schema_errors_as_text(kind: str, data: dict[str, Any]) -> list[str]:
    return [error.as_text() for error in validate_with_schema(kind, data)]


def _load_schema(kind: str) -> dict[str, Any]:
    try:
        filename = SCHEMA_FILES[kind]
    except KeyError as exc:
        raise ValueError(f"unknown schema kind: {kind}") from exc
    path = next((candidate / filename for candidate in SCHEMA_DIRS if (candidate / filename).is_file()), None)
    if path is None:
        searched = ", ".join(str(candidate) for candidate in SCHEMA_DIRS)
        raise FileNotFoundError(f"schema file not found for {kind}; searched: {searched}")
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"schema must be an object: {path}")
    return value


def _format_error(error: ValidationError) -> SchemaValidationError:
    path = ".".join(str(part) for part in error.absolute_path)
    code = str(error.validator)
    return SchemaValidationError(path=path, code=code, message=error.message)
