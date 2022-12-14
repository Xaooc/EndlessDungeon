from random import randint
from datetime import datetime

from database import UserData


class GeneratorPers:
    def __init__(self, name: str, tg_id: int):
        self.name = name
        self.tg_id = tg_id
        self.con = self.roll_4d6_drop_low()
        self.dex = self.roll_4d6_drop_low()
        self.mnd = self.roll_4d6_drop_low()
        self.gold = randint(1, 20)

    async def new(self):
        new = UserData(tg_id=self.tg_id)
        date = str(datetime.date(datetime.today()))
        await new.new_char(name=self.name, con=self.con, dex=self.dex, mnd=self.mnd, gold=self.gold, date=date)
        await new.create_char()

    @staticmethod
    def roll_4d6_drop_low() -> int:
        roll = [randint(1, 6) for _ in range(4)]
        roll.remove(min(roll))
        return sum(roll)

