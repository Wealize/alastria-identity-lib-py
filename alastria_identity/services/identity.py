from typing import List
from dataclasses import asdict
from eth_account.account import SignedTransaction, HexBytes

from alastria_identity.types import UserIdentity, Transaction, DEFAULT_NONCE


class UserIdentityService:
    def __init__(self, identity: UserIdentity):
        self.identity = identity

    def add_transaction(self, transaction: Transaction) -> None:
        self.identity.transactions.append(transaction)

    def get_signed_transactions(self) -> List:
        return map(self.sign_transaction, self.identity.transactions)

    def get_signed_transaction_from_anonymous(self, transaction: Transaction) -> HexBytes:
        user_transaction = self.update_transaction_nonce(transaction)
        return self.sign_transaction(user_transaction)

    def update_transaction_nonce(self, transaction: Transaction) -> Transaction:
        if transaction.nonce == DEFAULT_NONCE:
            transaction.nonce = self.identity.endpoint.eth.getTransactionCount(
                self.identity.address)
        return transaction

    def sign_transaction(self, transaction: Transaction) -> HexBytes:
        signed_transaction: SignedTransaction = self.identity.endpoint.eth.account.sign_transaction(
            asdict(transaction), self.identity.private_key)
        return signed_transaction.rawTransaction
