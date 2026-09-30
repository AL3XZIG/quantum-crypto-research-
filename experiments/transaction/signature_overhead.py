"""Модель накладных расходов от размера цифровой подписи."""

def total_signature_bytes(signature_size: int, signatures: int) -> int:
    return signature_size * signatures

def main() -> None:
    print("Transaction overhead model")

if __name__ == "__main__":
    main()
