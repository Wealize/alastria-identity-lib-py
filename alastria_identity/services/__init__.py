from .config_builder import IdentityConfigBuilder
from .contracts import (
    IDENTITY_MANAGER_ADDRESS,
    ContractsService,
    PUBLIC_KEY_REGISTRY_ADDRESS,
    PRESENTATION_REGISTRY_ADDRESS,
    CREDENTIAL_REGISTRY_ADDRESS
)
from .credential_registry import CredentialRegistryService
from .identity import UserIdentityService
from .identity_manager import IdentityManagerService
from .parsers import ContractParser
from .presentation_registry import PresentationRegistryService
from .tokens import TokenService
from .public_key import PublicKeyService
