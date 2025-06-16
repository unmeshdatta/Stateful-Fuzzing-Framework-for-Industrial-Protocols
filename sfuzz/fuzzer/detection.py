"""Simple anomaly detection."""
from __future__ import annotations


def detect_anomaly(response: bytes) -> bool:
    """Very naive detection of anomalies."""
    return b"error" in response.lower() or response == b""
