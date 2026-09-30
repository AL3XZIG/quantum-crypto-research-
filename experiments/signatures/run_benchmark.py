"""Единая точка запуска сравнительного эксперимента ECDSA vs ML-DSA."""

from __future__ import annotations

import argparse
import csv
from dataclasses import asdict
from pathlib import Path

from experiments.signatures.ecdsa_benchmark import benchmark as benchmark_ecdsa
from experiments.signatures.mldsa_benchmark import benchmark as benchmark_mldsa

ROOT = Path(__file__).resolve().parents[2]
RESULT_PATH = ROOT / "data" / "signature_benchmark.csv"


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Benchmark ECDSA P-256 against ML-DSA-65."
    )
    parser.add_argument(
        "--repetitions",
        type=int,
        default=100,
        help="Number of timed repetitions for each operation.",
    )
    args = parser.parse_args()

    if args.repetitions < 2:
        parser.error("--repetitions must be >= 2")

    results = [
        benchmark_ecdsa(repetitions=args.repetitions),
        benchmark_mldsa(repetitions=max(30, args.repetitions // 2)),
    ]

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
