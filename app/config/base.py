import logging.config

APP_HOST = 'localhost'
APP_PORT = 8080

DB_HOST = 'localhost'
DB_PORT = 5432
DB_NAME = 'species_db'
DB_USER = 'species_admin'
DB_PASS = 'species_admin'

LOG_LEVEL = 'INFO'

logging.basicConfig(
    format='%(asctime)s %(levelname)s:%(name)s - %(message)s',
    level=logging.INFO,
)

logging.info(f'Configured with LOG_LEVEL={LOG_LEVEL}')
