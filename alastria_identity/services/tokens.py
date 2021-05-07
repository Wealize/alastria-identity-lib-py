import base64
import time
import json
from web3 import Web3
from hexbytes import HexBytes

from jwcrypto import jwk, jwt, jws
from ecdsa.keys import SigningKey, VerifyingKey
from ecdsa.curves import SECP256k1
from eth_utils import decode_hex

from alastria_identity.types import (NetworkDid, JwtToken)


class TokenService:
    BASE_HEADER = {
        'alg': 'ES256K',
        'typ': 'JWT'
    }

    def __init__(self, private_key: str):
        private_key = self.remove_starting_hex_prefix(private_key)
        pem = SigningKey.from_string(bytes.fromhex(
            private_key), curve=SECP256k1).to_pem()
        self.signing_key = jwk.JWK.from_pem(pem)
        self.algorithm = 'ES256K'

    def remove_starting_hex_prefix(self, hex_data: str):
        if hex_data.startswith('0x'):
            return hex_data[2:]
        return hex_data

    @staticmethod
    def create_did(network_did: NetworkDid):
        return f'did:ala:{network_did.network}:{network_did.network_id}:{network_did.proxy_address}'

    def sign_jwt(self, jwt_data: JwtToken):
        token = jwt.JWT(header=jwt_data.header,
                        claims=jwt_data.payload, algs=[self.algorithm])
        token.make_signed_token(self.signing_key)
        return token.serialize()

    def verify_jwt(self, jwt_data: str, raw_public_key: str):
        try:
            pem = VerifyingKey.from_string(decode_hex(
                raw_public_key), curve=SECP256k1).to_pem()
            verifying_key = jwk.JWK.from_pem(pem)
            jws_token = jws.JWS(jwt_data)
            jws_token.deserialize(jwt_data)
            jws_token.allowed_algs.extend([self.algorithm])
            jws_token.verify(verifying_key, alg=self.algorithm)
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
