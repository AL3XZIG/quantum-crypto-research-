"""Единая точка запуска сравнительного эксперимента ECDSA vs ML-DSA."""

from __future__ import annotations

import csv
from dataclasses import asdict
from pathlib import Path

from experiments.signatures.ecdsa_benchmark import benchmark as benchmark_ecdsa
from experiments.signatures.mldsa_benchmark import benchmark as benchmark_mldsa

RESULT_PATH = Path("data/signature_benchmark.csv")


def main() -> None:
    results = [benchmark_ecdsa(), benchmark_mldsa()]
    RESULT_PATH.parent.mkdir(parents=True, exist_ok=True)

    with RESULT_PATH.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=asdict(results[0]).keys())
        writer.writeheader()
        for result in results:
            writer.writerow(asdict(result))

    print(f"Saved results to {RESULT_PATH}")
    for result in results:
        print(result)


if __name__ == "__main__":
    main()
