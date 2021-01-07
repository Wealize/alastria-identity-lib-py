from mock import *
import time
from hexbytes import HexBytes

from eth_keys import keys
from eth_utils import decode_hex

from alastria_identity.services import TokenService
from alastria_identity.types import (
    NetworkDid,
    JwtToken,
    AlastriaSession,
    AlastriaToken,
    AlastriaIdentityCreation,
    Credential,
    PresentationRequest,
    PresentationRequestData
)

mock_time = Mock()
mock_time.return_value = time.time()

first_private_key = '1da6847600b0ee25e9ad9a52abbd786dd2502fa4005dd5af9310b7cc7a3b25db'
first_public_key = keys.PrivateKey(
    decode_hex(first_private_key)).public_key.to_hex()
second_private_key = '5f25043160494cc82f7054ea935ebb7d9ac67bbe336ddf11b3b61b8d4731009e'
second_public_key = keys.PrivateKey(
    decode_hex(second_private_key)).public_key.to_hex()


def test_jwt_verification_with_correct_public_key():
    jwt = JwtToken(
        header={
            "alg": "ES256K",
            "typ": "JWT"
        },
        payload={
            "iss": "iss",
            "gwu": "gwu",
            "cbu": "cbu",
            "ani": "ani",
            "exp": 1,
            "iat": int(time.time())
        })

    service = TokenService(private_key=first_private_key)
    signed_jwt = service.sign_jwt(jwt)
    decoded_jwt = TokenService.decode_jwt(signed_jwt)

    assert service.verify_jwt(signed_jwt, first_public_key)
    assert decoded_jwt.get('header') == jwt.header
    assert decoded_jwt.get('payload') == jwt.payload


def test_jwt_verification_with_incorrect_public_key():
    jwt = JwtToken(
        header={
            "alg": "ES256K",
            "typ": "JWT"
        },
        payload={
            "iss": "iss",
            "gwu": "gwu",
            "cbu": "cbu",
            "ani": "ani",
            "exp": 1,
            "iat": int(time.time())
        })

    service = TokenService(private_key=first_private_key)
    signed_jwt = service.sign_jwt(jwt)
    decoded_jwt = TokenService.decode_jwt(signed_jwt)

    assert not service.verify_jwt(signed_jwt, second_public_key)
    assert decoded_jwt.get('header') == jwt.header
    assert decoded_jwt.get('payload') == jwt.payload


def test_create_did_with_network_did():
    expected_did = 'did:ala:789:012:345'
    network_did = NetworkDid.from_did('123:456:789:012:345')
    service = TokenService(private_key=first_private_key)

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

    jwt = AlastriaToken('iss', 'gwu', 'cbu', 'ani', 1).build_jwt()

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

    jwt = AlastriaToken('iss', 'gwu', 'cbu', 'ani', 1,
                        "kid", "jwk", 1, "jti").build_jwt()

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

    jwt = AlastriaSession(['CustomContext'], ['CustomType'],
                          'iss', '0x01234').build_jwt()

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

    jwt = AlastriaSession(['CustomContext'], ['CustomType'],
                          'iss', '0x01234', 'jti', 1, 1, 'kid', 'jwk').build_jwt()

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

    jwt = AlastriaIdentityCreation(
        ['CustomContext'], ['CustomType'], '0x4321', '0x01234', '0x0011').build_jwt()

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

    service = TokenService(private_key=first_private_key)

    jwt = AlastriaIdentityCreation(['CustomContext'], [
                                   'CustomType'], '0x4321', '0x01234', '0x0011', 'jti', 1, 1, 'kid', 'jwk').build_jwt()

    assert jwt == expected_jwt


def test_psmhash():
    foo_signed_jwt = '''
                    eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NksiLCJraWQiOiJkaWQ6YWxhOnF1b3I6cmVkVDo4ZjQ0MDA0O
                    WNiYmU1YzZiYzllZmY0NjM2OWY5MDkxZjFkODEzMzNjI2tleXMtMSJ9.
                    eyJqdGkiOiJmaGJ0aDlocnVkbCIsImlzcyI6ImRpZDphbGE6cXVvcjpyZWRUOjhmNDQwMDQ5Y2JiZTVjNmJjOW
                    VmZjQ2MzY5ZjkwOTFmMWQ4MTMzM2MiLCJzdWIiOiJkaWQ6YWxhOnF1b3I6cmVkVDowYTc3ODAyOTVhYjgwNmY4
                    Y2RiNjIzY2ZhNDhhNzQ5ZTk1OTE4MTU5IiwiaWF0IjoxNTkxMTczNjkzLCJleHAiOjE1OTEyNjAwOTMxNDMsIm
                    5iZiI6MTU5MTE3MzY5MzE0MywidmMiOnsiQGNvbnRleHQiOlsiaHR0cHM6Ly93d3cudzMub3JnLzIwMTgvY3Jl
                    ZGVudGlhbHMvdjEiLCJKV1QiXSwidHlwZSI6WyJWZXJpZmlhYmxlQ3JlZGVudGlhbCIsIkFsYXN0cmlhRXhhbX
                    BsZUNyZWRlbnRpYWwiXSwiY3JlZGVudGlhbFN1YmplY3QiOnsibGV2ZWxPZkFzc3VyYW5jZSI6MywiZnVsbG5h
                    bWUiOiJEYW5pZWwgZGUgbGEgU290YSJ9fX0.
                    DZsssNSg0_NzrjSiCNrkVss9-bnUZxFrbH6oN9NluCJwg0MqwAvyvwtKww_f_lF1sMVXt6UZyl_gJEkCSaspWw',
                    'eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NksiLCJraWQiOiJkaWQ6YWxhOnF1b3I6cmVkVDo4ZjQ0MDA0OWNiY
                    mU1YzZiYzllZmY0NjM2OWY5MDkxZjFkODEzMzNjI2tleXMtMSJ9.
                    '''
    foo_did = 'did:ala:quor:redT:8f440049cbbe5c6bc9eff46369f9091f1d81333'
    expected_psmash = HexBytes(
        '0xdb61eb3ad9020e8fe0509618a8579fe350cb16be20fbfd43a098e152fa9b3a31')

    psmhash = TokenService.psm_hash(foo_signed_jwt, foo_did)

    assert psmhash == expected_psmash


def test_create_credential_only_required_args():
    expected_jwt = {
        "header": {
            "alg": "ES256K",
            "typ": "JWT",
        },
        "payload": {
            'iss': 'iss',
            "iat": int(time.time()),
            "vc": {
                "@context": ['https://www.w3.org/2018/credentials/v1', 'https://alastria.github.io/identity/credentials/v1', 'CustomContext'],
                "type": ['VerifiableCredential', 'AlastriaVerifiableCredential'],
                "credentialSubject": {
                    "levelOfAssurance": 3,
                    "covid_test": {
                        "name": "Perico Perez",
                        "mail": "perico.perez@example.com",
                        "test_result": "negative"
                    }
                }
            }
        }
    }

    service = TokenService(private_key=first_private_key)

    jwt = Credential(
        'iss',
        ['CustomContext'],
        {
            "levelOfAssurance": 3,
            "covid_test": {
                "name": "Perico Perez",
                "mail": "perico.perez@example.com",
                "test_result": "negative"
            }
        }).build_jwt()

    assert jwt == expected_jwt


def test_create_credential_all_args():
    expected_jwt = {
        "header": {
            "alg": "ES256K",
            "typ": "JWT",
            "kid": "kid",
            "jwk": "jwk"
        },
        "payload": {
            "iss": "iss",
            "iat": int(time.time()),
            "jti": "jti",
            "sub": "sub",
            "nbf": 100,
            "exp": 10,
            "vc": {
                "@context": ['https://www.w3.org/2018/credentials/v1', 'https://alastria.github.io/identity/credentials/v1', 'CustomContext'],
                "type": ['VerifiableCredential', 'AlastriaVerifiableCredential', 'CustomType'],
                "credentialSubject": {
                    "levelOfAssurance": 3,
                    "covid_test": {
                        "name": "Perico Perez",
                        "mail": "perico.perez@example.com",
                        "test_result": "negative"
                    }
                }
            }
        }
    }

    service = TokenService(private_key=first_private_key)

    jwt = Credential(
        'iss',
        ['CustomContext'],
        {
            "levelOfAssurance": 3,
            "covid_test": {
                "name": "Perico Perez",
                "mail": "perico.perez@example.com",
                "test_result": "negative"
            }
        },
        'kid',
        'sub',
        10,
        100,
        'jti',
        'jwk',
        ['CustomType']).build_jwt()

    assert jwt == expected_jwt


def test_create_presentation_request_data_required_args():
    expected_data = {
        '@context': [
            'https://www.w3.org/2018/credentials/v1',
            'https://alastria.github.io/identity/credentials/v1'
        ],
        'type': [
            'VerifiablePresentationRequest',
            'AlastriaVerifiablePresentationRequest'
        ],
        'levelOfAssurance': 0,
        'required': True,
        'field_name': 'example_name'
    }

    data = PresentationRequestData(required=True, field_name='example_name').build_data()

    assert data == expected_data


def test_create_presentation_request_data_all_args():
    expected_data = {
        '@context': [
            'https://www.w3.org/2018/credentials/v1',
            'https://alastria.github.io/identity/credentials/v1',
            'https://alastria.github.io/identity/covid'
        ],
        'type': [
            'VerifiablePresentationRequest',
            'AlastriaVerifiablePresentationRequest',
            'CustomType'
        ],
        'levelOfAssurance': 2,
        'required': True,
        'field_name': 'example_name'
    }

    data = PresentationRequestData(
        required=True,
        field_name='example_name',
        context=['https://alastria.github.io/identity/covid'],
        type=['CustomType'],
        level_of_assurance=2
    ).build_data()

    assert data == expected_data


def test_create_presentation_request_required_args():
    expected_jwt = {
        'header': {
            'alg': 'ES256K',
            'typ': 'JWT'
        },
        'payload': {
            'iss': 'did:alastria:quorum:testnet1:3eabc53a85',
            'iat': int(time.time()),
            'cbu': 'https://alastria.github.io/callback',
            'pr': {
                '@context': [
                    'https://www.w3.org/2018/credentials/v1',
                    'https://alastria.github.io/identity/credentials/v1'
                ],
                'type': [
                    'VerifiablePresentationRequest',
                    'AlastriaVerifiablePresentationRequest'
                ],
                'procHash': 'H398sjHd...kldjUYn475n',
                'procUrl': 'https://alastria.github.io/data',
                'data': [
                    {
                        '@context': [
                            'https://www.w3.org/2018/credentials/v1',
                            'https://alastria.github.io/identity/credentials/v1'
                        ],
                        'type': [
                            'VerifiablePresentationRequest',
                            'AlastriaVerifiablePresentationRequest'
                        ],
                        'levelOfAssurance': 0,
                        'required': True,
                        'field_name': 'field_1'
                    },
                    {
                        '@context': [
                            'https://www.w3.org/2018/credentials/v1',
                            'https://alastria.github.io/identity/credentials/v1',
                            'https://alastria.github.io/identity/covid'
                        ],
                        'type': [
                            'VerifiablePresentationRequest',
                            'AlastriaVerifiablePresentationRequest',
                            'CustomType'
                        ],
                        'levelOfAssurance': 1,
                        'required': False,
                        'field_name': 'field_2'
                    }
                ]
            }
        }
    }

    jwt = PresentationRequest(
        iss='did:alastria:quorum:testnet1:3eabc53a85',
        cbu='https://alastria.github.io/callback',
        proc_hash='H398sjHd...kldjUYn475n',
        proc_url='https://alastria.github.io/data',
        data=[
            PresentationRequestData(required=True, field_name='field_1'),
            PresentationRequestData(
                required=False,
                field_name='field_2',
                context=['https://alastria.github.io/identity/covid'],
                type=['CustomType'],
                level_of_assurance=1
            )
        ]
    ).build_jwt()

    assert jwt == expected_jwt


def test_create_presentation_request_all_args():
    expected_jwt = {
        'header': {
            'alg': 'ES256K',
            'typ': 'JWT',
            'kid': 'did:etc',
            'jwk': '0x123456'
        },
        'payload': {
            'jti': 'alastria',
            'iss': 'did:alastria:quorum:testnet1:3eabc53a85',
            'iat': int(time.time()),
            'exp': 100,
            'nbf': 200,
            'cbu': 'https://alastria.github.io/callback',
            'pr': {
                '@context': [
                    'https://www.w3.org/2018/credentials/v1',
                    'https://alastria.github.io/identity/credentials/v1',
                    'https://alastria.github.io/identity/covid'
                ],
                'type': [
                    'VerifiablePresentationRequest',
                    'AlastriaVerifiablePresentationRequest',
                    'CustomType'
                ],
                'procHash': 'H398sjHd...kldjUYn475n',
                'procUrl': 'https://alastria.github.io/data',
                'data': [
                    {
                        '@context': [
                            'https://www.w3.org/2018/credentials/v1',
                            'https://alastria.github.io/identity/credentials/v1'
                        ],
                        'type': [
                            'VerifiablePresentationRequest',
                            'AlastriaVerifiablePresentationRequest'
                        ],
                        'levelOfAssurance': 0,
                        'required': True,
                        'field_name': 'field_1'
                    },
                    {
                        '@context': [
                            'https://www.w3.org/2018/credentials/v1',
                            'https://alastria.github.io/identity/credentials/v1',
                            'https://alastria.github.io/identity/covid'
                        ],
                        'type': [
                            'VerifiablePresentationRequest',
                            'AlastriaVerifiablePresentationRequest',
                            'CustomType'
                        ],
                        'levelOfAssurance': 1,
                        'required': False,
                        'field_name': 'field_2'
                    }
                ]
            }
        }
    }

    jwt = PresentationRequest(
        iss='did:alastria:quorum:testnet1:3eabc53a85',
        cbu='https://alastria.github.io/callback',
        proc_hash='H398sjHd...kldjUYn475n',
        proc_url='https://alastria.github.io/data',
        data=[
            PresentationRequestData(required=True, field_name='field_1'),
            PresentationRequestData(
                required=False,
                field_name='field_2',
                context=['https://alastria.github.io/identity/covid'],
                type=['CustomType'],
                level_of_assurance=1
            )
        ],
        jti='alastria',
        exp=100,
        nbf=200,
        context=['https://alastria.github.io/identity/covid'],
        type=['CustomType'],
        kid='did:etc',
        jwk='0x123456'
    ).build_jwt()

    assert jwt == expected_jwt