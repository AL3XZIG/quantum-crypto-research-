"""Реальный бенчмарк ML-DSA через Open Quantum Safe (liboqs)."""

from __future__ import annotations

from experiments.signatures.benchmark import BenchmarkResult, measure_ms

MESSAGE = b"quantum-crypto-research benchmark message"
ALGORITHM = "ML-DSA-65"


def benchmark(repetitions: int = 30) -> BenchmarkResult:
    try:
        import oqs
    except ImportError as exc:
        raise RuntimeError(
            "Не найден liboqs-python. Установите зависимости из requirements.txt."
        ) from exc

    if ALGORITHM not in oqs.get_enabled_sig_mechanisms():
        raise RuntimeError(
            f"{ALGORITHM} недоступен в установленной сборке liboqs. "
            f"Доступные алгоритмы: {oqs.get_enabled_sig_mechanisms()}"
        )

    with oqs.Signature(ALGORITHM) as signer:
        public_key = signer.generate_keypair()
        private_key = signer.export_secret_key()

        signature = signer.sign(MESSAGE)
        if not signer.verify(MESSAGE, signature, public_key):
            raise RuntimeError("ML-DSA verification failed.")

        keygen_ms = measure_ms(
            lambda: _generate_keypair(oqs, ALGORITHM),
            repetitions=repetitions,
        )
        sign_ms = measure_ms(
            lambda: signer.sign(MESSAGE),
            repetitions=repetitions,
        )
        verify_ms = measure_ms(
            lambda: signer.verify(MESSAGE, signature, public_key),
            repetitions=repetitions,
        )

        return BenchmarkResult(
            algorithm=ALGORITHM,
            parameter=ALGORITHM,
            keygen_ms=keygen_ms,
            sign_ms=sign_ms,
            verify_ms=verify_ms,
            public_key_bytes=len(public_key),
            private_key_bytes=len(private_key),
            signature_bytes=len(signature),
        )


def _generate_keypair(oqs, algorithm: str) -> None:
    with oqs.Signature(algorithm) as signer:
        signer.generate_keypair()


def main() -> None:
    result = benchmark()
    print(result)


if __name__ == "__main__":
    main()
