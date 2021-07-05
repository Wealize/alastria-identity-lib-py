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

    # Non delegated call
    PROVIDER_NODE_URL = os.environ.get(
        'PROVIDER_NODE_URL', 'https://127.0.0.1/rpc')
    web3_endpoint = Web3(Web3.HTTPProvider(PROVIDER_NODE_URL))

    PRESENTATION_REGISTRY_ADDRESS = '0x123'
    transaction_service = TransactionService(
        config,
        'AlastriaPresentationRegistry',
        PRESENTATION_REGISTRY_ADDRESS,
        web3_endpoint)

    DELEGATED_ADDRESS = '0x12345'
    receiver_presentation_hash, status = 'myhash', 'active'
    transaction_service.set_delegated(
        DELEGATED_ADDRESS
    ).generate_transaction(
        'updateReceiverPresentation', [receiver_presentation_hash, status])

if __name__ == '__main__':
    main()
