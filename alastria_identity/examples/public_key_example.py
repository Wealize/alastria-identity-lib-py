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

    transaction_service = TransactionService(
        config,
        'AlastriaPublicKeyRegistry',
        web3_endpoint)

    subject_address = Web3.toChecksumAddress('0xee2d1fe7b0d4571155c93497a7a9bde56fb87b40')
    public_key = b'12345'
    transaction_service.generate_transaction(
        'getPublicKeyStatus', [subject_address, public_key])

    transaction_service.enable_delegated_call().generate_transaction(
        'deletePublicKey', [subject_address])

if __name__ == '__main__':
    main()
