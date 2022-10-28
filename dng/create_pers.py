from random import randint

from dng.database import Pers, Users, Place

from sqlalchemy import create_engine
from sqlalchemy.orm import Session


class GeneratorPers:

    def __init__(self, name, user_id=0):
        self.name = name
        self.user_id = user_id

        self.exp = 0

        self.con = self.roll_4d6_drop_low()
        self.dex = self.roll_4d6_drop_low()
        self.mnd = self.roll_4d6_drop_low()

        self.max_hp = 10 + ((self.con - 10) // 2)
        self.con_str = self.con_res = self.con_dmg = (self.con - 10) // 2
        self.dex_crt = self.dex_lp = self.dex_esc = self.dex_ac = (self.dex - 10) // 2
        self.mnd_mgc = self.mnd_prc = self.mnd_wll = self.mnd_trd = (self.mnd - 10) // 2

        self.gold = randint(1, 20)

        DATABASE_NAME = 'rpg.sqlite'
        engine = create_engine(f'sqlite:///{DATABASE_NAME}')
        session = Session(bind=engine)

        new = Pers(
            self.name,
            self.user_id,
            self.max_hp,
            self.con,
            self.con_str,
            self.con_res,
            self.con_dmg,
            self.dex,
            self.dex_crt,
            self.dex_ac,
            self.dex_esc,
            self.dex_lp,
            self.mnd,
            self.mnd_mgc,
            self.mnd_prc,
            self.mnd_wll,
            self.mnd_trd,
            self.gold
        )
        session.add(new)
        session.commit()

    @staticmethod
    def roll_4d6_drop_low():
        roll = [randint(1, 6) for i in range(4)]
        roll.remove(min(roll))
        return sum(roll)

    def __str__(self):
        return f'     Имя персонажа | Максимальное здоровье\n' \
               f'     {self.name:^16}{self.max_hp:^21}\n' \
               f'\n' \
               f'Cила | Урон в ближнем бою | Атлетика | Стойкость\n' \
               f'{self.con:^5}|{self.con_dmg:^20}|{self.con_str:^10}|{self.con_res:^10}\n' \
               f'\n' \
               f'Ловкость | Шанс уклонения | Шанс критической атаки | Шанс побега | Взлом замков\n' \
               f'{self.dex:^9}|{self.dex_ac:^16}|{self.dex_crt:^24}|{self.dex_esc:^13}|{self.dex_lp:^16}\n' \
               f'\n' \
               f'Разум | Шанс срабатывания магии | Внимательность | Воля | Торговля\n' \
               f'{self.mnd:^6}|{self.mnd_mgc:^25}|{self.mnd_prc:^16}|{self.mnd_wll:^6}|{self.mnd_trd:^12}\n'


a = GeneratorPers('sd')