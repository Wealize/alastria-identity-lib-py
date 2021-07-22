from mock import Mock, patch, MagicMock
from unittest.mock import patch

from web3 import Web3

from alastria_identity.services import UserIdentityService
from alastria_identity.types import UserIdentity, Transaction


def test_update_transaction_nonce():
    endpoint = MagicMock()
    endpoint.eth.getTransactionCount.return_value = 3
    default_nonce = 1
    user_identity = UserIdentity(
        endpoint=endpoint,
        address='0x123',
        private_key='1234',
        nonce=default_nonce,
        transactions=[]
    )
    transaction = Transaction()

    identity = UserIdentityService(user_identity)

    updated_transaction = identity.update_transaction_nonce(transaction)

    assert updated_transaction.nonce != default_nonce
