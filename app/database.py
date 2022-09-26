import peewee_async

from app import config

database = peewee_async.PostgresqlDatabase('species')


def init_database(db: peewee_async.PostgresqlDatabase):
    db.init(
        host=config.DB_HOST,
        port=config.DB_PORT,
        database=config.DB_NAME,
        user=config.DB_USER,
        password=config.DB_PASS,
    )
