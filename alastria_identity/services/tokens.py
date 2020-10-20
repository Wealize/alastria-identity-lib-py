import jwt

from alastria_identity.types import NetworkDid


class TokenService:
    def __init__(self, secret: str, algorithm: str):
        self.secret = secret
        self.algorithms = [algorithm]

    def create_did(self, network_did: NetworkDid):
        return f'did:ala:{network_did.network}:{network_did.network_id}:{network_did.proxy_address}'

    def decode_jwt(self, jwt_token: str) -> dict:
        if not jwt_token:
            return {}

        return jwt.decode(
            jwt_token,
            self.secret,
            algorithms=self.algorithms)
