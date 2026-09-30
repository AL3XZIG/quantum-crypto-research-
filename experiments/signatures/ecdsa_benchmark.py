"""Заготовка эксперимента ECDSA."""

from cryptography.hazmat.primitives.asymmetric import ec


def generate_key():
    """Создать ключ ECDSA P-256."""
    return ec.generate_private_key(ec.SECP256R1())


def main() -> None:
    key = generate_key()
    print("ECDSA P-256 key generated:", key.curve.name)


if __name__ == "__main__":
    main()
