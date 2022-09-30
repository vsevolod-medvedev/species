from yoyo import step

from app.db.__init__ import database
from app.models import Species, Genus

__depends__ = {}


def init_data(connection):
    Species.drop_table()
    Genus.drop_table()

    database.create_tables([
        Genus,
        Species,
    ])

    genus = Genus.create(caption='Снегири')
    Species.create(caption='Снегирь', genus=genus)

    genus = Genus.create(caption='Настоящие дрозды')
    Species.create(caption='Певчий дрозд', genus=genus)


steps = [
    step(init_data)
]
