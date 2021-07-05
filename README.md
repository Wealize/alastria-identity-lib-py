# alastria-identity-lib-py

Python version of the Alastria Identity lib

## Installing

```bash
pip install alastria-identity
```

or you could use Poetry

```bash
poetry add alastria-identity
```

## Testing

Execute tests

```bash
docker-compose run --rm identity poetry run python -m coverage run -m pytest alastria_identity -v .
```

Create and check test coverage

```bash
docker-compose run --rm identity poetry run coverage html
python -m http.server 8000
```

Open `http://localhost:8000` in your browser

## How to use the library

You can check [the examples in this folder, we'll continue updating the documentation](https://github.com/Wealize/alastria-identity-lib-py/tree/main/alastria_identity/examples).

## Some gooodies

You can check in different files utilities that might be useful to you.

- **Types**: We use these dataclasses so it's easier to interact with the library, feel free to [use them to make it easier on yourself](https://github.com/Wealize/alastria-identity-lib-py/tree/main/alastria_identity/types). :-)
- **JWT tokens handling**: [This service](https://github.com/Wealize/alastria-identity-lib-py/blob/main/alastria_identity/services/tokens.py) makes encoding decoding jwt tokens easier.
- **Config builder**: [The config builder](https://github.com/Wealize/alastria-identity-lib-py/blob/main/alastria_identity/services/config_builder.py) receives an url and a parser class and parses the configuration so It can be read by the transaction service. You can check [the test to see how this structure ends up](https://github.com/Wealize/alastria-identity-lib-py/blob/main/alastria_identity/tests/test_parsers.py).
- **Transaction service**: [The service in charge of building a transaction](https://github.com/Wealize/alastria-identity-lib-py/tree/main/alastria_identity/services/transaction_service.py) and "talking" to the smart contract, it receives a configuration to know which parameters can use and what's available.

## Glossary

- **Provider node url**: It's the url (with `/rpc` endpoint) of the node you want to connect in which the library can interact with the Alastria identity
  smart contracts.
- **Contracts info**: It's the file Alastria members created to be loaded to the identity libraries. You can't change it using the javascript library but you can set it in this one. We generate the configuration the Transaction service uses on the fly.
- **Contract names**: The contract names you need to use the library, in this case you can check the Alastria examples in the [ContractsInfo file]( 'https://raw.githubusercontent.com/alastria/alastria-identity/master/contracts/ContractInfo.md')
- **Contract addresses**: As the one above It's self-explanatory, the address of the smart contract deployed you want to use.

## TODO

- ~This README~
- ~Add more code examples~ [You can check them here](https://github.com/Wealize/alastria-identity-lib-py/tree/main/alastria_identity/examples)
- ~Create the PyPI package and push it to pypi.org~
- Test the connection with the identity Alastria network node
- ~Delegate calls is still a WIP, we need to finish that~

## Contributors

Started with :heart: by the [Wealize Team](https://github.com/Wealize/alastria-identity-lib-py/graphs/contributors).
