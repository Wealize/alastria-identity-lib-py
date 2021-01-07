import time
from typing import List
from dataclasses import dataclass, field

from web3 import Web3

from .alastria_session import AlastriaSession
from .alastria_token import AlastriaToken
from .alastria_identity_creation import AlastriaIdentityCreation
from .transaction import Transaction
from .entity import Entity
from .credential import Credential
from .presentation_request import PresentationRequest, PresentationRequestData

DEFAULT_GAS_LIMIT = 600000
DEFAULT_NONCE = '0x0'

@dataclass
class PublicKeyStatus:
    exists: bool
    status: int
    startDate: int
    endDate: int


@dataclass
class JwtToken:
    header: dict
    payload: dict


@dataclass
class Transaction:
    to: str = '0x0000000000000000000000000000000000000000'
    data: str = '0x0'
    gasPrice: int = 0
    nonce: str = DEFAULT_NONCE
    gas: int = DEFAULT_GAS_LIMIT


@dataclass
class IdentityConfig:
    identity_manager: str
    credential_registry: str
    presentation_registry: str
    publickey_registry: str
    basic_transaction: Transaction
    contracts_abi: dict
    zeroValue: str = '00000000000000000000000000000000000000000000000000000000000000000000'


@dataclass
class UserIdentity:
    endpoint: Web3
    address: str
    private_key: str
    nonce: int
    transactions: List


@dataclass
class NetworkDid:
    network: str
    network_id: str
    proxy_address: str

    @classmethod
    def from_did(cls, did: str):
        network_items = did.split(':')
        return NetworkDid(
            network=network_items[2],
            network_id=network_items[3],
            proxy_address=network_items[4]
        )


@dataclass
class UnsignedCredential:
    iss: str
    context: List[str]
    credential_subject: dict
    type: List[str]
    kid: str = ''
    sub: str = ''
    exp: int = 0
    nbf: int = 0
    jti: str = ''
    jwk: str = ''
    REQUIRED_CONTEXT: List[str] = field(default_factory=lambda: [
        'https://www.w3.org/2018/credentials/v1',
        'https://alastria.github.io/identity/credentials/v1'
    ])
    REQUIRED_TYPES: List[str] = field(default_factory=lambda: [
        'VerifiableCredential',
        'AlastriaVerifiableCredential'
    ])

    def get_jwt_payload(self):
        return {
            'header': {
                'typ': 'JWT',
                'alg': 'ES256K',
                'kid': self.kid,
                'jwk': self.jwk
            },
            'payload': {
                'jti': self.jti,
                'iss': self.iss,
                'sub': self.sub,
                'iat': int(time.time()),
                'exp': self.exp,
                'nbf': self.nbf,
                'vc': {
                    '@context': self.context,
                    'type': self.type,
                    'credentialSubject': self.credential_subject
                }
            }
        }


@dataclass
class UnsignedPresentation:
    iss: str
    aud: str
    context: List[str]
    verifiable_credential: List[str]
    proc_url: str
    proc_hash: str
    type: str
    kid: str = ''
    jwk: str = ''
    exp: str = ''
    nbf: str = ''
    jti: str = ''
    REQUIRED_CONTEXT: List[str] = field(default_factory=lambda: [
        'https://www.w3.org/2018/credentials/v1',
        'https://alastria.github.io/identity/credentials/v1'
    ])
    REQUIRED_TYPES: List[str] = field(default_factory=lambda: [
        'VerifiableCredential',
        'AlastriaVerifiablePresentationRequest'
    ])

    def get_jwt_payload(self):
        return {
            'header': {
                'alg': 'ES256K',
                'typ': 'JWT',
                'kid': self.kid,
                'jwk': self.jwk
            },
            'payload': {
                'jti': self.jti,
                'iss': self.iss,
                'aud': self.aud,
                'iat': int(time.time()),
                'exp': self.exp,
                'nbf': self.nbf,
                'vp': {
                    '@context': self.REQUIRED_CONTEXT + self.context,
                    'type': self.REQUIRED_TYPES + self.type,
                    'procHash': self.proc_hash,
                    'procUrl': self.proc_url,
                    'verifiableCredential': self.verifiable_credential
                }
            }
        }
