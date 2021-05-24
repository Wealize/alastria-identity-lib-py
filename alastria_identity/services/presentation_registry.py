from web3 import Web3

from alastria_identity.types import (Transaction, NetworkDid)
from alastria_identity.services import (
    ContractsService,
    PRESENTATION_REGISTRY_ADDRESS,
    IDENTITY_MANAGER_ADDRESS)


class PresentationRegistryService:
    def __init__(self, endpoint: Web3):
        self.endpoint = endpoint

    def add_subject_presentation(self, subject_presentation_hash: str, uri: str) -> Transaction:
        return self._build_transaction(
            "addSubjectPresentation",
            [subject_presentation_hash, uri],
            delegated=True)

    def update_subject_presentation(self, subject_presentation_hash: str, status: int) -> Transaction:
        return self._build_transaction(
            "updateSubjectPresentation",
            [subject_presentation_hash, status],
            delegated=True
        )

    def get_subject_presentation_status(self, subject_did: str, subject_presentation_hash: str) -> Transaction:
        subject_address = NetworkDid.from_did(subject_did).proxy_address
        return self._build_transaction(
            "getSubjectPresentationStatus",
            [subject_address, subject_presentation_hash],
            delegated=False
        )

    def get_subject_presentation_list(self, subject_did: str) -> Transaction:
        subject_address = NetworkDid.from_did(subject_did).proxy_address
        return self._build_transaction(
            "getSubjectPresentationList",
            [subject_address],
            delegated=False
        )

    def update_receiver_presentation(self, receiver_presentation_hash: str, status: int) -> Transaction:
        return self._build_transaction(
            "updateReceiverPresentation",
            [receiver_presentation_hash, status],
            delegated=True
        )

    def get_receiver_presentation_status(self, receiver_did: str, receiver_presentation_hash: str) -> Transaction:
        receiver_address = NetworkDid.from_did(receiver_did).proxy_address
        return self._build_transaction(
            "getReceiverPresentationStatus",
            [receiver_address, receiver_presentation_hash],
            delegated=False
        )

    def get_presentation_status(self, subject_status: int, receiver_status: int) -> Transaction:
        return self._build_transaction(
            "getPresentationStatus",
            [subject_status, receiver_status],
            delegated=False
        )

    def _build_transaction(self, function_name: str, args: list, delegated: bool) -> Transaction:
        encoded_abi = ContractsService.AlastriaPresentationRegistry(self.endpoint).encodeABI(
            fn_name=function_name,
            args=args
        )

        data = self.delegated(encoded_abi) if delegated else encoded_abi
        contract_address = IDENTITY_MANAGER_ADDRESS if delegated else PRESENTATION_REGISTRY_ADDRESS

        return Transaction(
            to=Web3.toChecksumAddress(contract_address),
            data=data)

    def delegated(self, delegated_data) -> str:
        return ContractsService.AlastriaIdentityManager(self.endpoint).encodeABI(
            fn_name='delegateCall',
            args=[Web3.toChecksumAddress(
                PRESENTATION_REGISTRY_ADDRESS), 0, delegated_data]
        )
