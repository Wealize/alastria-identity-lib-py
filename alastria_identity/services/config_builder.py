from typing import List
import re
from collections import defaultdict

import requests

from .parsers import ContractParser
from alastria_identity.types import ConfigParser


class IdentityConfigBuilder:
    CONTRACT_NAME_REGEX = r'sol_(?P<name>.*)\.abi'
    CONTRACT_URL_POSITION = -2
    ADDRESS_POSITION = -3

    def __init__(self, contracts_info_url: str, parser_class: ConfigParser):
        self.parser_class = parser_class
        self.contracts_info_url = contracts_info_url

    def generate(self):
        '''
            We will output a config with two keys:
            - Functions are the ones interesting for generating transactions
            - Addresses will be used to point to the right contract also using
              its name
        '''
        config = defaultdict(dict)
        contracts = self.get_contracts()

        for contract_item in contracts:
            name = re.search(
                self.CONTRACT_NAME_REGEX,
                contract_item['url']
            ).group('name')

            config[name]['functions'] = self.parser_class(contract_item['url']).parse()
            config[name]['address'] = contract_item['address']

        return config

    def get_contracts(self) -> List[str]:
        contracts_raw_response = requests.get(self.contracts_info_url)
        return list(self.extract_contract_item_from_response(
            contracts_raw_response.content.decode('utf-8')))

    def extract_contract_item_from_response(
        self, contracts_content: str
    ) -> List[dict]:
        return map(
            lambda contract_line: {
                'url': contract_line.split('|')[self.CONTRACT_URL_POSITION].strip(),
                'address': contract_line.split('|')[self.ADDRESS_POSITION].strip()
            },
            contracts_content.split('\n')[2:-1]
        )
