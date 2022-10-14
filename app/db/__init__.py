import pathlib

import peewee_async
import yoyo

from app import config

database = peewee_async.PostgresqlDatabase(config.DB_NAME)
manager = peewee_async.Manager(database)


def init_database() -> peewee_async.PostgresqlDatabase:
    database.init(
        host=config.DB_HOST,
        port=config.DB_PORT,
        database=config.DB_NAME,
        user=config.DB_USER,
        password=config.DB_PASS,
    )
    apply_migrations()
    database.set_allow_sync(False)
    return database


def apply_migrations() -> None:
    db_uri = f'postgres://{config.DB_USER}:{config.DB_PASS}@{config.DB_HOST}:{config.DB_PORT}/{config.DB_NAME}'
    backend = yoyo.get_backend(uri=db_uri)
    path = (pathlib.Path(__file__).parent / 'migrations').as_posix()
    migrations = yoyo.read_migrations(path)
    if not migrations:
        raise RuntimeError('Migrations not found!')
    with backend.lock():
        backend.apply_migrations(backend.to_apply(migrations))
