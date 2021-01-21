from mock import Mock, patch
from dataclasses import asdict
from unittest.mock import patch
from web3 import Web3

from alastria_identity.services import PUBLIC_KEY_REGISTRY_ADDRESS, PublicKeyService


@patch('alastria_identity.services.PublicKeyService.delegated')
@patch('alastria_identity.services.identity_manager.ContractsService.AlastriaPublicKeyRegistry')
def test_add_key(
    mock_alastria_add_public_key,
    mock_delegated
):
    web3_mock = Mock()
    public_key = '0x3'

    mock_alastria_add_public_key(
        web3_mock
    ).encodeABI.return_value = 'addKeyReturnValue'
    mock_delegated.return_value = 'delegatedReturnValue'

    expected_transaction = {
        'to': Web3.toChecksumAddress(PUBLIC_KEY_REGISTRY_ADDRESS),
        'data': 'delegatedReturnValue',
        'gasPrice': 0,
        'gas': 600000,
        'nonce': '0x0'
    }

    service = PublicKeyService(web3_mock)

    transaction = service.add_key(public_key)

    mock_alastria_add_public_key.assert_called_with(web3_mock)
    mock_alastria_add_public_key(
        web3_mock
    ).encodeABI.assert_called_with(
        fn_name='addKey',
        args=[public_key]
    )
    mock_delegated.assert_called_with('addKeyReturnValue')

    assert asdict(transaction) == expected_transaction


@patch('alastria_identity.services.PublicKeyService.delegated')
@patch('alastria_identity.services.identity_manager.ContractsService.AlastriaPublicKeyRegistry')
def test_revoke_public_key(
    mock_alastria_public_key,
    mock_delegated
):
    web3_mock = Mock()
    public_key = '0x3'

    mock_alastria_public_key(
        web3_mock
    ).encodeABI.return_value = 'revokePublicKeyReturnValue'
    mock_delegated.return_value = 'delegatedReturnValue'

    expected_transaction = {
        'to': Web3.toChecksumAddress(PUBLIC_KEY_REGISTRY_ADDRESS),
        'data': 'delegatedReturnValue',
        'gasPrice': 0,
        'gas': 600000,
        'nonce': '0x0'
    }

    service = PublicKeyService(web3_mock)

    transaction = service.revoke_public_key(public_key)

    mock_alastria_public_key.assert_called_with(web3_mock)
    mock_alastria_public_key(
        web3_mock
    ).encodeABI.assert_called_with(
        fn_name='revokePublicKey',
        args=[public_key]
    )
    mock_delegated.assert_called_with('revokePublicKeyReturnValue')

    assert asdict(transaction) == expected_transaction

@patch('alastria_identity.services.PublicKeyService.delegated')
@patch('alastria_identity.services.identity_manager.ContractsService.AlastriaPublicKeyRegistry')
def test_delete_public_key(
    mock_alastria_public_key,
    mock_delegated
):
    web3_mock = Mock()
    public_key = '0x3'

    mock_alastria_public_key(
        web3_mock
    ).encodeABI.return_value = 'deletePublicKeyReturnValue'
    mock_delegated.return_value = 'delegatedReturnValue'

    expected_transaction = {
        'to': Web3.toChecksumAddress(PUBLIC_KEY_REGISTRY_ADDRESS),
        'data': 'delegatedReturnValue',
        'gasPrice': 0,
        'gas': 600000,
        'nonce': '0x0'
    }

    service = PublicKeyService(web3_mock)

    transaction = service.delete_public_key(public_key)

    mock_alastria_public_key.assert_called_with(web3_mock)
    mock_alastria_public_key(
        web3_mock
    ).encodeABI.assert_called_with(
        fn_name='deletePublicKey',
        args=[public_key]
    )
    mock_delegated.assert_called_with('deletePublicKeyReturnValue')

    assert asdict(transaction) == expected_transaction

@patch('alastria_identity.services.identity_manager.ContractsService.AlastriaPublicKeyRegistry')
def test_get_current_public_key(
    mock_alastria_public_key,
):
    web3_mock = Mock()
    public_key = '0x3'
    issuer_address = 'e53d78c1c6fc694a0f29b3f24bee439338acbe3e'
    issuer_did = f'did:ala:quor:redT:{issuer_address}'

    mock_alastria_public_key(
        web3_mock
    ).encodeABI.return_value = 'getCurrentPublicKeyReturnValue'

    expected_transaction = {
        'to': Web3.toChecksumAddress(PUBLIC_KEY_REGISTRY_ADDRESS),
        'data': 'getCurrentPublicKeyReturnValue',
        'gasPrice': 0,
        'gas': 600000,
        'nonce': '0x0'
    }

    service = PublicKeyService(web3_mock)

    transaction = service.get_current_public_key(issuer_did)

    mock_alastria_public_key.assert_called_with(web3_mock)
    mock_alastria_public_key(
        web3_mock
    ).encodeABI.assert_called_with(
        fn_name='getCurrentPublicKey',
        args=[issuer_address]
    )

    assert asdict(transaction) == expected_transaction

@patch('alastria_identity.services.identity_manager.ContractsService.AlastriaPublicKeyRegistry')
def test_get_public_key_status(
    mock_alastria_public_key,
):
    web3_mock = Mock()
    public_key = '0x3'
    issuer_address = 'e53d78c1c6fc694a0f29b3f24bee439338acbe3e'
    issuer_did = f'did:ala:quor:redT:{issuer_address}'

    mock_alastria_public_key(
        web3_mock
    ).encodeABI.return_value = 'getPublicKeyStatusReturnValue'

    expected_transaction = {
        'to': Web3.toChecksumAddress(PUBLIC_KEY_REGISTRY_ADDRESS),
        'data': 'getPublicKeyStatusReturnValue',
        'gasPrice': 0,
        'gas': 600000,
        'nonce': '0x0'
    }

    service = PublicKeyService(web3_mock)

    transaction = service.get_public_key_status(issuer_did, public_key)

    mock_alastria_public_key.assert_called_with(web3_mock)
    mock_alastria_public_key(
        web3_mock
    ).encodeABI.assert_called_with(
        fn_name='getPublicKeyStatus',
        args=[issuer_address, public_key]
    )

    assert asdict(transaction) == expected_transaction

