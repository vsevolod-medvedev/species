import asyncio
import peewee_async

from app.database import database, init_database
from app.models import Species, Genus


def start():
    init_database(database)

    # Look, sync code is working!
    Genus.create_table()
    genus = Genus.create(caption='Снегири')
    Species.create_table()
    Species.create(caption='Снегирь', genus=genus)
    database.close()

    # Create async models manager:
    objects = peewee_async.Manager(database)

    # No need for sync anymore!
    database.set_allow_sync(False)

    async def handler():
        genus = await objects.create(Genus, caption='Настоящие дрозды')
        await objects.create(Species, caption='Певчий дрозд', genus=genus)
        all_objects = await objects.execute(Species.select(Species, Genus).join(Genus))
        for obj in all_objects:
            print(f'{obj.caption} ({obj.genus.caption})')

    loop = asyncio.get_event_loop()
    loop.run_until_complete(handler())
    loop.close()

    # Clean up, can do it sync again:
    with objects.allow_sync():
        Species.drop_table()
        Genus.drop_table()
