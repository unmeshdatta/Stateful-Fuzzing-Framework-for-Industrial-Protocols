"""Reporting utilities."""
from __future__ import annotations

import json
from dataclasses import dataclass, asdict
from typing import List


@dataclass
class Finding:
    description: str
    payload: bytes


class Report:
    def __init__(self):
        self.findings: List[Finding] = []

    def add_finding(self, description: str, payload: bytes):
        self.findings.append(Finding(description, payload))

    def to_json(self) -> str:
        return json.dumps([asdict(f) for f in self.findings], indent=2)
