import json

import requests


class ContractParser:
    def __init__(self, contract_url):
        self.contract_url = contract_url

    def parse(self):
        contract_response = self.get_json_data_from_url()
        return self.extract_data_from_content(
            contract_response.content)

    def extract_data_from_content(self, content):
        contract_content = json.loads(content.decode('utf-8'))

        return {
            self.get_name_in_content(item): item
            for item in contract_content
            if 'name' in item or 'type' in item
        }

    def get_name_in_content(self, content):
        name = content.get('name', None)

        if content.get('type', None) == 'constructor':
            name = 'constructor'

        return name

    def get_json_data_from_url(self):
        contract_url = self.contract_url.replace(
            'https://github.com/',
            'https://raw.githubusercontent.com/'
        ).replace(
            'blob/',
            ''
        )
        contract_response = requests.get(contract_url)
        contract_response.raise_for_status()

        return contract_response
