from dataclasses import dataclass
from pathlib import Path


class ScriptError(Exception):
    "An operation script is invalid or failed while running"


@dataclass
class Operation:
    name: str
    filename: str
    code: object


def load_operation(path: Path) -> Operation:
    source = path.read_text()
    code = compile(source, path.name, "exec")
    return Operation(path.stem, path.name, code)
