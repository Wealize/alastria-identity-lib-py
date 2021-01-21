from web3 import Web3

from alastria_identity.types import (Transaction, NetworkDid)
from alastria_identity.services import (
    ContractsService,
    PUBLIC_KEY_REGISTRY_ADDRESS
)


class PublicKeyService:
    def __init__(self, endpoint: Web3):
        self.endpoint = endpoint

    def add_key(self, public_key: str) -> Transaction:
        return self._build_transaction(
            "addKey",
            [public_key],
            delegated=True)

    def revoke_public_key(self, public_key: str) -> Transaction:
        return self._build_transaction(
            "revokePublicKey",
            [public_key],
            delegated=True)

    def delete_public_key(self, public_key: str) -> Transaction:
        return self._build_transaction(
            "deletePublicKey",
            [public_key],
            delegated=True)

    def get_current_public_key(self, did: str) -> Transaction:
        subject_address = NetworkDid.from_did(did).proxy_address
        return self._build_transaction(
            "getCurrentPublicKey",
            [subject_address],
            delegated=False)

    def get_public_key_status(self, did: str, public_key: str) -> Transaction:
        subject_address = NetworkDid.from_did(did).proxy_address
        return self._build_transaction(
            "getPublicKeyStatus",
            [subject_address, public_key],
            delegated=False)

    def _build_transaction(self, function_name: str, args: list, delegated: bool) -> Transaction:
        encoded_abi = ContractsService.AlastriaPublicKeyRegistry(self.endpoint).encodeABI(
            fn_name=function_name,
            args=args
        )

        data = self.delegated(encoded_abi) if delegated else encoded_abi

        return Transaction(
            to=Web3.toChecksumAddress(PUBLIC_KEY_REGISTRY_ADDRESS),
            data=data)

    def delegated(self, delegated_data) -> str:
        return ContractsService.AlastriaIdentityManager(self.endpoint).encodeABI(
            fn_name='delegateCall',
            args=[Web3.toChecksumAddress(
                PUBLIC_KEY_REGISTRY_ADDRESS), 0, delegated_data]
        )
