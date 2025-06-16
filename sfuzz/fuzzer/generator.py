"""Fuzzing test case generator."""
import os
import random
from typing import Iterable


class TestCaseGenerator:
    def __init__(self, mutations: Iterable[bytes] | None = None):
        self.mutations = list(mutations or [])

    def mutate(self, data: bytes) -> bytes:
        if not self.mutations:
            # simple byte flip
            index = random.randint(0, len(data) - 1)
            flipped = bytes([data[index] ^ 0xFF])
            return data[:index] + flipped + data[index + 1 :]
        else:
            mutation = random.choice(self.mutations)
            index = random.randint(0, len(data))
            return data[:index] + mutation + data[index:]
