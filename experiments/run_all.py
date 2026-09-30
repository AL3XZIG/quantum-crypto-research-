"""Запуск полного прототипа исследования."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def run(module: str, *args: str) -> None:
    command = [sys.executable, "-m", module, *args]
    subprocess.run(command, cwd=ROOT, check=True)


def main() -> None:
    run("experiments.grover.grover_model")
    run("experiments.signatures.run_benchmark", "--repetitions", "100")
    run("experiments.signatures.analyze_results")


if __name__ == "__main__":
    main()
