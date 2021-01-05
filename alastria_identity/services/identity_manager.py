from web3 import Web3

from alastria_identity.types import (
    Transaction,
    NetworkDid,
    Entity)
from alastria_identity.services import IdentityConfigBuilder, ContractsService, IDENTITY_MANAGER_ADDRESS


class IdentityManagerService:
    def __init__(self, endpoint: Web3):
        self.endpoint = endpoint

    def prepare_alastria_id(self, sign_address: str) -> Transaction:
        data = self.delegated(ContractsService.AlastriaIdentityManager(self.endpoint).encodeABI(
            fn_name="prepareAlastriaID",
            args=[sign_address]
        ))

        return Transaction(
            to=Web3.toChecksumAddress(IDENTITY_MANAGER_ADDRESS),
            data=data)

    def create_alastria_identity(self, public_key: str) -> Transaction:
        public_key_data = ContractsService.AlastriaPublicKeyRegistry(self.endpoint).encodeABI(
            fn_name="addKey",
            args=[public_key])
        data = ContractsService.AlastriaIdentityManager(self.endpoint).encodeABI(
            fn_name="createAlastriaIdentity",
            args=[public_key_data])

        return Transaction(
            to=Web3.toChecksumAddress(IDENTITY_MANAGER_ADDRESS),
            data=data)

    def add_idendity_issuer(self, did_issuer: str, level: int) -> Transaction:
        issuer_address = NetworkDid.from_did(did_issuer).proxy_address
        data = self.delegated(ContractsService.AlastriaIdentityManager(self.endpoint).encodeABI(
            fn_name='addIdentityIssuer',
            args=[issuer_address, level]))
        return Transaction(
            to=Web3.toChecksumAddress(IDENTITY_MANAGER_ADDRESS),
            data=data
        )

    def update_identity_issuer_eidas_level(self, did_issuer: str, level: int) -> Transaction:
        issuer_address = NetworkDid.from_did(did_issuer).proxy_address
        data = self.delegated(ContractsService.AlastriaIdentityManager(self.endpoint).encodeABI(
            fn_name='updateIdentityIssuerEidasLevel',
            args=[issuer_address, level]))
        return Transaction(
            to=Web3.toChecksumAddress(IDENTITY_MANAGER_ADDRESS),
            data=data
        )

    def delete_identity_issuer(self, did_issuer: str) -> Transaction:
        issuer_address = NetworkDid.from_did(did_issuer).proxy_address
        data = self.delegated(ContractsService.AlastriaIdentityManager(self.endpoint).encodeABI(
            fn_name='deleteIdentityIssuer',
            args=[issuer_address]))
        return Transaction(
            to=Web3.toChecksumAddress(IDENTITY_MANAGER_ADDRESS),
            data=data
        )

    def get_eidas_level(self, did_issuer: str) -> Transaction:
        issuer_address = NetworkDid.from_did(did_issuer).proxy_address
        data = ContractsService.AlastriaIdentityManager(self.endpoint).encodeABI(
            fn_name='getEidasLevel',
            args=[issuer_address])
        return Transaction(
            to=Web3.toChecksumAddress(IDENTITY_MANAGER_ADDRESS),
            data=data
        )

    def add_identity_service_provider(self, did_service_provider: str) -> Transaction:
        provider_address = NetworkDid.from_did(
            did_service_provider).proxy_address
        data = self.delegated(ContractsService.AlastriaIdentityManager(self.endpoint).encodeABI(
            fn_name='addIdentityServiceProvider',
            args=[provider_address]))
        return Transaction(
            to=Web3.toChecksumAddress(IDENTITY_MANAGER_ADDRESS),
            data=data
        )

    def delete_identity_service_provider(self, did_service_provider: str) -> Transaction:
        provider_address = NetworkDid.from_did(
            did_service_provider).proxy_address
        data = self.delegated(ContractsService.AlastriaIdentityManager(self.endpoint).encodeABI(
            fn_name='deleteIdentityServiceProvider',
            args=[provider_address]))
        return Transaction(
            to=Web3.toChecksumAddress(IDENTITY_MANAGER_ADDRESS),
            data=data
        )

    def is_identity_service_provider(self, did_service_provider: str) -> Transaction:
        provider_address = NetworkDid.from_did(
            did_service_provider).proxy_address
        data = ContractsService.AlastriaIdentityManager(self.endpoint).encodeABI(
            fn_name='isIdentityServiceProvider',
            args=[provider_address])
        return Transaction(
            to=Web3.toChecksumAddress(IDENTITY_MANAGER_ADDRESS),
            data=data
        )

    def is_identity_issuer(self, did_issuer: str) -> Transaction:
        issuer_address = NetworkDid.from_did(did_issuer).proxy_address
        data = ContractsService.AlastriaIdentityManager(self.endpoint).encodeABI(
            fn_name='isIdentityIssuer',
            args=[issuer_address])
        return Transaction(
            to=Web3.toChecksumAddress(IDENTITY_MANAGER_ADDRESS),
            data=data
        )

    def add_entity(self, entity: Entity) -> Transaction:
        entity_address = NetworkDid.from_did(entity.did_entity).proxy_address
        data = self.delegated(ContractsService.AlastriaIdentityManager(self.endpoint).encodeABI(
            fn_name='addEntity',
            args=[entity_address,
                  entity.name,
                  entity.cif,
                  entity.url_logo,
                  entity.url_create_aid,
                  entity.url_aoa,
                  entity.status]))
        return Transaction(
            to=Web3.toChecksumAddress(IDENTITY_MANAGER_ADDRESS),
            data=data
        )

    def set_entity_name(self, entity: Entity) -> Transaction:
        entity_address = NetworkDid.from_did(entity.did_entity).proxy_address
        data = self.delegated(ContractsService.AlastriaIdentityManager(self.endpoint).encodeABI(
            fn_name='setNameEntity',
            args=[entity.name]))
        return Transaction(
            to=Web3.toChecksumAddress(IDENTITY_MANAGER_ADDRESS),
            data=data
        )

    def set_entity_cif(self, entity: Entity) -> Transaction:
        entity_address = NetworkDid.from_did(entity.did_entity).proxy_address
        data = self.delegated(ContractsService.AlastriaIdentityManager(self.endpoint).encodeABI(
            fn_name='setCifEntity',
            args=[entity.cif]))
        return Transaction(
            to=Web3.toChecksumAddress(IDENTITY_MANAGER_ADDRESS),
            data=data
        )

    def set_entity_url_logo(self, entity: Entity) -> Transaction:
        entity_address = NetworkDid.from_did(entity.did_entity).proxy_address
        data = self.delegated(ContractsService.AlastriaIdentityManager(self.endpoint).encodeABI(
            fn_name='setUrlLogo',
            args=[entity.url_logo]))
        return Transaction(
            to=Web3.toChecksumAddress(IDENTITY_MANAGER_ADDRESS),
            data=data
        )

    def set_entity_url_create_aid(self, entity: Entity) -> Transaction:
        entity_address = NetworkDid.from_did(entity.did_entity).proxy_address
        data = self.delegated(ContractsService.AlastriaIdentityManager(self.endpoint).encodeABI(
            fn_name='setUrlCreateAID',
            args=[entity.url_create_aid]))
        return Transaction(
            to=Web3.toChecksumAddress(IDENTITY_MANAGER_ADDRESS),
            data=data
        )

    def set_entity_url_aoa_aid(self, entity: Entity) -> Transaction:
        entity_address = NetworkDid.from_did(entity.did_entity).proxy_address
        data = self.delegated(ContractsService.AlastriaIdentityManager(self.endpoint).encodeABI(
            fn_name='setUrlAOA',
            args=[entity.url_aoa]))
        return Transaction(
            to=Web3.toChecksumAddress(IDENTITY_MANAGER_ADDRESS),
            data=data
        )

    def get_entity(self, entity: Entity) -> Transaction:
        entity_address = NetworkDid.from_did(entity.did_entity).proxy_address
        data = ContractsService.AlastriaIdentityManager(self.endpoint).encodeABI(
            fn_name='getEntity',
            args=[entity_address])
        return Transaction(
            to=Web3.toChecksumAddress(IDENTITY_MANAGER_ADDRESS),
            data=data
        )

    def get_entities_list(self) -> Transaction:
        data = ContractsService.AlastriaIdentityManager(self.endpoint).encodeABI(
            fn_name='entitiesList',
            args=[])
        return Transaction(
            to=Web3.toChecksumAddress(IDENTITY_MANAGER_ADDRESS),
            data=data
        )

    def get_identity_key(self, address: str) -> Transaction:
        data = ContractsService.AlastriaIdentityManager(self.endpoint).encodeABI(
            fn_name='identityKeys',
            args=[address])
        return Transaction(
            to=Web3.toChecksumAddress(IDENTITY_MANAGER_ADDRESS),
            data=data
        )

    def delegated(self, delegated_data) -> str:
        return ContractsService.AlastriaIdentityManager(self.endpoint).encodeABI(
            fn_name='delegateCall',
            args=[Web3.toChecksumAddress(
                IDENTITY_MANAGER_ADDRESS), 0, delegated_data]
        )
