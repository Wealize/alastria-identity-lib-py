from mock import *
from dataclasses import asdict
from unittest.mock import patch
from web3 import Web3

from alastria_identity.services import IdentityManagerService, IDENTITY_MANAGER_ADDRESS
from alastria_identity.types import Entity


@patch('alastria_identity.services.IdentityManagerService.delegated')
@patch('alastria_identity.services.identity_manager.ContractsService.AlastriaIdentityManager')
def test_prepare_alastria_id(
        mock_alastria_identity_manager,
        mock_delegated):
    web3_mock = Mock()
    sign_addres = '0x1234'
    mock_alastria_identity_manager(
        web3_mock).encodeABI.return_value = 'prepareAlastriaIDReturnValue'
    mock_delegated.return_value = 'delegatedReturnValue'
    expected_transaction = {
        'to': Web3.toChecksumAddress(IDENTITY_MANAGER_ADDRESS),
        'data': 'delegatedReturnValue',
        'gasPrice': 0,
        'gas': 600000,
        'nonce': '0x0'
    }
    service = IdentityManagerService(web3_mock)

    transaction = service.prepare_alastria_id(sign_addres)

    mock_alastria_identity_manager.assert_called_with(web3_mock)
    mock_alastria_identity_manager(web3_mock).encodeABI.assert_called_with(
        fn_name='prepareAlastriaID', args=[sign_addres])
    mock_delegated.assert_called_with('prepareAlastriaIDReturnValue')
    assert asdict(transaction) == expected_transaction


@patch('alastria_identity.services.identity_manager.ContractsService.AlastriaIdentityManager')
@patch('alastria_identity.services.identity_manager.ContractsService.AlastriaPublicKeyRegistry')
def test_create_alastria_identity(
        mock_public_key_registry,
        mock_identity_manager):
    web3_mock = Mock()
    public_key = '0x1234'
    mock_public_key_registry(web3_mock).encodeABI.return_value = 'addKeyValue'
    mock_identity_manager(
        web3_mock).encodeABI.return_value = 'createAlastriaIdentityValue'
    expected_transaction = {
        'to': Web3.toChecksumAddress(IDENTITY_MANAGER_ADDRESS),
        'data': 'createAlastriaIdentityValue',
        'gasPrice': 0,
        'gas': 600000,
        'nonce': '0x0'
    }
    service = IdentityManagerService(web3_mock)

    transaction = service.create_alastria_identity(public_key)

    mock_public_key_registry.assert_called_with(web3_mock)
    mock_public_key_registry(web3_mock).encodeABI.assert_called_with(
        fn_name='addKey', args=[public_key])
    mock_identity_manager.assert_called_with(web3_mock)
    mock_identity_manager(web3_mock).encodeABI.assert_called_with(
        fn_name='createAlastriaIdentity', args=['addKeyValue'])
    assert asdict(transaction) == expected_transaction


@patch('alastria_identity.services.IdentityManagerService.delegated')
@patch('alastria_identity.services.identity_manager.ContractsService.AlastriaIdentityManager')
def test_add_identity_issuer(
        mock_alastria_identity_manager,
        mock_delegated):
    web3_mock = Mock()
    issuer_address = 'e53d78c1c6fc694a0f29b3f24bee439338acbe3e'
    did_issuer = f'did:ala:quor:redT:{issuer_address}'
    level = '1'
    mock_alastria_identity_manager(
        web3_mock).encodeABI.return_value = 'addIdentityIssuerValue'
    mock_delegated.return_value = 'delegatedReturnValue'
    expected_transaction = {
        'to': Web3.toChecksumAddress(IDENTITY_MANAGER_ADDRESS),
        'data': 'delegatedReturnValue',
        'gasPrice': 0,
        'gas': 600000,
        'nonce': '0x0'
    }
    service = IdentityManagerService(web3_mock)

    transaction = service.add_idendity_issuer(did_issuer, level)

    mock_alastria_identity_manager.assert_called_with(web3_mock)
    mock_alastria_identity_manager(web3_mock).encodeABI.assert_called_with(
        fn_name='addIdentityIssuer', args=[issuer_address, level])
    mock_delegated.assert_called_with('addIdentityIssuerValue')
    assert asdict(transaction) == expected_transaction


@patch('alastria_identity.services.IdentityManagerService.delegated')
@patch('alastria_identity.services.identity_manager.ContractsService.AlastriaIdentityManager')
def test_update_identity_issuer_eidas_level(
        mock_alastria_identity_manager,
        mock_delegated):
    web3_mock = Mock()
    issuer_address = 'e53d78c1c6fc694a0f29b3f24bee439338acbe3e'
    did_issuer = f'did:ala:quor:redT:{issuer_address}'
    level = '3'
    mock_alastria_identity_manager(
        web3_mock).encodeABI.return_value = 'updateIdentityIssuerEidasLevelValue'
    mock_delegated.return_value = 'delegatedReturnValue'
    expected_transaction = {
        'to': Web3.toChecksumAddress(IDENTITY_MANAGER_ADDRESS),
        'data': 'delegatedReturnValue',
        'gasPrice': 0,
        'gas': 600000,
        'nonce': '0x0'
    }
    service = IdentityManagerService(web3_mock)

    transaction = service.update_identity_issuer_eidas_level(did_issuer, level)

    mock_alastria_identity_manager.assert_called_with(web3_mock)
    mock_alastria_identity_manager(web3_mock).encodeABI.assert_called_with(
        fn_name='updateIdentityIssuerEidasLevel', args=[issuer_address, level])
    mock_delegated.assert_called_with('updateIdentityIssuerEidasLevelValue')
    assert asdict(transaction) == expected_transaction


@patch('alastria_identity.services.IdentityManagerService.delegated')
@patch('alastria_identity.services.identity_manager.ContractsService.AlastriaIdentityManager')
def test_delete_identity_issuer(
        mock_alastria_identity_manager,
        mock_delegated):
    web3_mock = Mock()
    issuer_address = 'e53d78c1c6fc694a0f29b3f24bee439338acbe3e'
    did_issuer = f'did:ala:quor:redT:{issuer_address}'
    mock_alastria_identity_manager(
        web3_mock).encodeABI.return_value = 'deleteIdentityIssuerEidasLevelValue'
    mock_delegated.return_value = 'delegatedReturnValue'
    expected_transaction = {
        'to': Web3.toChecksumAddress(IDENTITY_MANAGER_ADDRESS),
        'data': 'delegatedReturnValue',
        'gasPrice': 0,
        'gas': 600000,
        'nonce': '0x0'
    }
    service = IdentityManagerService(web3_mock)

    transaction = service.delete_identity_issuer(did_issuer)

    mock_alastria_identity_manager.assert_called_with(web3_mock)
    mock_alastria_identity_manager(web3_mock).encodeABI.assert_called_with(
        fn_name='deleteIdentityIssuer', args=[issuer_address])
    mock_delegated.assert_called_with('deleteIdentityIssuerEidasLevelValue')
    assert asdict(transaction) == expected_transaction


@patch('alastria_identity.services.identity_manager.ContractsService.AlastriaIdentityManager')
def test_get_eidas_level(
        mock_alastria_identity_manager):
    web3_mock = Mock()
    issuer_address = 'e53d78c1c6fc694a0f29b3f24bee439338acbe3e'
    did_issuer = f'did:ala:quor:redT:{issuer_address}'
    mock_alastria_identity_manager(
        web3_mock).encodeABI.return_value = 'getEidasLevelValue'
    expected_transaction = {
        'to': Web3.toChecksumAddress(IDENTITY_MANAGER_ADDRESS),
        'data': 'getEidasLevelValue',
        'gasPrice': 0,
        'gas': 600000,
        'nonce': '0x0'
    }
    service = IdentityManagerService(web3_mock)

    transaction = service.get_eidas_level(did_issuer)

    mock_alastria_identity_manager.assert_called_with(web3_mock)
    mock_alastria_identity_manager(web3_mock).encodeABI.assert_called_with(
        fn_name='getEidasLevel', args=[issuer_address])
    assert asdict(transaction) == expected_transaction


@patch('alastria_identity.services.IdentityManagerService.delegated')
@patch('alastria_identity.services.identity_manager.ContractsService.AlastriaIdentityManager')
def test_add_identity_service_provider(
        mock_alastria_identity_manager,
        mock_delegated):
    web3_mock = Mock()
    provider_address = 'e53d78c1c6fc694a0f29b3f24bee439338acbe3e'
    did_service_provider = f'did:ala:quor:redT:{provider_address}'
    mock_alastria_identity_manager(
        web3_mock).encodeABI.return_value = 'addIdentityServiceProviderValue'
    mock_delegated.return_value = 'delegatedReturnValue'
    expected_transaction = {
        'to': Web3.toChecksumAddress(IDENTITY_MANAGER_ADDRESS),
        'data': 'delegatedReturnValue',
        'gasPrice': 0,
        'gas': 600000,
        'nonce': '0x0'
    }
    service = IdentityManagerService(web3_mock)

    transaction = service.add_identity_service_provider(did_service_provider)

    mock_alastria_identity_manager.assert_called_with(web3_mock)
    mock_alastria_identity_manager(web3_mock).encodeABI.assert_called_with(
        fn_name='addIdentityServiceProvider', args=[provider_address])
    mock_delegated.assert_called_with('addIdentityServiceProviderValue')
    assert asdict(transaction) == expected_transaction


@patch('alastria_identity.services.IdentityManagerService.delegated')
@patch('alastria_identity.services.identity_manager.ContractsService.AlastriaIdentityManager')
def test_delete_identity_service_provider(
        mock_alastria_identity_manager,
        mock_delegated):
    web3_mock = Mock()
    provider_address = 'e53d78c1c6fc694a0f29b3f24bee439338acbe3e'
    did_service_provider = f'did:ala:quor:redT:{provider_address}'
    mock_alastria_identity_manager(
        web3_mock).encodeABI.return_value = 'deleteIdentityServiceProviderValue'
    mock_delegated.return_value = 'delegatedReturnValue'
    expected_transaction = {
        'to': Web3.toChecksumAddress(IDENTITY_MANAGER_ADDRESS),
        'data': 'delegatedReturnValue',
        'gasPrice': 0,
        'gas': 600000,
        'nonce': '0x0'
    }
    service = IdentityManagerService(web3_mock)

    transaction = service.delete_identity_service_provider(
        did_service_provider)

    mock_alastria_identity_manager.assert_called_with(web3_mock)
    mock_alastria_identity_manager(web3_mock).encodeABI.assert_called_with(
        fn_name='deleteIdentityServiceProvider', args=[provider_address])
    mock_delegated.assert_called_with('deleteIdentityServiceProviderValue')
    assert asdict(transaction) == expected_transaction


@patch('alastria_identity.services.identity_manager.ContractsService.AlastriaIdentityManager')
def test_is_identity_service_provider(
        mock_alastria_identity_manager):
    web3_mock = Mock()
    provider_address = 'e53d78c1c6fc694a0f29b3f24bee439338acbe3e'
    did_service_provider = f'did:ala:quor:redT:{provider_address}'
    mock_alastria_identity_manager(
        web3_mock).encodeABI.return_value = 'isIdentityServiceProviderValue'
    expected_transaction = {
        'to': Web3.toChecksumAddress(IDENTITY_MANAGER_ADDRESS),
        'data': 'isIdentityServiceProviderValue',
        'gasPrice': 0,
        'gas': 600000,
        'nonce': '0x0'
    }
    service = IdentityManagerService(web3_mock)

    transaction = service.is_identity_service_provider(did_service_provider)

    mock_alastria_identity_manager.assert_called_with(web3_mock)
    mock_alastria_identity_manager(web3_mock).encodeABI.assert_called_with(
        fn_name='isIdentityServiceProvider', args=[provider_address])
    assert asdict(transaction) == expected_transaction


@patch('alastria_identity.services.identity_manager.ContractsService.AlastriaIdentityManager')
def test_is_identity_issuer(
        mock_alastria_identity_manager):
    web3_mock = Mock()
    issuer_address = 'e53d78c1c6fc694a0f29b3f24bee439338acbe3e'
    did_issuer = f'did:ala:quor:redT:{issuer_address}'
    mock_alastria_identity_manager(
        web3_mock).encodeABI.return_value = 'isIdentityIssuerValue'
    expected_transaction = {
        'to': Web3.toChecksumAddress(IDENTITY_MANAGER_ADDRESS),
        'data': 'isIdentityIssuerValue',
        'gasPrice': 0,
        'gas': 600000,
        'nonce': '0x0'
    }
    service = IdentityManagerService(web3_mock)

    transaction = service.is_identity_issuer(did_issuer)

    mock_alastria_identity_manager.assert_called_with(web3_mock)
    mock_alastria_identity_manager(web3_mock).encodeABI.assert_called_with(
        fn_name='isIdentityIssuer', args=[issuer_address])
    assert asdict(transaction) == expected_transaction


@patch('alastria_identity.services.IdentityManagerService.delegated')
@patch('alastria_identity.services.identity_manager.ContractsService.AlastriaIdentityManager')
def test_add_entity(
        mock_alastria_identity_manager,
        mock_delegated):
    web3_mock = Mock()
    entity_address = 'e53d78c1c6fc694a0f29b3f24bee439338acbe3e'
    did_entity = f'did:ala:quor:redT:{entity_address}'
    entity = Entity(
        did_entity,
        'EntityName',
        'EntityCIF',
        'EntityUrlLogo',
        'EntityCreateAID',
        'EntityAOA',
        0)
    mock_alastria_identity_manager(
        web3_mock).encodeABI.return_value = 'addEntityValue'
    mock_delegated.return_value = 'delegatedReturnValue'
    expected_transaction = {
        'to': Web3.toChecksumAddress(IDENTITY_MANAGER_ADDRESS),
        'data': 'delegatedReturnValue',
        'gasPrice': 0,
        'gas': 600000,
        'nonce': '0x0'
    }
    service = IdentityManagerService(web3_mock)

    transaction = service.add_entity(entity)

    mock_alastria_identity_manager.assert_called_with(web3_mock)
    mock_alastria_identity_manager(web3_mock).encodeABI.assert_called_with(
        fn_name='addEntity',
        args=[
            entity_address,
            entity.name,
            entity.cif,
            entity.url_logo,
            entity.url_create_aid,
            entity.url_aoa,
            entity.status
        ])
    mock_delegated.assert_called_with('addEntityValue')
    assert asdict(transaction) == expected_transaction


@patch('alastria_identity.services.IdentityManagerService.delegated')
@patch('alastria_identity.services.identity_manager.ContractsService.AlastriaIdentityManager')
def test_set_entity_name(
        mock_alastria_identity_manager,
        mock_delegated):
    web3_mock = Mock()
    entity_address = 'e53d78c1c6fc694a0f29b3f24bee439338acbe3e'
    did_entity = f'did:ala:quor:redT:{entity_address}'
    entity = Entity(
        did_entity,
        'EntityName',
        'EntityCIF',
        'EntityUrlLogo',
        'EntityCreateAID',
        'EntityAOA',
        0)
    mock_alastria_identity_manager(
        web3_mock).encodeABI.return_value = 'setEntityNameValue'
    mock_delegated.return_value = 'delegatedReturnValue'
    expected_transaction = {
        'to': Web3.toChecksumAddress(IDENTITY_MANAGER_ADDRESS),
        'data': 'delegatedReturnValue',
        'gasPrice': 0,
        'gas': 600000,
        'nonce': '0x0'
    }
    service = IdentityManagerService(web3_mock)

    transaction = service.set_entity_name(entity)

    mock_alastria_identity_manager.assert_called_with(web3_mock)
    mock_alastria_identity_manager(web3_mock).encodeABI.assert_called_with(
        fn_name='setNameEntity',
        args=[entity.name])
    mock_delegated.assert_called_with('setEntityNameValue')
    assert asdict(transaction) == expected_transaction


@patch('alastria_identity.services.IdentityManagerService.delegated')
@patch('alastria_identity.services.identity_manager.ContractsService.AlastriaIdentityManager')
def test_set_entity_cif(
        mock_alastria_identity_manager,
        mock_delegated):
    web3_mock = Mock()
    entity_address = 'e53d78c1c6fc694a0f29b3f24bee439338acbe3e'
    did_entity = f'did:ala:quor:redT:{entity_address}'
    entity = Entity(
        did_entity,
        'EntityName',
        'EntityCIF',
        'EntityUrlLogo',
        'EntityCreateAID',
        'EntityAOA',
        0)
    mock_alastria_identity_manager(
        web3_mock).encodeABI.return_value = 'setEntityCifValue'
    mock_delegated.return_value = 'delegatedReturnValue'
    expected_transaction = {
        'to': Web3.toChecksumAddress(IDENTITY_MANAGER_ADDRESS),
        'data': 'delegatedReturnValue',
        'gasPrice': 0,
        'gas': 600000,
        'nonce': '0x0'
    }
    service = IdentityManagerService(web3_mock)

    transaction = service.set_entity_cif(entity)

    mock_alastria_identity_manager.assert_called_with(web3_mock)
    mock_alastria_identity_manager(web3_mock).encodeABI.assert_called_with(
        fn_name='setCifEntity',
        args=[entity.cif])
    mock_delegated.assert_called_with('setEntityCifValue')
    assert asdict(transaction) == expected_transaction


@patch('alastria_identity.services.IdentityManagerService.delegated')
@patch('alastria_identity.services.identity_manager.ContractsService.AlastriaIdentityManager')
def test_set_entity_url_logo(
        mock_alastria_identity_manager,
        mock_delegated):
    web3_mock = Mock()
    entity_address = 'e53d78c1c6fc694a0f29b3f24bee439338acbe3e'
    did_entity = f'did:ala:quor:redT:{entity_address}'
    entity = Entity(
        did_entity,
        'EntityName',
        'EntityCIF',
        'EntityUrlLogo',
        'EntityCreateAID',
        'EntityAOA',
        0)
    mock_alastria_identity_manager(
        web3_mock).encodeABI.return_value = 'setEntityUrlLogoValue'
    mock_delegated.return_value = 'delegatedReturnValue'
    expected_transaction = {
        'to': Web3.toChecksumAddress(IDENTITY_MANAGER_ADDRESS),
        'data': 'delegatedReturnValue',
        'gasPrice': 0,
        'gas': 600000,
        'nonce': '0x0'
    }
    service = IdentityManagerService(web3_mock)

    transaction = service.set_entity_url_logo(entity)

    mock_alastria_identity_manager.assert_called_with(web3_mock)
    mock_alastria_identity_manager(web3_mock).encodeABI.assert_called_with(
        fn_name='setUrlLogo',
        args=[entity.url_logo])
    mock_delegated.assert_called_with('setEntityUrlLogoValue')
    assert asdict(transaction) == expected_transaction


@patch('alastria_identity.services.IdentityManagerService.delegated')
@patch('alastria_identity.services.identity_manager.ContractsService.AlastriaIdentityManager')
def test_set_entity_url_create_aid(
        mock_alastria_identity_manager,
        mock_delegated):
    web3_mock = Mock()
    entity_address = 'e53d78c1c6fc694a0f29b3f24bee439338acbe3e'
    did_entity = f'did:ala:quor:redT:{entity_address}'
    entity = Entity(
        did_entity,
        'EntityName',
        'EntityCIF',
        'EntityUrlLogo',
        'EntityCreateAID',
        'EntityAOA',
        0)
    mock_alastria_identity_manager(
        web3_mock).encodeABI.return_value = 'setEntityUrlCreateAIDValue'
    mock_delegated.return_value = 'delegatedReturnValue'
    expected_transaction = {
        'to': Web3.toChecksumAddress(IDENTITY_MANAGER_ADDRESS),
        'data': 'delegatedReturnValue',
        'gasPrice': 0,
        'gas': 600000,
        'nonce': '0x0'
    }
    service = IdentityManagerService(web3_mock)

    transaction = service.set_entity_url_create_aid(entity)

    mock_alastria_identity_manager.assert_called_with(web3_mock)
    mock_alastria_identity_manager(web3_mock).encodeABI.assert_called_with(
        fn_name='setUrlCreateAID',
        args=[entity.url_create_aid])
    mock_delegated.assert_called_with('setEntityUrlCreateAIDValue')
    assert asdict(transaction) == expected_transaction


@patch('alastria_identity.services.IdentityManagerService.delegated')
@patch('alastria_identity.services.identity_manager.ContractsService.AlastriaIdentityManager')
def test_set_entity_url_aoa(
        mock_alastria_identity_manager,
        mock_delegated):
    web3_mock = Mock()
    entity_address = 'e53d78c1c6fc694a0f29b3f24bee439338acbe3e'
    did_entity = f'did:ala:quor:redT:{entity_address}'
    entity = Entity(
        did_entity,
        'EntityName',
        'EntityCIF',
        'EntityUrlLogo',
        'EntityCreateAID',
        'EntityAOA',
        0)
    mock_alastria_identity_manager(
        web3_mock).encodeABI.return_value = 'setEntityUrlAoaAIDValue'
    mock_delegated.return_value = 'delegatedReturnValue'
    expected_transaction = {
        'to': Web3.toChecksumAddress(IDENTITY_MANAGER_ADDRESS),
        'data': 'delegatedReturnValue',
        'gasPrice': 0,
        'gas': 600000,
        'nonce': '0x0'
    }
    service = IdentityManagerService(web3_mock)

    transaction = service.set_entity_url_aoa_aid(entity)

    mock_alastria_identity_manager.assert_called_with(web3_mock)
    mock_alastria_identity_manager(web3_mock).encodeABI.assert_called_with(
        fn_name='setUrlAOA',
        args=[entity.url_aoa])
    mock_delegated.assert_called_with('setEntityUrlAoaAIDValue')
    assert asdict(transaction) == expected_transaction


@patch('alastria_identity.services.identity_manager.ContractsService.AlastriaIdentityManager')
def test_get_entity(
        mock_alastria_identity_manager):
    web3_mock = Mock()
    entity_address = 'e53d78c1c6fc694a0f29b3f24bee439338acbe3e'
    did_entity = f'did:ala:quor:redT:{entity_address}'
    entity = Entity(
        did_entity,
        'EntityName',
        'EntityCIF',
        'EntityUrlLogo',
        'EntityCreateAID',
        'EntityAOA',
        0)
    mock_alastria_identity_manager(
        web3_mock).encodeABI.return_value = 'getEntityValue'
    expected_transaction = {
        'to': Web3.toChecksumAddress(IDENTITY_MANAGER_ADDRESS),
        'data': 'getEntityValue',
        'gasPrice': 0,
        'gas': 600000,
        'nonce': '0x0'
    }
    service = IdentityManagerService(web3_mock)

    transaction = service.get_entity(entity)

    mock_alastria_identity_manager.assert_called_with(web3_mock)
    mock_alastria_identity_manager(web3_mock).encodeABI.assert_called_with(
        fn_name='getEntity',
        args=[entity_address])
    assert asdict(transaction) == expected_transaction


@patch('alastria_identity.services.identity_manager.ContractsService.AlastriaIdentityManager')
def test_get_entities_list(
        mock_alastria_identity_manager):
    web3_mock = Mock()
    mock_alastria_identity_manager(
        web3_mock).encodeABI.return_value = 'getEntitiesListValue'
    expected_transaction = {
        'to': Web3.toChecksumAddress(IDENTITY_MANAGER_ADDRESS),
        'data': 'getEntitiesListValue',
        'gasPrice': 0,
        'gas': 600000,
        'nonce': '0x0'
    }
    service = IdentityManagerService(web3_mock)

    transaction = service.get_entities_list()

    mock_alastria_identity_manager.assert_called_with(web3_mock)
    mock_alastria_identity_manager(web3_mock).encodeABI.assert_called_with(
        fn_name='entitiesList',
        args=[])
    assert asdict(transaction) == expected_transaction


@patch('alastria_identity.services.identity_manager.ContractsService.AlastriaIdentityManager')
def test_delegated_call(
        mock_alastria_identity_manager):
    web3_mock = Mock()
    data = 'exampleData'
    mock_alastria_identity_manager(
        web3_mock).encodeABI.return_value = 'delegatedValue'
    service = IdentityManagerService(web3_mock)

    transaction = service.delegated(data)

    mock_alastria_identity_manager.assert_called_with(web3_mock)
    mock_alastria_identity_manager(web3_mock).encodeABI.assert_called_with(
        fn_name='delegateCall',
        args=[Web3.toChecksumAddress(IDENTITY_MANAGER_ADDRESS), 0, data])
    assert transaction == 'delegatedValue'
