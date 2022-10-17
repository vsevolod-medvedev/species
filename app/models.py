import peewee
from playhouse.shortcuts import model_to_dict

from app.db import database


class BaseModel(peewee.Model):
    class Meta:
        database = database

    def to_dict(self):
        return model_to_dict(self, recurse=False)


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
