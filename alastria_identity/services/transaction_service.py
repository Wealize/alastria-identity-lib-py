from web3 import Web3

from alastria_identity.types import (Transaction, NetworkDid)
from alastria_identity.services import (
    ContractsService,
    CREDENTIAL_REGISTRY_ADDRESS,
    IDENTITY_MANAGER_ADDRESS)


class TransactionService:
    DEFAULT_DELEGATED_FUNCTION_NAME = 'delegateCall'
    DEFAULT_CONTRACT_DELEGATED_NAME = 'AlastriaIdentityManager'

    def __init__(self, config, contract_name, contract_address):
        self.contract_name = contract_name
        self.contract_address = contract_address
        self.contract_handler = ContractsService(
            self.config
        ).get_contract_handler(
            contract_name, self.endpoint)
        self.delegated_call_address = None
        self.identity_manager_contract = ContractsService(
            self.config
        ).get_contract_handler(
            self.DEFAULT_CONTRACT_DELEGATED_NAME,
            self.endpoint)

    def set_delegated_call(self, delegated_call_address: str):
        self.delegated_call_address = delegated_call_address
        return self

    def generate_transaction(
        self, function_name: str, args: list
    ) -> Transaction:
        encoded_abi  = self.contract_handler.encodeABI(
            fn_name=function_name,
            args=args)

        payload = encoded_abi

        if self.is_delegated_call():
            payload = self.delegated(encoded_abi)

        contract_address = self.delegated_call_address or self.contract_address

        return Transaction(
            to=Web3.toChecksumAddress(contract_address),
            data=payload)

    def delegated(self, delegated_data) -> str:
        return self.identity_manager_contract.encodeABI(
            fn_name=self.DEFAULT_DELEGATED_FUNCTION_NAME,
            args=[Web3.toChecksumAddress(
                self.contract_address), 0, delegated_data]
        )

    def is_delegated_call(self):
        return bool(self.delegated_call_address)
