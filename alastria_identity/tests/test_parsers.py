from alastria_identity.services import ContractParser


def test_get_name_in_content_return_constructor():
    expected_name = 'constructor'
    contract_url = 'http://example.com'
    content = {
        "constant": True,
        "inputs": [{
            "name": "",
            "type": "address"
        }],
        "name": "identityKeys",
        "outputs": [{
            "name": "",
            "type": "address"
        }],
        "payable": False,
        "stateMutability": "view",
        "type": "constructor"
    }
    parser = ContractParser(contract_url)

    name = parser.get_name_in_content(content)

    assert name == expected_name

def test_get_name_in_content_return_item_with_name():
    expected_name = 'identityKeys'
    contract_url = 'http://example.com'
    content = {
        "constant": True,
        "inputs": [{
            "name": "",
            "type": "address"
        }],
        "name": "identityKeys",
        "outputs": [{
            "name": "",
            "type": "address"
        }],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    }
    parser = ContractParser(contract_url)

    parser.get_name_in_content(content)
