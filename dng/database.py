from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship


DATABASE_NAME = 'rpg.sqlite'

engine = create_engine(f'sqlite:///{DATABASE_NAME}')
Session = sessionmaker(bind=engine)

Base = declarative_base()

def create_db():
    Base.metadata.create_all(engine)


class Pers(Base):

    __tablename__ = "pers"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    user_id = Column(Integer)
    max_hp = Column(Integer)
    con = Column(Integer)
    con_str = Column(Integer)
    con_res = Column(Integer)
    con_dmg = Column(Integer)
    dex = Column(Integer)
    dex_crt = Column(Integer)
    dex_ac = Column(Integer)
    dex_esc = Column(Integer)
    dex_lp = Column(Integer)
    mnd = Column(Integer)
    mnd_mgc = Column(Integer)
    mnd_prc = Column(Integer)
    mnd_wll = Column(Integer)
    mnd_trd = Column(Integer)
    gold = Column(Integer)
    place = Column(Integer)
    items = Column(String)
    is_dead = Column(Boolean)

    def __init__(self, name: str, user_id: int,
                 max_hp: int, con: int, con_str: int, con_res: int, con_dmg: int,
                 dex: int, dex_crt: int, dex_ac: int, dex_esc: int, dex_lp: int,
                 mnd: int, mnd_mgc: int, mnd_prc: int, mnd_wll: int, mnd_trd: int,
                 gold: int, place: int = 0, items: str = '', is_dead: bool = False):
        self.user_id = user_id
        self.max_hp = max_hp
        self.is_dead = is_dead
        self.items = items
        self.gold = gold
        self.place = place
        self.mnd_trd = mnd_trd
        self.mnd_wll = mnd_wll
        self.mnd_prc = mnd_prc
        self.mnd = mnd
        self.mnd_mgc = mnd_mgc
        self.dex_lp = dex_lp
        self.dex_esc = dex_esc
        self.dex_ac = dex_ac
        self.dex_crt = dex_crt
        self.dex = dex
        self.con_dmg = con_dmg
        self.con_res = con_res
        self.con_str = con_str
        self.con = con
        self.name = name


class Place(Base):

    __tablename__ = "place"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    desc = Column(String)
    ivent = Column(String)


class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    tg_id = Column(Integer)
    active_pers = Column(Integer)
