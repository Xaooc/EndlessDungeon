from sqlalchemy import create_engine, Table, MetaData
from sqlalchemy.orm import mapper, Session

DATABASE_NAME = 'rpg.sqlite'

engine = create_engine(f'sqlite:///{DATABASE_NAME}')
meta = MetaData(engine)

chars = Table('characters', meta, autoload=True)
users = Table('users', meta, autoload=True)
session = Session(bind=engine)


class Chars:
    def __init__(self, name: str, tg_id: int, con: int, dex: int, mnd: int,
                 gold: int, hp: int = 0, lvl: int = 0, place: int = 0, is_dead: bool = False):
        self.tg_id = tg_id
        self.name = name
        self.hp = hp
        self.lvl = lvl
        self.con = con
        self.dex = dex
        self.mnd = mnd
        self.gold = gold
        self.place = place
        self.is_dead = is_dead


class Place:
    def __init__(self, name: str, desc: str, event: str):
        self.name = name
        self.desc = desc
        self.event = event


class Users:
    def __init__(self, tg_id: int, id_char: int):
        self.tg_id = tg_id
        self.id_char = id_char


mapper(Users, users)
mapper(Chars, chars)


class UserData:
    def __init__(self, tg_id: int):
        self.tg_id = tg_id
        self.id_char = 0
        self.name = ''
        self.con = 0
        self.dex = 0
        self.mnd = 0
        self.gold = 0

    def is_user_created(self) -> bool:
        return session.query(Users).where(Users.tg_id == self.tg_id).scalar()

    def user_char_upd(self):
        user = session.query(Users).where(Users.tg_id == self.tg_id).one()
        user.id_char = self.id_char
        session.add(user)
        session.commit()

    async def create_char(self):
        user = Users(self.tg_id, self.id_char)
        if not self.is_user_created():
            session.add(user)
        else:
            self.user_char_upd()
        session.commit()

    def is_user_active_char(self) -> bool:
        return session.query(Users).where(Users.tg_id == self.tg_id).where(Users.id_char == 0).scalar()

    async def new_char(self, name: str, con: int, dex: int, mnd: int, gold: int):
        self.name = name
        self.con = con
        self.dex = dex
        self.mnd = mnd
        self.gold = gold

        new = Chars(self.name, self.tg_id, self.con, self.dex, self.mnd, self.gold)
        session.add(new)
        session.commit()
        session.refresh(new)
        self.id_char = new.id
