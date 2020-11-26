import base64
import time

# from jsontokens import TokenSigner, TokenVerifier, decode_token

from alastria_identity.types import NetworkDid


class TokenService:
    def __init__(self, private_key: str):
        # self.token_signer = TokenSigner()
        # self.token_verifier = TokenVerifier()
        self.private_key = private_key
        self.algorithm = 'ES256K'

    def create_did(self, network_did: NetworkDid):
        return f'did:ala:{network_did.network}:{network_did.network_id}:{network_did.proxy_address}'

    def sign_jwt(self, jwt: dict):
        # return self.sign(jwt, self.private_key)
        pass

    def verify_jwt(self, jwt: str):
        # return self.verify_jwt(jwt, self.private_key)
        pass

    def decode_jwt(self, jwt: str):
        # return decode_token(jwt)
        pass

    def create_alastria_token(self,
                              iss: str,
                              gwu: str,
                              cbu: str,
                              ani: str,
                              exp: int,
                              kid: str = None,
                              jwk: str = None,
                              nbf: int = None,
                              jti: str = None):
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
        header = dict()
        payload = dict()

        header.update(
            alg='ES256K',
            typ='JWT'
        )

        payload.update(
            iss=iss,
            gwu=gwu,
            cbu=cbu,
            ani=ani,
            exp=exp,
            iat=int(time.time())
        )

        if kid:
            header.update(kid=kid)

        if jwk:
            header.update(jwk=jwk)

        if nbf:
            payload.update(nbf=nbf)

        if jti:
            payload.update(jti=jti)

        return {'header': header, 'payload': payload}

    def create_alastria_session(
            self,
            context: [str],
            type: [str],
            iss: str,
            alastria_token: str,
            jti: str = None,
            exp: int = None,
            nbf: int = None,
            kid: str = None,
            jwk: str = None):
        """Creates a Alastria Session (AS).

        :param context: It should be at least "https://alastria.github.io/identity/artifacts/v1",
        more urls with other specifications are allowed
        :param type: It should be at least "AlastriaSession", more objects
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
        header = dict()
        payload = dict()
        full_context = ['https://alastria.github.io/identity/artifacts/v1']
        full_context.extend(context)
        full_types = ['AlastriaSession']
        full_types.extend(type)

        header.update(
            alg='ES256K',
            typ='JWT'
        )

        payload["@context"] = full_context

        payload.update(
            type=full_types,
            iss=iss,
            alastriaToken=alastria_token,
            iat=int(time.time())
        )

        if kid:
            header.update(kid=kid)

        if jwk:
            header.update(jwk=jwk)

        if jti:
            payload.update(jti=jti)

        if exp:
            payload.update(exp=exp)

        if nbf:
            payload.update(nbf=nbf)

        return {'header': header, 'payload': payload}

    def create_alastria_identity_creation(
            self,
            context: [str],
            type: [str],
            create_alastria_tx: str,
            alastria_token: str,
            public_key: str,
            jti: str = None,
            exp: int = None,
            nbf: int = None,
            kid: str = None,
            jwk: str = None):
        """Creates a Alastria Identity Creation (AIC).

        Is the JWT object sent by the subject from his/her wallet to register an
        Alastria DID, thus completing the creation of an Alastria ID

        :param context: It should be at least "https://alastria.github.io/identity/artifacts/v1",
        more urls with other specifications are allowed
        :param type: It should be "AlastriaIdentityCreation", more objects
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
        header = dict()
        payload = dict()
        full_context = ['https://alastria.github.io/identity/artifacts/v1']
        full_context.extend(context)
        full_types = ['AlastriaIdentityCreation']
        full_types.extend(type)

        header.update(
            alg='ES256K',
            typ='JWT'
        )

        payload["@context"] = full_context

        payload.update(
            type=full_types,
            createAlastriaTX=create_alastria_tx,
            alastriaToken=alastria_token,
            publicKey=public_key,
            iat=int(time.time())
        )

        if kid:
            header.update(kid=kid)

        if jwk:
            header.update(jwk=jwk)

        if jti:
            payload.update(jti=jti)

        if exp:
            payload.update(exp=exp)

        if nbf:
            payload.update(nbf=nbf)

        return {'header': header, 'payload': payload}

    def create_credential():
        pass

    def create_presentation_request():
        pass

    def create_presentation():
        pass

    def psm_hash():
        pass
