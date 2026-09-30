"""Общие структуры и утилиты бенчмарка цифровых подписей."""

from dataclasses import dataclass
from time import perf_counter
from typing import Callable


@dataclass
class BenchmarkResult:
    algorithm: str
    parameter: str
    keygen_ms: float
    sign_ms: float
    verify_ms: float
    public_key_bytes: int
    private_key_bytes: int
    signature_bytes: int


def measure_ms(function: Callable[[], object], repetitions: int = 100) -> float:
    start = perf_counter()
    for _ in range(repetitions):
        function()
    return (perf_counter() - start) * 1000 / repetitions
