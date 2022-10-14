import peewee

from app.db import database


class BaseModel(peewee.Model):
    class Meta:
        database = database


class Genus(BaseModel):
    """
    Биологический род
    """
    caption = peewee.CharField()


class Species(BaseModel):
    """
    Биологический вид
    """
    genus = peewee.ForeignKeyField(Genus)
    caption = peewee.CharField()


class Observation(BaseModel):
    """
    Наблюдение
    """
    species = peewee.ForeignKeyField(Species)
    timestamp = peewee.DateTimeField()
    latitude = peewee.FloatField()
    longitude = peewee.FloatField()
    # TODO: photos, description, tags
