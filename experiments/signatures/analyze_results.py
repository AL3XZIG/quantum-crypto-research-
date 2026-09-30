"""Анализ результатов бенчмарка цифровых подписей.

Скрипт не меняет исходные CSV-данные. Он создаёт сводную таблицу и графики,
которые можно использовать как основу для экспериментального раздела статьи.
"""

from __future__ import annotations

import argparse
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


ROOT = Path(__file__).resolve().parents[2]
DEFAULT_INPUT = ROOT / "data" / "signature_benchmark.csv"
DEFAULT_OUTPUT = ROOT / "results"


def load_results(path: Path) -> pd.DataFrame:
    df = pd.read_csv(path)
    required = {
        "algorithm",
        "parameter",
        "keygen_ms",
        "sign_ms",
        "verify_ms",
        "public_key_bytes",
        "private_key_bytes",
        "signature_bytes",
    }
    missing = required.difference(df.columns)
    if missing:
        raise ValueError(f"Missing columns: {sorted(missing)}")
    if df.empty:
        raise ValueError("Benchmark CSV is empty.")
    return df


def make_time_plot(df: pd.DataFrame, output: Path) -> None:
    ax = df.set_index("algorithm")[["keygen_ms", "sign_ms", "verify_ms"]].plot(
        kind="bar",
        figsize=(9, 5),
        logy=True,
    )
    ax.set_ylabel("Time, ms (log scale)")
    ax.set_xlabel("")
    ax.set_title("Digital signature benchmark")
    ax.legend(["KeyGen", "Sign", "Verify"])
    fig = ax.get_figure()
    fig.tight_layout()
    fig.savefig(output, dpi=180)
    plt.close(fig)


def make_size_plot(df: pd.DataFrame, output: Path) -> None:
    ax = df.set_index("algorithm")[
        ["public_key_bytes", "private_key_bytes", "signature_bytes"]
    ].plot(kind="bar", figsize=(9, 5))
    ax.set_ylabel("Bytes")
    ax.set_xlabel("")
    ax.set_title("Key and signature sizes")
    ax.legend(["Public key", "Private key", "Signature"])
    fig = ax.get_figure()
    fig.tight_layout()
    fig.savefig(output, dpi=180)
    plt.close(fig)


def write_summary(df: pd.DataFrame, output: Path) -> None:
    columns = [
        "algorithm",
        "parameter",
        "keygen_ms",
        "sign_ms",
        "verify_ms",
        "public_key_bytes",
        "private_key_bytes",
        "signature_bytes",
    ]
    df[columns].to_csv(output, index=False)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()

    df = load_results(args.input)
    figures = args.output / "figures"
    tables = args.output / "tables"
    figures.mkdir(parents=True, exist_ok=True)
    tables.mkdir(parents=True, exist_ok=True)

    make_time_plot(df, figures / "signature_times.png")
    make_size_plot(df, figures / "signature_sizes.png")
    write_summary(df, tables / "signature_benchmark_summary.csv")

    print(f"Figures written to {figures}")
    print(f"Summary written to {tables}")


if __name__ == "__main__":
    main()
