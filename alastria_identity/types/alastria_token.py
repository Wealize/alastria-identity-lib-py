import time
from dataclasses import dataclass

@dataclass
class AlastriaToken:
    """Creates a Alastria Token (AT).

    :param iss: Issuer. Alastria DID of the sender (issuer) of the AT,
    could be an Issuer or a Service Provider in Alastria ID model terms.
    :param gwu: GatewayURL. Sender's url gateway.
    :param cbu: CallbackURL. Callback URL to which subject answer
    (including user public key) should be addressed.
    :param ani: AlastriaNetworkId. Network Identifier of an Alastria ID
    compatible network
    :param exp: ExpirationTime. The Expiration time of the AT.
    :param kid: (Optional) Key identifier. Public key id used to sign the JWT
    :param jwk: (Optional) Public key. Users public key
    :param nbf: (Optional) NotBefore. Token activation date
    :param jti: (Optional) JWTID. JWT unique identifier
    """

    iss: str
    gwu: str
    cbu: str
    ani: str
    exp: int
    kid: str = None
    jwk: str = None
    nbf: int = None
    jti: str = None

    def build_jwt(self):
        header = {
            'alg': 'ES256K',
            'typ': 'JWT',
        }
        payload = {
            'iss': self.iss,
            'gwu': self.gwu,
            'cbu': self.cbu,
            'ani': self.ani,
            'exp': self.exp,
            'iat': int(time.time())
        }

        if self.kid:
            header.update(kid=self.kid)

        if self.jwk:
            header.update(jwk=self.jwk)

        if self.nbf:
            payload.update(nbf=self.nbf)

        if self.jti:
            payload.update(jti=self.jti)

        return {'header': header, 'payload': payload}
