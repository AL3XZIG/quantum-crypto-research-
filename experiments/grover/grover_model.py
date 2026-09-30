"""Идеализированная модель классического поиска и алгоритма Гровера."""

from pathlib import Path
import csv
import math

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "data" / "grover_results.csv"

def classical_work(n: int) -> float:
    return float(n)

def grover_work(n: int) -> float:
    return math.sqrt(n)

def generate_results() -> list[dict]:
    sizes = [2**8, 2**12, 2**16, 2**20, 2**24, 2**28, 2**32, 2**40, 2**48, 2**56, 2**64]
    return [{"search_space": n, "classical_work": classical_work(n),
             "grover_idealized_work": grover_work(n),
             "speedup": classical_work(n) / grover_work(n)} for n in sizes]

def save_results(rows: list[dict]) -> None:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with OUTPUT.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=[
            "search_space", "classical_work", "grover_idealized_work", "speedup"
        ])
        writer.writeheader()
        writer.writerows(rows)

def main() -> None:
    rows = generate_results()
    save_results(rows)
    print(f"Saved {len(rows)} rows to {OUTPUT}")

if __name__ == "__main__":
    main()
