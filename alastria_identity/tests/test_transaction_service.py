from mock import Mock, patch
from unittest.mock import patch

from web3 import Web3

from alastria_identity.services import TransactionService
from alastria_identity.types import Transaction


def test_is_delegated_call_return_false():
    contract_config = {'ContractName': {'address': '0x123', 'functions': {}}}
    transaction = TransactionService(
        config=contract_config,
        contract_name='ContractName',
        endpoint=Web3(Web3.HTTPProvider('https://127.0.0.1/rpc'))
    )

    is_delegated = transaction.is_delegated_call()

    assert not is_delegated


def test_is_delegated_call_return_true():
    contract_config = {
        'AlastriaIdentityManager': {
            'address': '0x123',
            'functions': {'myfunction': {'constant':True,'inputs':[{'name':'','type':'address'}],'name':'identityKeys','outputs':[{'name':'','type':'address'}],'payable':False,'stateMutability':'view','type':'function'}}}}
    transaction = TransactionService(
        config=contract_config,
        contract_name='AlastriaIdentityManager',
        endpoint=Web3(Web3.HTTPProvider('https://127.0.0.1/rpc'))
    )
    transaction.enable_delegated_call()

    is_delegated = transaction.is_delegated_call()

    assert is_delegated
