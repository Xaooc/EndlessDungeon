from sqlalchemy import create_engine, Table, MetaData
from sqlalchemy.orm import mapper

DATABASE_NAME = 'rpg.sqlite'

engine = create_engine(f'sqlite:///{DATABASE_NAME}')
conn = engine.connect()

meta = MetaData(engine)
chars = Table('characters', meta, autoload=True)
users = Table('users', meta, autoload=True)


class Chars:
    def __init__(self, name: str, tg_id: int, con: int, dex: int, mnd: int,
                 gold: int, hp: int = 0, place: int = 0, items: str = '', is_dead: bool = False):
        self.tg_id = tg_id
        self.hp = hp
        self.is_dead = is_dead
        self.items = items
        self.gold = gold
        self.place = place
        self.mnd = mnd
        self.dex = dex
        self.con = con
        self.name = name


class Place:
    def __init__(self, name: str, desc: str, event: str):
        self.name = name
        self.desc = desc
        self.event = event


class Users:
    def __init__(self, tg_id: int, active_pers: int = 0):
        self.tg_id = tg_id
        self.active_pers = active_pers


mapper(Users, users)
mapper(Chars, chars)
