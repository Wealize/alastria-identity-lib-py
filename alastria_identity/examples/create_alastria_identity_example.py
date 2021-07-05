import os

from web3 import Web3

from alastria_identity.services import (
    IdentityConfigBuilder, ContractParser, TransactionService)


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
    PRESENTATION_REGISTRY_ADDRESS = '0x123'
    IDENTITY_MANAGER_ADDRESS = '0x123'
    public_key = 'mykey'

    transaction_service = TransactionService(
        config,
        'AlastriaPublicKeyRegistry',
        PRESENTATION_REGISTRY_ADDRESS,
        web3_instance)
    public_key_response = transaction_service.generate_transaction(
        'addKey',
        [public_key]
    )

    transaction_service = TransactionService(
        config,
        'AlastriaIdentityManager',
        IDENTITY_MANAGER_ADDRESS,
        web3_instance)
    transaction_service.generate_transaction(
        'createAlastriaIdentity',
        [public_key_response]
    )


if __name__ == '__main__':
    main()
