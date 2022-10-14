# Species

This pet project is about biological species and aims to demonstrate the use of python async libraries working together.

## Setup

```shell
pyenv virtualenv 3.10.4 species_3104
pyenv activate species_3104
pip install -r requirements-dev.txt
```
Activate pre-commit hooks:
```shell
pre-commit install
```

## Running server

```shell
docker-compose up -d db
python main.py 
```

Then try to open in browser: http://localhost:8080/api/v1/species

## Running tests

```shell
docker-compose up -d db-test
ENV=unittest pytest
```
