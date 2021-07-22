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

    transaction_service = TransactionService(
        config,
        'AlastriaIdentityManager',
        web3_endpoint)

    SIGN_DID = os.environ.get(
        'SIGN_DID',
        'did:ala:quor:redT:ee2d1fe7b0d4571155c93497a7a9bde56fb87b40')

    # We can use NetworkDid to get the proxy_address out of a did
    sign_address = NetworkDid.from_did(SIGN_DID).proxy_address
    checksum = Web3.toChecksumAddress(sign_address)

    transaction_service.enable_delegated_call().generate_transaction(
        'prepareAlastriaID', [checksum])


if __name__ == '__main__':
    main()
