# alastria-identity-lib-py

Python version of the Alastria Identity lib

# Installing

```bash
pip install alastria-identity
```

or you could use Poetry

```bash
poetry add alastria-identity
```

# Testing

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

# TODO

- This README
- Add more code examples
- ~Create the PyPI package and push it to pypi.org~
- Test the connection with the identity Alastria network node
- Delegate calls is still a WIP, we need to finish that
