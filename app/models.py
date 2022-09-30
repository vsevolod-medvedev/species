import peewee

from app.db import database


class BaseModel(peewee.Model):
    class Meta:
        database = database


class Genus(BaseModel):
    caption = peewee.CharField()


class Species(BaseModel):
    genus = peewee.ForeignKeyField(Genus)
    caption = peewee.CharField()
