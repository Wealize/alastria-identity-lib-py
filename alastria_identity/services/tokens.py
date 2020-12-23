import base64
import time
import json
from web3 import Web3
from hexbytes import HexBytes

from jwcrypto import jwk, jwt, jws
from ecdsa.keys import SigningKey
from ecdsa.curves import SECP256k1

from alastria_identity.types import (NetworkDid, JwtToken)


class TokenService:
    BASE_HEADER = {
        'alg': 'ES256K',
        'typ': 'JWT'
    }

    def __init__(self, private_key: str):
        pem = SigningKey.from_string(bytes.fromhex(
            private_key), curve=SECP256k1).to_pem()
        self.signing_key = jwk.JWK.from_pem(pem)
        self.algorithm = 'ES256K'

    def create_did(self, network_did: NetworkDid):
        return f'did:ala:{network_did.network}:{network_did.network_id}:{network_did.proxy_address}'

    def sign_jwt(self, jwt_data: JwtToken):
        token = jwt.JWT(header=jwt_data.header,
                        claims=jwt_data.payload, algs=[self.algorithm])
        token.make_signed_token(self.signing_key)
        return token.serialize()

    def verify_jwt(self, jwt_data: str):
        try:
            jws_token = jws.JWS(jwt_data)
            jws_token.allowed_algs.extend([self.algorithm])
            jws_token.add_signature(self.signing_key, alg=self.algorithm)
            jws_token.verify(self.signing_key, alg=self.algorithm)
            return True
        except jws.InvalidJWSSignature:
            return False

    @staticmethod
    def decode_jwt(jwt_data: str):
        jws_token = jws.JWS(jwt_data)
        jws_token.deserialize(jwt_data)
        return {
            "header": jws_token.jose_header,
            "payload": json.loads(jws_token.objects.get('payload'))
        }

    @staticmethod
    def psm_hash(signed_jwt: str, did: str) -> HexBytes:
        return Web3.keccak(text=f'{signed_jwt}{did}')
