"""Эксперимент ECDSA — первая реальная криптографическая реализация."""

from cryptography.hazmat.primitives.asymmetric import ec

def generate_key():
    return ec.generate_private_key(ec.SECP256R1())

def main() -> None:
    key = generate_key()
    print("ECDSA:", key.curve.name)

if __name__ == "__main__":
    main()
