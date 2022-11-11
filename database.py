from sqlalchemy import create_engine, Table, MetaData
from sqlalchemy.orm import mapper, Session

DATABASE_NAME = 'rpg.sqlite'

engine = create_engine(f'sqlite:///{DATABASE_NAME}')
meta = MetaData(engine)

chars = Table('characters', meta, autoload=True)
users = Table('users', meta, autoload=True)
session = Session(bind=engine)


# инициализируем классы таблиц
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


class Users:
    def __init__(self, tg_id: int, id_char: int, status: int = 0):
        self.status = status
        self.tg_id = tg_id
        self.id_char = id_char


# мапим их с таблицей бд
mapper(Users, users)
mapper(Chars, chars)


###

class UserData:
    def __init__(self, tg_id: int):
        self.max_hp = 0
        self.tg_id = tg_id
        self.id_char = 0
        self.name = ''
        self.con = 0
        self.dex = 0
        self.mnd = 0
        self.gold = 0

    def is_user_created(self) -> bool:
        """
        Проверка наличия юзера в бд
        """
        return session.query(Users).where(Users.tg_id == self.tg_id).scalar()

    async def user_char_upd(self) -> None:
        """
        Обновление активного персонажа у юзера
        """
        user = session.query(Users).where(Users.tg_id == self.tg_id).one()
        user.id_char = self.id_char
        session.add(user)
        session.commit()

    async def create_char(self) -> None:
        """
        Создание нового персонажа и запись его юзеру
        """
        user = Users(self.tg_id, self.id_char)
        if not self.is_user_created():
            session.add(user)
        else:
            await self.user_char_upd()
        session.commit()

    def is_user_inactive_char(self) -> bool:
        """
        Проверка есть ли у юзера активный персонаж
        """
        return session.query(Users).where(Users.tg_id == self.tg_id).where(Users.id_char == 0).scalar()

    async def new_char(self, name: str, con: int, dex: int, mnd: int, gold: int) -> None:
        """
        Создание и запись нового персонажа в бд
        """
        self.name = name
        self.con = con
        self.dex = dex
        self.mnd = mnd
        self.gold = gold
        self.max_hp = 10 + (self.con - 10) // 2

        new = Chars(self.name, self.tg_id, self.con, self.dex, self.mnd, self.gold, hp=self.max_hp)
        session.add(new)
        session.commit()
        session.refresh(new)
        self.id_char = new.id

    async def get_char_name(self) -> dict:
        """
        Получить характеристики персонажа из бд
        """
        user = session.query(Users).where(Users.tg_id == self.tg_id).one()
        self.id_char = user.id_char
        char = session.get(Chars, self.id_char)
        return {'name': char.name, 'con': char.con, 'dex': char.dex, 'mnd': char.mnd, 'gold': char.gold}

    async def gold_mod(self, gold: int) -> None:
        """
        Изменение кол-ва золота
        """
        user = session.query(Users).where(Users.tg_id == self.tg_id).one()
        self.id_char = user.id_char
        char = session.get(Chars, self.id_char)
        char.gold += gold if (char.gold + gold) >= 0 else 0
        session.add(char)
        session.commit()

    async def hp_mod(self, hp: int) -> None:
        """
        Изменение кол-ва здоровья
        """
        user = session.query(Users).where(Users.tg_id == self.tg_id).one()
        self.id_char = user.id_char
        char = session.get(Chars, self.id_char)
        char.hp += hp if (char.hp + hp) >= 0 else 0
        if char.hp == 0:
            pass
        if char.hp > self.max_hp:
            char.hp = self.max_hp
        session.add(char)
        session.commit()

    async def update_stats(self, status: int) -> None:
        """
        Обновление статуса пользователя. Нужно для защиты от повторного вызова команды
        """
        user = session.query(Users).where(Users.tg_id == self.tg_id).one()
        user.status = status
        session.add(user)
        session.commit()

    async def get_user_status(self) -> int:
        """
        Получить статус пользователя
        """
        user = session.query(Users).where(Users.tg_id == self.tg_id).one()
        return user.status
