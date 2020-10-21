from alastria_identity.services import IdentityConfigBuilder
from alastria_identity.services import ContractParser


def main():
    builder = IdentityConfigBuilder(
        'https://raw.githubusercontent.com/alastria/alastria-identity/master/contracts/ContractInfo.md',
        ContractParser
    )
    config = builder.generate()
    print(config)


if __name__ == '__main__':
    main()
