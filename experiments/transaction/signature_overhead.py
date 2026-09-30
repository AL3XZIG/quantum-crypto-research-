"""Модель влияния размера подписи на размер сообщения/транзакции."""


def total_signature_bytes(signature_size: int, signatures: int) -> int:
    return signature_size * signatures


def main() -> None:
    print("Transaction overhead model")
    print("TODO: добавить реальные размеры ECDSA и ML-DSA из измерений.")


if __name__ == "__main__":
    main()
