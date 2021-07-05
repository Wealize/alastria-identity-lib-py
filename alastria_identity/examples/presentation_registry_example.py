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
    PRESENTATION_REGISTRY_ADDRESS = '0x123'
    transaction_service = TransactionService(
        config, 'AlastriaPresentationRegistry', PRESENTATION_REGISTRY_ADDRESS)

    DELEGATED_ADDRESS = '0x12345'
    receiver_presentation_hash, status = 'myhash', 'active'
    transaction_service.set_delegated(
        DELEGATED_ADDRESS
    ).generate_transaction(
        'updateReceiverPresentation', [receiver_presentation_hash, status])

if __name__ == '__main__':
    main()
