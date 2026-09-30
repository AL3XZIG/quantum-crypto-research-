"""Общий каркас бенчмарка цифровых подписей.

На первом этапе здесь определён единый формат результата.
Конкретные реализации ECDSA и ML-DSA подключаются отдельно.
"""

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


def measure_ms(function: Callable, repetitions: int = 100) -> float:
    """Среднее время выполнения функции в миллисекундах."""
    start = perf_counter()

    for _ in range(repetitions):
        function()

    elapsed = perf_counter() - start
    return elapsed * 1000 / repetitions


def run() -> None:
    raise NotImplementedError(
        "Подключите реализации ECDSA и ML-DSA перед запуском benchmark."
    )


if __name__ == "__main__":
    run()
