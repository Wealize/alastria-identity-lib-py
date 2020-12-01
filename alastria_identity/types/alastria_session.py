import time
from dataclasses import dataclass


@dataclass
class AlastriaSession:
    """Creates a Alastria Session (AS).

    :param context(list): It should be at least "https://alastria.github.io/identity/artifacts/v1",
    more urls with other specifications are allowed
    :param tipo(str): It should be at least "AlastriaSession", more objects
    names are allowed
    :param iss: Issuer. DID of the issuer of the Alastria Session. It is
    usually the subject/user in Alastria ID model.
    :param alastria_token: The original Alastria Token (AT) to which this
    Alastria Session is sent as answer. Coded as a 64BaseURL JWT
    :param jti: (Optional) JWTID. JWT unique identifier

    :param exp: (Optional) ExpirationTime. The Expiration time of the AS.
    :param nbf: (Optional) NotBefore. Token activation date
    :param kid: (Optional) Key identifier. Public key id used to sign the JWT
    :param jwk: (Optional) Public key. Users public key
    """
    context: [str]
    tipo: [str]
    iss: str
    alastria_token: str
    jti: str = None
    exp: int = None
    nbf: int = None
    kid: str = None
    jwk: str = None

    def build_jwt(self):
        full_context = ['https://alastria.github.io/identity/artifacts/v1']
        full_types = ['AlastriaSession']
        full_context.extend(self.context)
        full_types.extend(self.tipo)

        header = {
            'alg': 'ES256K',
            'typ': 'JWT',
        }

        payload = {
            '@context': full_context,
            'type': full_types,
            'iss': self.iss,
            'alastriaToken': self.alastria_token,
            'iat': int(time.time())
        }

        header.update(**self.get_optional_header_params())
        payload.update(**self.get_optional_payload_params())

        return {'header': header, 'payload': payload}

    def get_optional_header_params(self) -> dict:
        params = {}
        params.update(kid=self.kid) if self.kid else None
        params.update(jwk=self.jwk) if self.jwk else None
        return params

    def get_optional_payload_params(self) -> dict:
        params = {}
        params.update(jti=self.jti) if self.jti else None
        params.update(exp=self.exp) if self.exp else None
        params.update(nbf=self.nbf) if self.nbf else None
        return params
