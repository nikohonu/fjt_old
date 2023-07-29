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


class Anime(BaseModel):
    id = AutoField()
    date_time = DateTimeField(default=dt.datetime.utcnow())
    title = TextField()
    start = IntegerField()
    end = IntegerField()
    duration = FloatField()

    @property
    def episodes(self):
        return self.end - self.start + 1

    @property
    def amount(self):
        return (self.duration / 21) * self.episodes

    @property
    def points(self):
        return self.amount * 9.5

    def log(self):
        print(
            f".log anime {normalize_number(self.amount)} {self.title} {f'EP {self.end}' if self.episodes == 1 else f'EPS {self.start}-{self.end}'}"
        )


class Manga(BaseModel):
    id = AutoField()
    date_time = DateTimeField(default=dt.datetime.utcnow())
    title = TextField()
    start = IntegerField()
    end = IntegerField()
    volume = FloatField()
    chapter = FloatField()
    amount = IntegerField()

    @property
    def points(self):
        return self.amount * 0.2

    def log(self):
        print(
            f".log manga {normalize_number(self.amount)} {self.title} VOL {normalize_number(self.chapter)} CH {normalize_number(self.chapter)}"
        )


class Book(BaseModel):
    id = AutoField()
    date_time = DateTimeField(default=dt.datetime.utcnow())
    title = TextField()
    start = IntegerField()
    end = IntegerField()
    volume = FloatField()
    chapter = FloatField()
    amount = IntegerField()

    @property
    def points(self):
        return self.amount * 1

    def log(self):
        print(
            f".log book {normalize_number(self.amount)} {self.title} VOL {normalize_number(self.chapter)} CH {normalize_number(self.chapter)}"
        )


class Readtime(BaseModel):
    id = AutoField()
    date_time = DateTimeField(default=dt.datetime.utcnow())
    title = TextField()
    start = IntegerField()
    end = IntegerField()
    volume = FloatField()
    chapter = FloatField()
    amount = IntegerField()

    @property
    def points(self):
        return self.amount * 0.45

    def log(self):
        print(
            f".log readtime {normalize_number(self.amount)} {self.title} VOL {normalize_number(self.chapter)} CH {normalize_number(self.chapter)}"
        )


class VN(BaseModel):
    id = AutoField()
    date_time = DateTimeField(default=dt.datetime.utcnow())
    title = TextField()
    amount = IntegerField()

    @property
    def points(self):
        return self.amount / 350

    def log(self):
        print(f".log vn {normalize_number(self.amount)} {self.title}")


class Reading(BaseModel):
    id = AutoField()
    date_time = DateTimeField(default=dt.datetime.utcnow())
    title = TextField()
    amount = IntegerField()

    @property
    def points(self):
        return self.amount / 350

    def log(self):
        print(f".log vn {normalize_number(self.amount)} {self.title}")


class Listening(BaseModel):
    id = AutoField()
    date_time = DateTimeField(default=dt.datetime.utcnow())
    url = TextField()
    title = TextField()
    duration = FloatField()

    @property
    def amount(self):
        return self.duration

    @property
    def points(self):
        return self.amount * 0.45

    def log(self):
        print(
            f".log listening {normalize_number(self.amount)} {self.url if self.url else self.title}"
        )


models = BaseModel.__subclasses__()
database.create_tables(models)
