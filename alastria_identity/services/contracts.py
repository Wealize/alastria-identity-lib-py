from web3 import Web3
from web3.contract import Contract

from alastria_identity.exceptions import ContractNameError

IDENTITY_MANAGER_ADDRESS = '0xbd4a2c84edb97be5beff7cd341bd63567e73f8c9'
PUBLIC_KEY_REGISTRY_ADDRESS = '0x4958091227bbfbe1fdfc0fd79fc44844dc014ca0'
PRESENTATION_REGISTRY_ADDRESS = '0x54d1dbfacada17ff39f2bac08e05fbdb4659f671'
CREDENTIAL_REGISTRY_ADDRESS = '0x7bbca11cbd86b562136d5708eba40f4bc0aa1ddc'


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
