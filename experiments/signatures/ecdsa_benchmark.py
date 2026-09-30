"""Реальный бенчмарк ECDSA P-256."""

from __future__ import annotations

from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives.serialization import Encoding, PublicFormat

from experiments.signatures.benchmark import BenchmarkResult, measure_ms

MESSAGE = b"quantum-crypto-research benchmark message"


def generate_key() -> ec.EllipticCurvePrivateKey:
    return ec.generate_private_key(ec.SECP256R1())


def benchmark(repetitions: int = 100) -> BenchmarkResult:
    key = generate_key()
    public_key = key.public_key()
    signature = key.sign(MESSAGE, ec.ECDSA(hashes.SHA256()))

    if not _verify(public_key, signature):
        raise RuntimeError("ECDSA verification failed.")

    private_key_bytes = key.private_bytes(
        Encoding.DER,
        serialization.PrivateFormat.PKCS8,
        serialization.NoEncryption(),
    )
    public_key_bytes = public_key.public_bytes(
        Encoding.DER,
        PublicFormat.SubjectPublicKeyInfo,
    )

    return BenchmarkResult(
        algorithm="ECDSA",
        parameter="P-256 / SHA-256",
        keygen_ms=measure_ms(generate_key, repetitions=repetitions),
        sign_ms=measure_ms(
            lambda: key.sign(MESSAGE, ec.ECDSA(hashes.SHA256())),
            repetitions=repetitions,
        ),
        verify_ms=measure_ms(
            lambda: _verify(public_key, signature),
            repetitions=repetitions,
        ),
        public_key_bytes=len(public_key_bytes),
        private_key_bytes=len(private_key_bytes),
        signature_bytes=len(signature),
    )


def _verify(public_key: ec.EllipticCurvePublicKey, signature: bytes) -> bool:
    try:
        public_key.verify(signature, MESSAGE, ec.ECDSA(hashes.SHA256()))
    except Exception:
        return False
    return True


def main() -> None:
    result = benchmark()
    print(result)


if __name__ == "__main__":
    main()
