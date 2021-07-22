import os

from web3 import Web3

from alastria_identity.services import (
    IdentityConfigBuilder, ContractParser, TransactionService)
from alastria_identity.types import Transaction


def main():
    # We generate the config based on the markdown url
    CONTRACTS_INFO_URL = 'https://raw.githubusercontent.com/alastria/alastria-identity/master/contracts/ContractInfo.md'
    builder = IdentityConfigBuilder(
        contracts_info_url=CONTRACTS_INFO_URL,
        parser_class=ContractParser
    )
    config = builder.generate()

    PROVIDER_NODE_URL = os.environ.get(
        'PROVIDER_NODE_URL', 'https://127.0.0.1/rpc')
    web3_instance = Web3(Web3.HTTPProvider(PROVIDER_NODE_URL))

    # Non delegated call
    PUBLIC_KEY = os.environ.get('PUBLIC_KEY', 'mykey')

    transaction_service = TransactionService(
        config,
        'AlastriaPublicKeyRegistry',
        web3_instance)
    transaction_response: Transaction = transaction_service.generate_transaction(
        'addKey',
        [PUBLIC_KEY]
    )

    transaction_service = TransactionService(
        config,
        'AlastriaIdentityManager',
        web3_instance)
    transaction_response: Transaction = transaction_service.generate_transaction(
        'createAlastriaIdentity',
        [transaction_response.data]
    )


if __name__ == '__main__':
    main()
