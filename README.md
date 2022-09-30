# Species

This pet project is about biological species and aims to demonstrate the use of python async libraries working together.

## Setup

```shell
pyenv virtualenv 3.8 species_38
pyenv activate species_38
pip install -r requirements-dev.txt
```
Activate pre-commit hooks:
```shell
pre-commit install
```

## Running

```shell
docker-compose up -d
python main.py 
```

Then try to open in browser: http://localhost:8080/api/v1/species
