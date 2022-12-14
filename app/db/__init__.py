import pathlib

import peewee_async
import yoyo
from yoyo.migrations import MigrationList

from app import config

database = peewee_async.PostgresqlDatabase(config.DB_NAME)
manager = peewee_async.Manager(database)


DATA_MIGRATIONS = (
    '002_populate_test_data',
)


def init_database(skip_data_migrations: bool = False) -> peewee_async.PostgresqlDatabase:
    database.init(
        host=config.DB_HOST,
        port=config.DB_PORT,
        database=config.DB_NAME,
        user=config.DB_USER,
        password=config.DB_PASS,
    )
    apply_migrations(skip_data_migrations)
    database.set_allow_sync(False)
    return database


def apply_migrations(skip_data_migrations: bool) -> None:
    db_uri = f'postgres://{config.DB_USER}:{config.DB_PASS}@{config.DB_HOST}:{config.DB_PORT}/{config.DB_NAME}'
    backend = yoyo.get_backend(uri=db_uri)
    path = (pathlib.Path(__file__).parent / 'migrations').as_posix()
    migrations = yoyo.read_migrations(path)
    if not migrations:
        raise RuntimeError('Migrations not found!')
    if skip_data_migrations:
        migrations = MigrationList(
            items=(m for m in migrations if m.id not in DATA_MIGRATIONS),
            post_apply=migrations.post_apply,
        )
    with backend.lock():
        backend.apply_migrations(backend.to_apply(migrations))
