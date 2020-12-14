from dataclasses import dataclass


@dataclass
class Entity:
    did_entity: str = ''
    name: str = ''
    cif: str = ''
    url_logo: str = ''
    url_create_aid: str = ''
    url_aoa: str = ''
    status: int = 0
