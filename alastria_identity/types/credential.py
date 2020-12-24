import time
from dataclasses import dataclass


@dataclass
class Credential:
    """Creates a Verificable Credential (VC).

    :param iss: Issuer. DID representing the AlastriaID of the entity that issued the VC
    :param context: Additional URLs to W3 and Alastria credentials
    :param credential_subject: dict containing credential.
    If multiple credentials are sent, use a JSON array with the key 'verifiableCredential'
    :param kid: (Optional) Key identifier. Public key id used to sign the JWT
    :param sub: (Optional) Subject. DID representing the AlastriaID of the subject to which the credential refers to
    :param exp: ExpirationTime. The Expiration time of the AT.
    :param nbf: (Optional) NotBefore. Token activation date
    :param jti: (Optional) JWTID. JWT unique identifier
    :param jwk: (Optional) Public key. Users public key
    :param credential_type: (Optional) Type. Additional types to W3 VerifiableCredential and Alastria AlastriaVerifiableCredential
    """

    iss: str
    context: [str]
    credential_subject: dict
    kid: str = None
    sub: str = None
    exp: int = None
    nbf: int = None
    jti: str = None
    jwk: str = None
    credential_type: [str] = None

    def build_jwt(self):
        full_context = [
            'https://www.w3.org/2018/credentials/v1',
            'https://alastria.github.io/identity/credentials/v1'
        ]
        full_types = [
            'VerifiableCredential',
            'AlastriaVerifiableCredential'
        ]
        full_context.extend(self.context)
        full_types.extend(
            self.credential_type) if self.credential_type else None

        header = {
            'alg': 'ES256K',
            'typ': 'JWT',
        }
        payload = {
            'iss': self.iss,
            'iat': int(time.time()),
            'vc': {
                '@context': full_context,
                'type': full_types,
                'credentialSubject': self.credential_subject
            }
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
        params.update(sub=self.sub) if self.sub else None
        params.update(nbf=self.nbf) if self.nbf else None
        params.update(exp=self.exp) if self.exp else None
        return params
