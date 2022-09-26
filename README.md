# Species

## Setup

```shell
pyenv virtualenv 3.8 species_38
pyenv activate species_38
pip install -r requirements-dev.txt
```

## Running

```shell
docker-compose up -d
python main.py 
```

Then try to open in browser: http://localhost:8080/api/v1/species
