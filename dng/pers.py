from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from dng.database import Base

class Pers(Base):
    __tablename__ = "pers"

    id = Column(Integer, primary_key=True)
    name = Column(String)
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
    place = Column(Integer, ForeignKey("place.id"))
    gold = Column(Integer)
    items = Column(String)
    is_dead = Column(Boolean)

    users = relationship('Users')

    def __init__(self, name: str, con: int, con_str: int, con_res: int, con_dmg: int,
                 dex: int, dex_crt: int, dex_ac: int, dex_esc: int, dex_lp: int,
                 mnd: int, mnd_mgc: int, mnd_prc: int, mnd_wll: int, mnd_trd: int,
                 gold: int, place: int = 0, items: str = '', is_dead: bool = False):
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
