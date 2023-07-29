import datetime as dt
from pathlib import Path

from appdirs import user_config_dir, user_data_dir
from peewee import (AutoField, BooleanField, CompositeKey, DateField,
                    DateTimeField, FloatField, ForeignKeyField, IntegerField,
                    Model, SqliteDatabase, TextField)

database_path = Path(user_data_dir("fjt", "nikohonu")) / "database.db"
database_path.parent.mkdir(parents=True, exist_ok=True)
database = SqliteDatabase(database_path, pragmas={"foreign_keys": 1})


def normalize_number(number):
    number = str(round(number * 100) / 100)
    try:
        float_number = float(number)
        if float_number.is_integer():
            return int(float_number)
        else:
            return float_number
    except ValueError:
        return number


class BaseModel(Model):
    class Meta:
        database = database


class MediaType(BaseModel):
    id = AutoField()
    name = TextField()
    last_usage = DateTimeField()
    usage_count = IntegerField(default=0)
    points = FloatField()
    amount_text = TextField()


class Media(BaseModel):
    id = AutoField()
    name = TextField()
    last_usage = DateTimeField(default=dt.datetime.utcnow())
    media_type = ForeignKeyField(MediaType)
    last_amount = IntegerField(default=1)
    last_additional_info = TextField(default="")

    class Meta:
        indexes = ((("name", "media_type"), True),)


models = BaseModel.__subclasses__()
database.create_tables(models)
