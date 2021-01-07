
import time

from dataclasses import dataclass, field
from typing import List


@dataclass
class PresentationRequestData:
    """Creates data items for Presentation Request.

    :param required: Its value specifies if the field is compulsory (true) or optional (false).
    :param field_name: The name of the required field, as defined in the ontology specified in @context.
    :param context: (Optional) Additional urls to "https://www.w3.org/2018/credentials/v1" and "https://alastria.github.io/identity/credentials/v1"
    :param type: (Optional) Aditional types to "VerifiablePresentationRequest" and "AlastriaVerifiablePresentationRequest"
    :param level_of_assurance: (Optional) Corresponds to the eIDAS assurance levels ("Self", "Low", "Substantial", "High"). Default value is "Self". 0 for "Self", 1 for "Low", 2 for "Substantial" and 3 for "High"
    """

    required: bool
    field_name: str
    context: List[str] = field(default_factory=list)
    type: List[str] = field(default_factory=list)
    level_of_assurance: int = 0
    
    def build_data(self) -> dict:
        full_context = [
            'https://www.w3.org/2018/credentials/v1',
            'https://alastria.github.io/identity/credentials/v1'
        ]
        full_types = [
            'VerifiablePresentationRequest',
            'AlastriaVerifiablePresentationRequest'
        ]

        full_context.extend(self.context)
        full_types.extend(self.type)

        return {
            '@context': full_context,
            'type': full_types,
            'levelOfAssurance': self.level_of_assurance,
            'required': self.required,
            'field_name': self.field_name
        }


@dataclass
class PresentationRequest:
    """Creates a Presentation Request.

    :param iss: DID representing the Alastria.ID of the entity that sent the Presentation Request
    :param cbu: Callback url from the user
    :param proc_hash: The hash of an external document describing the intended purpose of the data that the service provider is requesting
    :param proc_url: The URL of an external document describing the intended purpose of the data that the service provider is receiving
    :param data: List of PresentationRequestData that contains the actual Presentation Request data items. See PresentationRequestData
    :param jti: (Optional) This is the identification of this specific Presentation Request (it is NOT the identifier of the holder or of any other actor)
    :param exp: (Optional) Identifies the expiration time on or after which the JWT (Presentation Request) MUST NOT be accepted for processing
    :param nbf: (Optional) Identifies the time before which the JWT (presentation) MUST NOT be accepted for processing
    :param context: (Optional) Additional urls to "https://www.w3.org/2018/credentials/v1" and "https://alastria.github.io/identity/credentials/v1"
    :param type: (Optional) Aditional types to "VerifiablePresentationRequest" and "AlastriaVerifiablePresentationRequest"
    :param kid: (Optional) Key identifier. Public key id used to sign the JWT
    :param jwk: (Optional) Public key which was used to sign the JWT
    """

    iss: str
    cbu: str
    proc_hash: str
    proc_url: str
    data: List[PresentationRequestData]
    jti: str = None
    exp: int = None
    nbf: int = None
    context: List[str] = field(default_factory=list)
    type: List[str] = field(default_factory=list)
    kid: str = None
    jwk: str = None

    def build_jwt(self) -> dict:
        full_context = [
            'https://www.w3.org/2018/credentials/v1',
            'https://alastria.github.io/identity/credentials/v1'
        ]
        full_types = [
            'VerifiablePresentationRequest',
            'AlastriaVerifiablePresentationRequest'
        ]

        full_context.extend(self.context)
        full_types.extend(self.type)

        header = {
            'alg': 'ES256K',
            'typ': 'JWT'
        }
        payload = {
            'iss': self.iss,
            'iat': int(time.time()),
            'cbu': self.cbu,
            'pr': {
                '@context': full_context,
                'type': full_types,
                'procHash': self.proc_hash,
                'procUrl': self.proc_url,
                'data': [item.build_data() for item in self.data]
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
        params.update(exp=self.exp) if self.exp else None
        params.update(nbf=self.nbf) if self.nbf else None
        return params
