from mock import Mock, patch
from dataclasses import asdict
from unittest.mock import patch

from web3 import Web3

from alastria_identity.services import (
    CredentialRegistryService,
    CREDENTIAL_REGISTRY_ADDRESS,
    IDENTITY_MANAGER_ADDRESS)
from alastria_identity.types import Entity


@patch('alastria_identity.services.CredentialRegistryService.delegated')
@patch('alastria_identity.services.identity_manager.ContractsService.AlastriaCredentialRegistry')
def test_add_subject_credential(
        mock_alastria_credential_registry,
        mock_delegated):
    web3_mock = Mock()
    subject_credential_hash = '0x1234'
    uri = '0x9876'
    mock_alastria_credential_registry(
        web3_mock).encodeABI.return_value = 'addSubjectCredentialReturnValue'
    mock_delegated.return_value = 'delegatedReturnValue'
    expected_transaction = {
        'to': Web3.toChecksumAddress(IDENTITY_MANAGER_ADDRESS),
        'data': 'delegatedReturnValue',
        'gasPrice': 0,
        'gas': 600000,
        'nonce': '0x0'
    }
    service = CredentialRegistryService(web3_mock)

    transaction = service.add_subject_credential(subject_credential_hash, uri)

    mock_alastria_credential_registry.assert_called_with(web3_mock)
    mock_alastria_credential_registry(web3_mock).encodeABI.assert_called_with(
        fn_name='addSubjectCredential', args=[subject_credential_hash, uri])
    mock_delegated.assert_called_with('addSubjectCredentialReturnValue')
    assert asdict(transaction) == expected_transaction


@patch('alastria_identity.services.CredentialRegistryService.delegated')
@patch('alastria_identity.services.identity_manager.ContractsService.AlastriaCredentialRegistry')
def test_delete_subject_credential(
        mock_alastria_credential_registry,
        mock_delegated):
    web3_mock = Mock()
    subject_credential_hash = '0x1234'
    mock_alastria_credential_registry(
        web3_mock).encodeABI.return_value = 'deleteSubjectCredentialReturnValue'
    mock_delegated.return_value = 'delegatedReturnValue'
    expected_transaction = {
        'to': Web3.toChecksumAddress(IDENTITY_MANAGER_ADDRESS),
        'data': 'delegatedReturnValue',
        'gasPrice': 0,
        'gas': 600000,
        'nonce': '0x0'
    }
    service = CredentialRegistryService(web3_mock)

    transaction = service.delete_subject_credential(subject_credential_hash)

    mock_alastria_credential_registry.assert_called_with(web3_mock)
    mock_alastria_credential_registry(web3_mock).encodeABI.assert_called_with(
        fn_name='deleteSubjectCredential', args=[subject_credential_hash])
    mock_delegated.assert_called_with('deleteSubjectCredentialReturnValue')
    assert asdict(transaction) == expected_transaction


@patch('alastria_identity.services.identity_manager.ContractsService.AlastriaCredentialRegistry')
def test_get_subject_credential_status(
        mock_alastria_credential_registry):
    web3_mock = Mock()
    subject_credential_hash = '0x1234'
    subject_address = 'e53d78c1c6fc694a0f29b3f24bee439338acbe3e'
    subject_did = f'did:ala:quor:redT:{subject_address}'
    mock_alastria_credential_registry(
        web3_mock).encodeABI.return_value = 'getSubjectCredentialStatusReturnValue'
    expected_transaction = {
        'to': Web3.toChecksumAddress(CREDENTIAL_REGISTRY_ADDRESS),
        'data': 'getSubjectCredentialStatusReturnValue',
        'gasPrice': 0,
        'gas': 600000,
        'nonce': '0x0'
    }
    service = CredentialRegistryService(web3_mock)

    transaction = service.get_subject_credential_status(
        subject_did, subject_credential_hash)

    mock_alastria_credential_registry.assert_called_with(web3_mock)
    mock_alastria_credential_registry(web3_mock).encodeABI.assert_called_with(
        fn_name='getSubjectCredentialStatus', args=[subject_address, subject_credential_hash])
    assert asdict(transaction) == expected_transaction


@patch('alastria_identity.services.identity_manager.ContractsService.AlastriaCredentialRegistry')
def test_get_subject_credential_list(
        mock_alastria_credential_registry):
    web3_mock = Mock()
    subject_address = 'e53d78c1c6fc694a0f29b3f24bee439338acbe3e'
    subject_did = f'did:ala:quor:redT:{subject_address}'
    mock_alastria_credential_registry(
        web3_mock).encodeABI.return_value = 'getSubjectCredentialListReturnValue'
    expected_transaction = {
        'to': Web3.toChecksumAddress(CREDENTIAL_REGISTRY_ADDRESS),
        'data': 'getSubjectCredentialListReturnValue',
        'gasPrice': 0,
        'gas': 600000,
        'nonce': '0x0'
    }
    service = CredentialRegistryService(web3_mock)

    transaction = service.get_subject_credential_list(subject_did)

    mock_alastria_credential_registry.assert_called_with(web3_mock)
    mock_alastria_credential_registry(web3_mock).encodeABI.assert_called_with(
        fn_name='getSubjectCredentialList', args=[subject_address])
    assert asdict(transaction) == expected_transaction


@patch('alastria_identity.services.CredentialRegistryService.delegated')
@patch('alastria_identity.services.identity_manager.ContractsService.AlastriaCredentialRegistry')
def test_add_issuer_credential(
        mock_alastria_credential_registry,
        mock_delegated):
    web3_mock = Mock()
    issuer_credential_hash = '0x1234'
    mock_alastria_credential_registry(
        web3_mock).encodeABI.return_value = 'addIssuerCredentialReturnValue'
    mock_delegated.return_value = 'delegatedReturnValue'
    expected_transaction = {
        'to': Web3.toChecksumAddress(IDENTITY_MANAGER_ADDRESS),
        'data': 'delegatedReturnValue',
        'gasPrice': 0,
        'gas': 600000,
        'nonce': '0x0'
    }
    service = CredentialRegistryService(web3_mock)

    transaction = service.add_issuer_credential(issuer_credential_hash)

    mock_alastria_credential_registry.assert_called_with(web3_mock)
    mock_alastria_credential_registry(web3_mock).encodeABI.assert_called_with(
        fn_name='addIssuerCredential', args=[issuer_credential_hash])
    mock_delegated.assert_called_with('addIssuerCredentialReturnValue')
    assert asdict(transaction) == expected_transaction


@patch('alastria_identity.services.identity_manager.ContractsService.AlastriaCredentialRegistry')
def test_get_issuer_credential_status(
        mock_alastria_credential_registry):
    web3_mock = Mock()
    issuer_address = 'e53d78c1c6fc694a0f29b3f24bee439338acbe3e'
    issuer_did = f'did:ala:quor:redT:{issuer_address}'
    issuer_credential_hash = '0x1234'
    mock_alastria_credential_registry(
        web3_mock).encodeABI.return_value = 'getIssuerCredentialStatusReturnValue'
    expected_transaction = {
        'to': Web3.toChecksumAddress(CREDENTIAL_REGISTRY_ADDRESS),
        'data': 'getIssuerCredentialStatusReturnValue',
        'gasPrice': 0,
        'gas': 600000,
        'nonce': '0x0'
    }
    service = CredentialRegistryService(web3_mock)

    transaction = service.get_issuer_credential_status(
        issuer_did, issuer_credential_hash)

    mock_alastria_credential_registry.assert_called_with(web3_mock)
    mock_alastria_credential_registry(web3_mock).encodeABI.assert_called_with(
        fn_name='getIssuerCredentialStatus', args=[issuer_address, issuer_credential_hash])
    assert asdict(transaction) == expected_transaction


@patch('alastria_identity.services.CredentialRegistryService.delegated')
@patch('alastria_identity.services.identity_manager.ContractsService.AlastriaCredentialRegistry')
def test_update_credential_status(
        mock_alastria_credential_registry,
        mock_delegated):
    web3_mock = Mock()
    status = 2
    issuer_credential_hash = '0x1234'
    mock_alastria_credential_registry(
        web3_mock).encodeABI.return_value = 'updateCredentialStatusReturnValue'
    mock_delegated.return_value = 'delegatedReturnValue'
    expected_transaction = {
        'to': Web3.toChecksumAddress(IDENTITY_MANAGER_ADDRESS),
        'data': 'delegatedReturnValue',
        'gasPrice': 0,
        'gas': 600000,
        'nonce': '0x0'
    }
    service = CredentialRegistryService(web3_mock)

    transaction = service.update_credential_status(
        issuer_credential_hash, status)

    mock_alastria_credential_registry.assert_called_with(web3_mock)
    mock_alastria_credential_registry(web3_mock).encodeABI.assert_called_with(
        fn_name='updateCredentialStatus', args=[issuer_credential_hash, status])
    mock_delegated.assert_called_with('updateCredentialStatusReturnValue')
    assert asdict(transaction) == expected_transaction


@patch('alastria_identity.services.identity_manager.ContractsService.AlastriaCredentialRegistry')
def test_get_credential_status(
        mock_alastria_credential_registry):
    web3_mock = Mock()
    subject_status = 2
    issuer_status = 2
    mock_alastria_credential_registry(
        web3_mock).encodeABI.return_value = 'getCredentialStatusReturnValue'
    expected_transaction = {
        'to': Web3.toChecksumAddress(CREDENTIAL_REGISTRY_ADDRESS),
        'data': 'getCredentialStatusReturnValue',
        'gasPrice': 0,
        'gas': 600000,
        'nonce': '0x0'
    }
    service = CredentialRegistryService(web3_mock)

    transaction = service.get_credential_status(subject_status, issuer_status)

    mock_alastria_credential_registry.assert_called_with(web3_mock)
    mock_alastria_credential_registry(web3_mock).encodeABI.assert_called_with(
        fn_name='getCredentialStatus', args=[subject_status, issuer_status])
    assert asdict(transaction) == expected_transaction


@patch('alastria_identity.services.identity_manager.ContractsService.AlastriaIdentityManager')
def test_delegated_call(
        mock_alastria_identity_manager):
    web3_mock = Mock()
    data = 'exampleData'
    mock_alastria_identity_manager(
        web3_mock).encodeABI.return_value = 'delegatedValue'
    service = CredentialRegistryService(web3_mock)

    transaction = service.delegated(data)

    mock_alastria_identity_manager.assert_called_with(web3_mock)
    mock_alastria_identity_manager(web3_mock).encodeABI.assert_called_with(
        fn_name='delegateCall',
        args=[Web3.toChecksumAddress(CREDENTIAL_REGISTRY_ADDRESS), 0, data])
    assert transaction == 'delegatedValue'
