from alastria_identity.services import TokenService
from alastria_identity.types import NetworkDid


def test_create_did_with_network_did():
    expected_did = 'did:ala:789:012:345'
    network_did = NetworkDid.from_did('123:456:789:012:345')
    service = TokenService(secret='secret', algorithm='HS256K')

    did = service.create_did(network_did)

    assert did == expected_did
