from typing import List
import re

import requests

from .parsers import ContractParser


class IdentityConfigBuilder:
    def __init__(self, contracts_info_url: str, parser_class: ContractParser):
        self.parser_class = parser_class
        self.contracts_info_url = contracts_info_url

    def get_contracts(self) -> List[str]:
        contracts_raw_response = requests.get(self.contracts_info_url)
        contracts = map(
            lambda contract_line: contract_line.split('|')[-2].strip(),
            contracts_raw_response.content.decode('utf-8').split('\n')[2:-1]
        )
        return list(contracts)

    def generate(self):
        config = {}
        contracts = self.get_contracts()

        for contract_url in contracts:
            name = re.search(
                r'sol_(?P<name>.*)\.abi',
                contract_url
            ).group('name')
            config[name] = self.parser_class(contract_url).parse()

        return config
