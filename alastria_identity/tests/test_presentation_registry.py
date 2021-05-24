from mock import Mock, patch
from dataclasses import asdict
from unittest.mock import patch
from web3 import Web3

from alastria_identity.services import (
    PresentationRegistryService,
    PRESENTATION_REGISTRY_ADDRESS,
    IDENTITY_MANAGER_ADDRESS)


@patch('alastria_identity.services.PresentationRegistryService.delegated')
@patch('alastria_identity.services.identity_manager.ContractsService.AlastriaPresentationRegistry')
def test_add_subject_presentation(
    mock_alastria_presentation_registry,
    mock_delegated
):

    web3_mock = Mock()
    subject_presentation_hash = '0x1234'
    uri = '0x9876'

    mock_alastria_presentation_registry(
        web3_mock
    ).encodeABI.return_value = 'addSubjectPresentationReturnValue'
    mock_delegated.return_value = 'delegatedReturnValue'

    expected_transaction = {
        'to': Web3.toChecksumAddress(IDENTITY_MANAGER_ADDRESS),
        'data': 'delegatedReturnValue',
        'gasPrice': 0,
        'gas': 600000,
        'nonce': '0x0'
    }

    service = PresentationRegistryService(web3_mock)

    transaction = service.add_subject_presentation(subject_presentation_hash, uri)

    mock_alastria_presentation_registry.assert_called_with(web3_mock)
    mock_alastria_presentation_registry(
        web3_mock
    ).encodeABI.assert_called_with(
        fn_name='addSubjectPresentation',
        args=[subject_presentation_hash, uri]
    )
    mock_delegated.assert_called_with('addSubjectPresentationReturnValue')

    assert asdict(transaction) == expected_transaction


@patch('alastria_identity.services.PresentationRegistryService.delegated')
@patch('alastria_identity.services.identity_manager.ContractsService.AlastriaPresentationRegistry')
def test_update_subject_presentation(
    mock_alastria_presentation_registry,
    mock_delegated
):

    web3_mock = Mock()
    subject_presentation_hash = '0x1234'
    status = 1

    mock_alastria_presentation_registry(
        web3_mock
    ).encodeABI.return_value = 'updateSubjectPresentationReturnValue'
    mock_delegated.return_value = 'delegatedReturnValue'

    expected_transaction = {
        'to': Web3.toChecksumAddress(IDENTITY_MANAGER_ADDRESS),
        'data': 'delegatedReturnValue',
        'gasPrice': 0,
        'gas': 600000,
        'nonce': '0x0'
    }

    service = PresentationRegistryService(web3_mock)

    transaction = service.update_subject_presentation(
        subject_presentation_hash, status
    )

    mock_alastria_presentation_registry.assert_called_with(web3_mock)
    mock_alastria_presentation_registry(
        web3_mock
    ).encodeABI.assert_called_with(
        fn_name='updateSubjectPresentation',
        args=[subject_presentation_hash, status]
    )
    mock_delegated.assert_called_with('updateSubjectPresentationReturnValue')

    assert asdict(transaction) == expected_transaction


@patch('alastria_identity.services.identity_manager.ContractsService.AlastriaPresentationRegistry')
def test_get_subject_presentation_status(
    mock_alastria_presentation_registry
):

    web3_mock = Mock()
    subject_presentation_hash = '0x1234'
    subject_address = 'e53d78c1c6fc694a0f29b3f24bee439338acbe3e'
    subject_did = f'did:ala:quor:redT:{subject_address}'

    mock_alastria_presentation_registry(
        web3_mock
    ).encodeABI.return_value = 'getSubjectPresentationStatusReturnValue'

    expected_transaction = {
        'to': Web3.toChecksumAddress(PRESENTATION_REGISTRY_ADDRESS),
        'data': 'getSubjectPresentationStatusReturnValue',
        'gasPrice': 0,
        'gas': 600000,
        'nonce': '0x0'
    }

    service = PresentationRegistryService(web3_mock)

    transaction = service.get_subject_presentation_status(
        subject_did, subject_presentation_hash
    )

    mock_alastria_presentation_registry.assert_called_with(web3_mock)
    mock_alastria_presentation_registry(
        web3_mock
    ).encodeABI.assert_called_with(
        fn_name='getSubjectPresentationStatus',
        args=[subject_address, subject_presentation_hash]
    )

    assert asdict(transaction) == expected_transaction


@patch('alastria_identity.services.identity_manager.ContractsService.AlastriaPresentationRegistry')
def test_get_subject_presentation_list(
    mock_alastria_presentation_registry
):

    web3_mock = Mock()
    subject_address = 'e53d78c1c6fc694a0f29b3f24bee439338acbe3e'
    subject_did = f'did:ala:quor:redT:{subject_address}'

    mock_alastria_presentation_registry(
        web3_mock
    ).encodeABI.return_value = 'getSubjectPresentationListReturnValue'

    expected_transaction = {
        'to': Web3.toChecksumAddress(PRESENTATION_REGISTRY_ADDRESS),
        'data': 'getSubjectPresentationListReturnValue',
        'gasPrice': 0,
        'gas': 600000,
        'nonce': '0x0'
    }

    service = PresentationRegistryService(web3_mock)

    transaction = service.get_subject_presentation_list(subject_did)

    mock_alastria_presentation_registry.assert_called_with(web3_mock)
    mock_alastria_presentation_registry(
        web3_mock
    ).encodeABI.assert_called_with(
        fn_name='getSubjectPresentationList',
        args=[subject_address]
    )

    assert asdict(transaction) == expected_transaction


@patch('alastria_identity.services.PresentationRegistryService.delegated')
@patch('alastria_identity.services.identity_manager.ContractsService.AlastriaPresentationRegistry')
def test_update_receiver_presentation(
    mock_alastria_presentation_registry,
    mock_delegated
):

    web3_mock = Mock()
    receiver_presentation_hash = '0x1234'
    status = 1
    mock_alastria_presentation_registry(
        web3_mock
    ).encodeABI.return_value = 'updateReceiverPresentationReturnValue'
    mock_delegated.return_value = 'delegatedReturnValue'

    expected_transaction = {
        'to': Web3.toChecksumAddress(IDENTITY_MANAGER_ADDRESS),
        'data': 'delegatedReturnValue',
        'gasPrice': 0,
        'gas': 600000,
        'nonce': '0x0'
    }

    service = PresentationRegistryService(web3_mock)

    transaction = service.update_receiver_presentation(receiver_presentation_hash, status)

    mock_alastria_presentation_registry.assert_called_with(web3_mock)
    mock_alastria_presentation_registry(
        web3_mock
    ).encodeABI.assert_called_with(
        fn_name='updateReceiverPresentation',
        args=[receiver_presentation_hash, status]
    )
    mock_delegated.assert_called_with('updateReceiverPresentationReturnValue')

    assert asdict(transaction) == expected_transaction


@patch('alastria_identity.services.identity_manager.ContractsService.AlastriaPresentationRegistry')
def test_get_receiver_presentation_status(
    mock_alastria_presentation_registry
):

    web3_mock = Mock()
    receiver_address = 'e53d78c1c6fc694a0f29b3f24bee439338acbe3e'
    receiver_did = f'did:ala:quor:redT:{receiver_address}'
    receiver_presentation_hash = '0x1234'

    mock_alastria_presentation_registry(
        web3_mock
    ).encodeABI.return_value = 'getReceiverPresentationStatusReturnValue'

    expected_transaction = {
        'to': Web3.toChecksumAddress(PRESENTATION_REGISTRY_ADDRESS),
        'data': 'getReceiverPresentationStatusReturnValue',
        'gasPrice': 0,
        'gas': 600000,
        'nonce': '0x0'
    }

    service = PresentationRegistryService(web3_mock)

    transaction = service.get_receiver_presentation_status(
        receiver_did, receiver_presentation_hash
    )

    mock_alastria_presentation_registry.assert_called_with(web3_mock)
    mock_alastria_presentation_registry(
        web3_mock
    ).encodeABI.assert_called_with(
        fn_name='getReceiverPresentationStatus',
        args=[receiver_address, receiver_presentation_hash]
    )

    assert asdict(transaction) == expected_transaction


@patch('alastria_identity.services.identity_manager.ContractsService.AlastriaPresentationRegistry')
def test_get_presentation_status(
    mock_alastria_presentation_registry
):

    web3_mock = Mock()
    subject_status = 2
    receiver_status = 2

    mock_alastria_presentation_registry(
        web3_mock
    ).encodeABI.return_value = 'getPresentationStatusReturnValue'

    expected_transaction = {
        'to': Web3.toChecksumAddress(PRESENTATION_REGISTRY_ADDRESS),
        'data': 'getPresentationStatusReturnValue',
        'gasPrice': 0,
        'gas': 600000,
        'nonce': '0x0'
    }
    service = PresentationRegistryService(web3_mock)

    transaction = service.get_presentation_status(subject_status, receiver_status)

    mock_alastria_presentation_registry.assert_called_with(web3_mock)
    mock_alastria_presentation_registry(
        web3_mock
    ).encodeABI.assert_called_with(
        fn_name='getPresentationStatus',
        args=[subject_status, receiver_status]
    )

    assert asdict(transaction) == expected_transaction


@patch('alastria_identity.services.identity_manager.ContractsService.AlastriaIdentityManager')
def test_delegated_call(
    mock_alastria_identity_manager
):

    web3_mock = Mock()
    data = 'exampleData'

    mock_alastria_identity_manager(
        web3_mock
    ).encodeABI.return_value = 'delegatedValue'
    service = PresentationRegistryService(web3_mock)

    transaction = service.delegated(data)

    mock_alastria_identity_manager.assert_called_with(web3_mock)
    mock_alastria_identity_manager(web3_mock).encodeABI.assert_called_with(
        fn_name='delegateCall',
        args=[Web3.toChecksumAddress(PRESENTATION_REGISTRY_ADDRESS), 0, data]
    )

    assert transaction == 'delegatedValue'
