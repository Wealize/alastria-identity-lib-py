import time

from typing import List
from dataclasses import dataclass, field


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
class BasicTransaction:
    to: str = '0x0000000000000000000000000000000000000000'
    data: str = '0x0'
    gas_limit: int = 0
    gas_price: int = 0
    nonce: str = '0x0'


@dataclass
class IdentityConfig:
    identity_manager: str
    credential_registry: str
    presentation_registry: str
    publickey_registry: str
    basic_transaction: BasicTransaction
    contracts_abi: dict
    zeroValue: str = '00000000000000000000000000000000000000000000000000000000000000000000'


@dataclass
class UserIdentity:
    endpoint: str
    address: str
    private_key: str
    nonce: int
    transactions: List


@dataclass
class Transaction:
    # TODO
    pass


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


# TODO Move to TOKENS.py in a types folder
@dataclass
class AlastriaSession:
    context: List[str]
    iss: str
    kid: str
    type: List[str]
    token: str
    exp: int
    pku: str = ''
    nbf: str = ''
    jti: str = ''
    REQUIRED_CONTEXT: List[str] = field(
        default_factory=lambda: [
            'https://alastria.github.io/identity/artifacts/v1'
        ])
    REQUIRED_TYPES: List[str] = field(
        default_factory=lambda: ['AlastriaSession'])

    def get_jwt_payload(self):
        return {
            'headers': {
                'alg': 'ES256K',
                'typ': 'JWT',
                'pku': self.pku,
                'kid': self.kid
            },
            'payload': {
                '@context': self.REQUIRED_CONTEXT + self.context,
                'type': self.REQUIRED_TYPES + self.type,
                'iss': self.iss,
                'iat': int(time.time()),
                'exp': self.exp,
                'nbf': self.nbf,
                'alastriaToken': self.token,
                'jti': self.jti
            }
        }


@dataclass
class AlastriaToken:
    iss: str
    gwu: str
    cbu: str
    ani: str
    exp: int
    kid: str
    jwk: str = ''
    nbf: int = 0
    jti: str = ''

    def get_jwt_payload(self):
        return {
            'header': {
                'alg': 'ES256K',
                'typ': 'JWT',
                'kid': self.kid,
                'jwk': self.jwk
            },
            'payload': {
                'iss': self.iss,
                'gwu': self.gwu,
                'cbu': self.cbu,
                'iat': int(time.time()),
                'ani': self.ani,
                'nbf': self.nbf,
                'exp': self.jti
            }
        }


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
