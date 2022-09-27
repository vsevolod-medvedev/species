import logging.config

APP_HOST = 'localhost'
APP_PORT = 8080

DB_HOST = 'localhost'
DB_PORT = 5432
DB_NAME = 'species'
DB_USER = 'species_admin'
DB_PASS = 'species_admin'

LOG_LEVEL = 'INFO'

LOG_CONFIG = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'default': {
            'format': '{asctime} {levelname}:{name} - {message}',
            'style': '{'
        },
    },
    'handlers': {
        'default': {
            'class': 'logging.StreamHandler',
            'formatter': 'default',
            'stream': 'ext://sys.stdout'
        },
    },
    'loggers': {
        '': {
            'level': locals().get('LOG_LEVEL'),
            'handlers': ['default'],
        }
    }
}

logging.config.dictConfig(LOG_CONFIG)

logging.info(f'Configured with LOG_LEVEL={LOG_LEVEL}')
