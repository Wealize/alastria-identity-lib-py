import os

from web3 import Web3

from alastria_identity.services import (
    IdentityConfigBuilder, ContractParser, TransactionService)


def main():
    # We generate the config based on the markdown url
    CONTRACTS_INFO_URL = os.environ.get(
        'CONTRACTS_INFO_URL',
        'https://raw.githubusercontent.com/alastria/alastria-identity/master/contracts/ContractInfo.md')
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
        config, 'AlastriaCredentialRegistry', web3_endpoint)

    subject_status, issuer_status = 1, 1
    transaction_service.generate_transaction(
        'getCredentialStatus', [subject_status, issuer_status])

    issuer_credential_hash, status = b'dummy', 1
    transaction_service.enable_delegated_call().generate_transaction(
        'updateCredentialStatus', [issuer_credential_hash, status])


if __name__ == '__main__':
    main()
