import time
from dataclasses import dataclass


@dataclass
class AlastriaIdentityCreation:
    """Creates a Alastria Identity Creation (AIC).

    Is the JWT object sent by the subject from his/her wallet to register an
    Alastria DID, thus completing the creation of an Alastria ID

    :param context: It should be at least "https://alastria.github.io/identity/artifacts/v1",
    more urls with other specifications are allowed
    :param object_type: It should be "AlastriaIdentityCreation", more objects
    names are allowed
    :param create_alastria_tx: Hex coded (with initial 0x) create_alastria_identity
    Transaction, signed by the subject.
    :param alastria_token: The original Alastria Token (AT) to which this
    Alastria Session is sent as answer. Coded as a 64BaseURL JWT.
    Is not signed by the subject, because it is included in a subject
    signed JWT, the AIC.
    :param public_key: Hex coded (with initial 0x) Subject's Public Key.
    :param jti: (Optional) JWTID. JWT unique identifier
    :param exp: (Optional) ExpirationTime. The Expiration time of the AS.
    :param nbf: (Optional) NotBefore. Token activation date
    :param kid: (Optional) Key identifier. Public key id used to sign the JWT
    :param jwk: (Optional) Public key. Users public key
    """
    context: [str]
    object_type: [str]
    create_alastria_tx: str
    alastria_token: str
    public_key: str
    jti: str = None
    exp: int = None
    nbf: int = None
    kid: str = None
    jwk: str = None

    def build_jwt(self):
        full_context = ['https://alastria.github.io/identity/artifacts/v1']
        full_types = ['AlastriaIdentityCreation']
        full_context.extend(self.context)
        full_types.extend(self.object_type)

        header = {
            'alg': 'ES256K',
            'typ': 'JWT',
        }

        payload = {
            '@context': full_context,
            'type': full_types,
            'createAlastriaTX': self.create_alastria_tx,
            'alastriaToken': self.alastria_token,
            'publicKey': self.public_key,
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

