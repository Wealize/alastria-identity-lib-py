from typing import List
import re

import requests

from .parsers import ContractParser


class IdentityConfigBuilder:
    CONTRACT_NAME_REGEX = r'sol_(?P<name>.*)\.abi'
    CONTRACT_URL_POSITION = -2

    def __init__(self, contracts_info_url: str, parser_class: ContractParser):
        self.parser_class = parser_class
        self.contracts_info_url = contracts_info_url

    def get_contracts(self) -> List[str]:
        contracts_raw_response = requests.get(self.contracts_info_url)
        return list(self.extract_urls_from_response(
            contracts_raw_response.content.decode('utf-8')))

    def extract_urls_from_response(
        self, contracts_content: List[dict]
    ) -> List[str]:
        return map(
            lambda contract_line: contract_line.split('|')[self.CONTRACT_URL_POSITION].strip(),
            contracts_content.split('\n')[2:-1]
        )

    def generate(self):
        config = {}
        contracts = self.get_contracts()

        for contract_url in contracts:
            name = re.search(
                self.CONTRACT_NAME_REGEX,
                contract_url
            ).group('name')
            config[name] = self.parser_class(contract_url).parse()

        return config
