from web3 import Web3

from alastria_identity.types import (Transaction, NetworkDid)
from alastria_identity.services import ContractsService, IDENTITY_MANAGER_ADDRESS


class CredentialRegistryService:
    DEFAULT_GAS_LIMIT = 600000

    def __init__(self, endpoint: Web3):
        self.endpoint = endpoint

    def add_subject_credential(self, subject_credential_hash: str, uri: str) -> Transaction:
        data = self.delegated(ContractsService.AlastriaCredentialRegistry(self.endpoint).encodeABI(
            fn_name="addSubjectCredential",
            args=[subject_credential_hash, uri]
        ))

        return Transaction(
            to=IDENTITY_MANAGER_ADDRESS,
            data=data,
            gasPrice=self.DEFAULT_GAS_LIMIT)

    def delete_subject_credential(self, subject_credential_hash: str) -> Transaction:
        data = self.delegated(ContractsService.AlastriaCredentialRegistry(self.endpoint).encodeABI(
            fn_name="deleteSubjectCredential",
            args=[subject_credential_hash]
        ))

        return Transaction(
            to=IDENTITY_MANAGER_ADDRESS,
            data=data,
            gasPrice=self.DEFAULT_GAS_LIMIT)

    def get_subject_credential_status(self, subject_did: str, subject_credential_hash: str) -> Transaction:
        subject_address = NetworkDid.from_did(subject_did).proxy_address
        data = ContractsService.AlastriaCredentialRegistry(self.endpoint).encodeABI(
            fn_name="getSubjectCredentialStatus",
            args=[subject_address, subject_credential_hash]
        )

        return Transaction(
            to=IDENTITY_MANAGER_ADDRESS,
            data=data,
            gasPrice=self.DEFAULT_GAS_LIMIT)

    def get_subject_credential_list(self, subject_did: str) -> Transaction:
        subject_address = NetworkDid.from_did(subject_did).proxy_address
        data = ContractsService.AlastriaCredentialRegistry(self.endpoint).encodeABI(
            fn_name="getSubjectCredentialList",
            args=[subject_address]
        )

        return Transaction(
            to=IDENTITY_MANAGER_ADDRESS,
            data=data,
            gasPrice=self.DEFAULT_GAS_LIMIT)

    def add_issuer_credential(self, issuer_credential_hash: str) -> Transaction:
        data = self.delegated(ContractsService.AlastriaCredentialRegistry(self.endpoint).encodeABI(
            fn_name="addIssuerCredential",
            args=[issuer_credential_hash]
        ))

        return Transaction(
            to=IDENTITY_MANAGER_ADDRESS,
            data=data,
            gasPrice=self.DEFAULT_GAS_LIMIT)

    def get_issuer_credential_status(self, issuer_did: str, issuer_credential_hash: str) -> Transaction:
        issuer_address = NetworkDid.from_did(issuer_did).proxy_address
        data = ContractsService.AlastriaCredentialRegistry(self.endpoint).encodeABI(
            fn_name="getIssuerCredentialStatus",
            args=[issuer_address, issuer_credential_hash]
        )

        return Transaction(
            to=IDENTITY_MANAGER_ADDRESS,
            data=data,
            gasPrice=self.DEFAULT_GAS_LIMIT)

    def update_credential_status(self, issuer_credential_hash: str, status: int) -> Transaction:
        data = self.delegated(ContractsService.AlastriaCredentialRegistry(self.endpoint).encodeABI(
            fn_name="updateCredentialStatus",
            args=[issuer_credential_hash, status]
        ))

        return Transaction(
            to=IDENTITY_MANAGER_ADDRESS,
            data=data,
            gasPrice=self.DEFAULT_GAS_LIMIT)

    def get_credential_status(self, subject_status: int, issuer_status: int) -> Transaction:
        data = ContractsService.AlastriaCredentialRegistry(self.endpoint).encodeABI(
            fn_name="getCredentialStatus",
            args=[subject_status, issuer_status]
        )

        return Transaction(
            to=IDENTITY_MANAGER_ADDRESS,
            data=data,
            gasPrice=self.DEFAULT_GAS_LIMIT)

    def delegated(self, delegated_data) -> str:
        return ContractsService.AlastriaIdentityManager(self.endpoint).encodeABI(
            fn_name='delegateCall',
            args=[IDENTITY_MANAGER_ADDRESS, 0, delegated_data]
        )
