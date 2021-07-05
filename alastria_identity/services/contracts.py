from web3 import Web3
from web3.contract import Contract

from alastria_identity.exceptions import ContractNameError


class ContractsService:
    def __init__(self, config):
        self.config = config

    def get_contract_handler(
        self, contract_name: str, endpoint: Web3
    ) -> Contract:
        return endpoint.eth.contract(
            abi=self.get_abi_by_contract_name(contract_name))

    def get_abi_by_contract_name(self, contract_name: str) -> list:
        try:
            contract_config = self.config[contract_name]
        except KeyError:
            raise ContractNameError(f'The contract {contract_name} does not exist')

        return [action for action in contract_config.values()]
