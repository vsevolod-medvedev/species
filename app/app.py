from app.database import database
from app.models import Species, Genus


def init_data():
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
