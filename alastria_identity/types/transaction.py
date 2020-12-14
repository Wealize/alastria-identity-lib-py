from dataclasses import dataclass


@dataclass
class Transaction:
    to: str = '0x0000000000000000000000000000000000000000'
    data: str = '0x0'
    gasPrice: int = 0
    nonce: str = '0x0'
