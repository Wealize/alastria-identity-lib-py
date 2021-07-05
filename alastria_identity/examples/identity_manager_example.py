import os

from web3 import Web3

from alastria_identity.services import (
    IdentityConfigBuilder, ContractParser, TransactionService)
from alastria_identity.types import NetworkDid


def main():
    # We generate the config based on the markdown url
    CONTRACTS_INFO_URL = 'https://raw.githubusercontent.com/alastria/alastria-identity/master/contracts/ContractInfo.md'
    builder = IdentityConfigBuilder(
        contracts_info_url=CONTRACTS_INFO_URL,
        parser_class=ContractParser
    )
    config = builder.generate()

    # Non delegated call
    PROVIDER_NODE_URL = os.environ.get(
        'PROVIDER_NODE_URL', 'https://127.0.0.1/rpc')
    web3_endpoint = Web3(Web3.HTTPProvider(PROVIDER_NODE_URL))

    IDENTITY_MANAGER_ADDRESS = '0x123'
    transaction_service = TransactionService(
        config,
        'AlastriaIdentityManager',
        IDENTITY_MANAGER_ADDRESS,
        web3_endpoint)

    DELEGATED_ADDRESS = '0x12345'
    sign_did = 'mydid:123456'

    # We can use NetworkDid to get the proxy_address out of a did
    sign_address = NetworkDid.from_did(sign_did).proxy_address

    transaction_service.set_delegated(
        DELEGATED_ADDRESS
    ).generate_transaction(
        'prepareAlastriaID', [sign_address])

if __name__ == '__main__':
    main()