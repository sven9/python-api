# Python API

![Lint](https://github.com/sven9/python-api/actions/workflows/lint.yml/badge.svg)
![Test](https://github.com/sven9/python-api/actions/workflows/test.yml/badge.svg)
[![Code Coverage](https://img.shields.io/codecov/c/github/sven9/python-api)](https://codecov.io/github/sven9/python-api)
![GitHub](https://img.shields.io/github/license/sven9/python-api)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

A simple [Flask](https://github.com/pallets/flask) API

## Features
* Flask API
* Dockerized environment with multi-stage builds
    * Builds for "development", "test", and "deployment"
    * Flask serving traffic for development, Gunicorn for deployment
* Quality controls
    * [pre-commit](https://github.com/pre-commit/pre-commit) configuration
    * Linting suite
    * [pytest](https://docs.pytest.org/en/stable/) tests
* [OpenAPI](https://github.com/OAI/OpenAPI-Specification) spec served from http://localhost:5000/apidocs
* GitHub Actions integration for linting, testing, and version bumping
* Structured logging including support for a correlation id per request

## Usage
### Running The Application
`make up` to serve HTTP traffic from http://localhost:5000

### Docker
* `make build` - build the application container
* `make up` - run the application
* `make shell` - open a shell inside the application container
* `make down` - shut down the application

### Tools
* `make lint` - run linting suite
* `make run-tests` - run tests and generate coverage report
* `make quality-reports` - generates code quality metric reports
* `make setup-pre-commit` - installs pre-commit hooks for Git
