from mock import Mock, patch
from unittest.mock import patch

from web3 import Web3

from alastria_identity.services import IdentityConfigBuilder, ContractParser


def test_extract_contract_item_from_response():
    contracts_content = '''| Contract Name | Address | ABI |
| :------------ | :-------| :--- |
| Eidas | 0x57a9604784f82e5637624ca9c87015aaa31e300d | https://github.com/alastria/alastria-identity/blob/develop/contracts/abi/__contracts_libs_Eidas_sol_Eidas.abi |
| AlastriaIdentityManager | 0xbd4a2c84edb97be5beff7cd341bd63567e73f8c9 | https://github.com/alastria/alastria-identity/blob/develop/contracts/abi/__contracts_identityManager_AlastriaIdentityManager_sol_AlastriaIdentityManager.abi |
'''
    expected_output = [
        {'url': 'https://github.com/alastria/alastria-identity/blob/develop/contracts/abi/__contracts_libs_Eidas_sol_Eidas.abi',
          'address': '0x57a9604784f82e5637624ca9c87015aaa31e300d'},
        {'url': 'https://github.com/alastria/alastria-identity/blob/develop/contracts/abi/__contracts_identityManager_AlastriaIdentityManager_sol_AlastriaIdentityManager.abi',
          'address': '0xbd4a2c84edb97be5beff7cd341bd63567e73f8c9'}
    ]

    identity = IdentityConfigBuilder(
        contracts_info_url= 'https://raw.githubusercontent.com/alastria/alastria-identity/master/contracts/ContractInfo.md',
        parser_class=ContractParser)

    output = identity.extract_contract_item_from_response(contracts_content)

    assert list(output) == expected_output


@patch.object(IdentityConfigBuilder, 'get_contracts')
def test_generate_return_valid_contracts(get_contracts):
    # We should mock the request response with responses in the future
    expected_output = {
      'Eidas': {
        'functions': [],
        'address': '0x57a9604784f82e5637624ca9c87015aaa31e300d'
      },
      'AlastriaIdentityManager': {
        'functions': [],
        'address': '0xbd4a2c84edb97be5beff7cd341bd63567e73f8c9'
      },
    }
    get_contracts.return_value = [
        {'url': 'https://github.com/alastria/alastria-identity/blob/develop/contracts/abi/__contracts_libs_Eidas_sol_Eidas.abi',
         'address': '0x57a9604784f82e5637624ca9c87015aaa31e300d'},
        {'url': 'https://github.com/alastria/alastria-identity/blob/develop/contracts/abi/__contracts_identityManager_AlastriaIdentityManager_sol_AlastriaIdentityManager.abi',
         'address': '0xbd4a2c84edb97be5beff7cd341bd63567e73f8c9'}
    ]

    identity = IdentityConfigBuilder(
        contracts_info_url= 'https://raw.githubusercontent.com/alastria/alastria-identity/master/contracts/ContractInfo.md',
        parser_class=ContractParser)

    config_output = identity.generate()

    assert config_output.keys() == expected_output.keys()
