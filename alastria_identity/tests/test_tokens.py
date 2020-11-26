from mock import *
import time

from alastria_identity.services import TokenService
from alastria_identity.types import NetworkDid

mock_time = Mock()
mock_time.return_value = time.time()

private_key = '0x2c8a1e61b1106b554c3144d85ee47b7fbf9b760b060f4a61a4541fc3c90f6ca4'

def test_create_did_with_network_did():
    expected_did = 'did:ala:789:012:345'
    network_did = NetworkDid.from_did('123:456:789:012:345')
    service = TokenService(private_key=private_key)

    did = service.create_did(network_did)

    assert did == expected_did


def test_create_alastria_token_only_required_args():
    expected_jwt = {
        "header": {
            "alg": "ES256K",
            "typ": "JWT"
        },
        "payload": {
            "iss": "iss",
            "gwu": "gwu",
            "cbu": "cbu",
            "ani": "ani",
            "exp": 1,
            "iat": int(time.time())
        }
    }

    service = TokenService(private_key=private_key)

    jwt = service.create_alastria_token('iss', 'gwu', 'cbu', 'ani', 1)

    assert jwt == expected_jwt

def test_create_alastria_token_all_args():
    expected_jwt = {
        "header": {
            "alg": "ES256K",
            "typ": "JWT",
            "kid": "kid",
            "jwk": "jwk"
        },
        "payload": {
            "iss": "iss",
            "gwu": "gwu",
            "cbu": "cbu",
            "ani": "ani",
            "exp": 1,
            "iat": int(time.time()),
            "nbf": 1,
            "jti": "jti"
        }
    }

    service = TokenService(private_key=private_key)

    jwt = service.create_alastria_token('iss', 'gwu', 'cbu', 'ani', 1, "kid", "jwk", 1, "jti")

    assert jwt == expected_jwt

def test_create_alastria_session_only_required_args():
    expected_jwt = {
        "header": {
            "alg": "ES256K",
            "typ": "JWT"
        },
        "payload": {
            "@context": ['https://alastria.github.io/identity/artifacts/v1', 'CustomContext'],
            "type": ['AlastriaSession', 'CustomType'],
            "iss": "iss",
            "alastriaToken": "0x01234",
            "iat": int(time.time())
        }
    }

    service = TokenService(private_key=private_key)

    jwt = service.create_alastria_session(['CustomContext'], ['CustomType'], 'iss', '0x01234')

    assert jwt == expected_jwt

def test_create_alastria_session_all_args():
    expected_jwt = {
        "header": {
            "alg": "ES256K",
            "typ": "JWT",
            "kid": "kid",
            "jwk": "jwk"
        },
        "payload": {
            "@context": ['https://alastria.github.io/identity/artifacts/v1', 'CustomContext'],
            "type": ['AlastriaSession', 'CustomType'],
            "iss": "iss",
            "alastriaToken": "0x01234",
            "jti": "jti",
            "exp": 1,
            "nbf": 1,
            "iat": int(time.time())
        }
    }

    service = TokenService(private_key=private_key)

    jwt = service.create_alastria_session(['CustomContext'], ['CustomType'], 'iss', '0x01234', 'jti', 1, 1, 'kid', 'jwk')

    assert jwt == expected_jwt

def test_create_alastria_identity_creation_only_required_args():
    expected_jwt = {
        "header": {
            "alg": "ES256K",
            "typ": "JWT",
        },
        "payload": {
            "@context": ['https://alastria.github.io/identity/artifacts/v1', 'CustomContext'],
            "type": ['AlastriaIdentityCreation', 'CustomType'],
            "createAlastriaTX": "0x4321",
            "alastriaToken": "0x01234",
            "publicKey": "0x0011",
            "iat": int(time.time())
        }
    }


    service = TokenService(private_key=private_key)

    jwt = service.create_alastria_identity_creation(['CustomContext'], ['CustomType'], '0x4321', '0x01234', '0x0011')

    assert jwt == expected_jwt

def test_create_alastria_identity_creation_all_args():
    expected_jwt = {
        "header": {
            "alg": "ES256K",
            "typ": "JWT",
            "kid": "kid",
            "jwk": "jwk"
        },
        "payload": {
            "@context": ['https://alastria.github.io/identity/artifacts/v1', 'CustomContext'],
            "type": ['AlastriaIdentityCreation', 'CustomType'],
            "createAlastriaTX": "0x4321",
            "alastriaToken": "0x01234",
            "publicKey": "0x0011",
            "jti": "jti",
            "exp": 1,
            "nbf": 1,
            "iat": int(time.time())
        }
    }

    service = TokenService(private_key=private_key)

    jwt = service.create_alastria_identity_creation(['CustomContext'], ['CustomType'], '0x4321', '0x01234', '0x0011', 'jti', 1, 1, 'kid', 'jwk')

    assert jwt == expected_jwt
