from alastria_identity.services import IdentityConfigBuilder, ContractParser


def main():
    # We generate the config based on the markdown url
    CONTRACTS_INFO_URL = 'https://raw.githubusercontent.com/alastria/alastria-identity/master/contracts/ContractInfo.md'
    builder = IdentityConfigBuilder(
        contracts_info_url=CONTRACTS_INFO_URL,
        parser_class=ContractParser
    )
    config = builder.generate()

    # This is the format of the config
    print(config)


if __name__ == '__main__':
    main()
