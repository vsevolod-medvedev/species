import asyncio
import peewee_async

from app.database import database
from app.models import Species


def start():
    # Look, sync code is working!
    Species.create_table(True)
    Species.create(text="Yo, I can do it sync!")
    database.close()

    # Create async models manager:
    objects = peewee_async.Manager(database)

    # No need for sync anymore!
    database.set_allow_sync(False)


    async def handler():
        await objects.create(Species, text="Not bad. Watch this, I'm async!")
        all_objects = await objects.execute(Species.select())
        for obj in all_objects:
            print(obj.text)

    loop = asyncio.get_event_loop()
    loop.run_until_complete(handler())
    loop.close()

    # Clean up, can do it sync again:
    with objects.allow_sync():
        Species.drop_table(True)

    # Expected output:
    # Yo, I can do it sync!
    # Not bad. Watch this, I'm async!
