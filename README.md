# alastria-identity-lib-py

Python version of the Alastria Identity lib

# Testing

Execute tests
```bash
docker-compose run --rm identity poetry run python -m coverage run -m pytest alastria_identity -v .
```

Create and check test coverage
```bash
docker-compose run --rm identity poetry run coverage html
npx http-server (or any local http server)
```

Open `http://localhost:8080` in your browser

# TODO

- This README
- Add more code examples
- Create the PyPI package and push it to pypi.org
- Test the connection with the identity Alastria network node
- Delegate calls is still a WIP, we need to finish that
