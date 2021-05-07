from web3 import Web3

from alastria_identity.types import (Transaction, NetworkDid)
from alastria_identity.services import (
    ContractsService,
    CREDENTIAL_REGISTRY_ADDRESS,
    IDENTITY_MANAGER_ADDRESS)


class CredentialRegistryService:
    def __init__(self, endpoint: Web3):
        self.endpoint = endpoint

    def add_subject_credential(self, subject_credential_hash: str, uri: str) -> Transaction:
        return self._build_transaction(
            "addSubjectCredential",
            [subject_credential_hash, uri],
            delegated=True)

    def delete_subject_credential(self, subject_credential_hash: str) -> Transaction:
        return self._build_transaction(
            "deleteSubjectCredential",
            [subject_credential_hash],
            delegated=True)

    def get_subject_credential_status(self, subject_did: str, subject_credential_hash: str) -> Transaction:
        subject_address = NetworkDid.from_did(subject_did).proxy_address
        return self._build_transaction(
            "getSubjectCredentialStatus",
            [subject_address, subject_credential_hash],
            delegated=False)

    def get_subject_credential_list(self, subject_did: str) -> Transaction:
        subject_address = NetworkDid.from_did(subject_did).proxy_address
        return self._build_transaction(
            "getSubjectCredentialList",
            [subject_address],
            delegated=False)

    def add_issuer_credential(self, issuer_credential_hash: str) -> Transaction:
        return self._build_transaction(
            "addIssuerCredential",
            [issuer_credential_hash],
            delegated=True)

    def get_issuer_credential_status(self, issuer_did: str, issuer_credential_hash: str) -> Transaction:
        issuer_address = NetworkDid.from_did(issuer_did).proxy_address
        return self._build_transaction(
            "getIssuerCredentialStatus",
            [issuer_address, issuer_credential_hash],
            delegated=False)

    def update_credential_status(self, issuer_credential_hash: str, status: int) -> Transaction:
        return self._build_transaction(
            "updateCredentialStatus",
            [issuer_credential_hash, status],
            delegated=True)

    def get_credential_status(self, subject_status: int, issuer_status: int) -> Transaction:
        return self._build_transaction(
            "getCredentialStatus",
            [subject_status, issuer_status],
            delegated=False)

    def _build_transaction(self, function_name: str, args: list, delegated: bool) -> Transaction:
        encoded_abi = ContractsService.AlastriaCredentialRegistry(self.endpoint).encodeABI(
            fn_name=function_name,
            args=args
        )

        data = self.delegated(encoded_abi) if delegated else encoded_abi
        contract_address = IDENTITY_MANAGER_ADDRESS if delegated else CREDENTIAL_REGISTRY_ADDRESS

        return Transaction(
            to=Web3.toChecksumAddress(contract_address),
            data=data)

    def delegated(self, delegated_data) -> str:
        return ContractsService.AlastriaIdentityManager(self.endpoint).encodeABI(
            fn_name='delegateCall',
            args=[Web3.toChecksumAddress(
                CREDENTIAL_REGISTRY_ADDRESS), 0, delegated_data]
        )
