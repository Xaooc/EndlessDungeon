from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship


DATABASE_NAME = 'rpg.sqlite'

engine = create_engine(f'sqlite:///{DATABASE_NAME}')
Session = sessionmaker(bind=engine)

Base = declarative_base()


def create_db():
    Base.metadata.create_all(engine)
    Session()


class Pers(Base):
    __tablename__ = "pers"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"))
    hp = Column(Integer)
    con = Column(Integer)
    dex = Column(Integer)
    mnd = Column(Integer)
    gold = Column(Integer)
    place = Column(Integer, ForeignKey("place.id"))
    items = Column(String)
    is_dead = Column(Boolean)

    def __init__(self, name: str, user_id: int, con: int, dex: int, mnd: int,
                 gold: int, hp: int = 0, place: int = 0, items: str = '', is_dead: bool = False):
        self.user_id = user_id
        self.hp = hp
        self.is_dead = is_dead
        self.items = items
        self.gold = gold
        self.place = place
        self.mnd = mnd
        self.dex = dex
        self.con = con
        self.name = name


class Place(Base):

    __tablename__ = "place"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    desc = Column(String)
    ivent = Column(String)

    def __init__(self, name: str, desc: str, ivent: str):
        self.name = name
        self.desc = desc
        self.ivent = ivent


class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    tg_id = Column(Integer)
    active_pers = Column(Integer, ForeignKey("pers.id"))

    def __init__(self, tg_id: int, active_pers: int = 0):
        self.tg_id = tg_id
        self.active_pers = active_pers
