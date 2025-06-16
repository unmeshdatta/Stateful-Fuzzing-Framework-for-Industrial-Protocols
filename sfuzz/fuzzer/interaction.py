"""Target interaction engine."""
from __future__ import annotations

import socket
from dataclasses import dataclass
from typing import Optional


@dataclass
class Target:
    host: str
    port: int


class InteractionEngine:
    def __init__(self, target: Target, timeout: float = 1.0):
        self.target = target
        self.timeout = timeout
        self.sock: Optional[socket.socket] = None

    def connect(self):
        self.sock = socket.create_connection((self.target.host, self.target.port), timeout=self.timeout)

    def send(self, data: bytes) -> bytes:
        assert self.sock, "Not connected"
        self.sock.sendall(data)
        return self.sock.recv(4096)

    def close(self):
        if self.sock:
            self.sock.close()
            self.sock = None
