from random import randint

from sqlalchemy.orm.util import identity_key

from dng.database import Chars, Users, Place, create_engine, DATABASE_NAME
from sqlalchemy.orm import Session




class GeneratorPers:

    def __init__(self, name, exp=0,  tg_id=0):
        self.name = name
        self.tg_id = tg_id

        self.exp = exp

        self.con = self.roll_4d6_drop_low()
        self.dex = self.roll_4d6_drop_low()
        self.mnd = self.roll_4d6_drop_low()

        self.gold = randint(1, 20)

        engine = create_engine(f'sqlite:///{DATABASE_NAME}')
        session = Session(bind=engine)

        new = Chars(
            self.name,
            self.tg_id,
            self.con,
            self.dex,
            self.mnd,
            self.gold
        )
        session.add(new)
        session.commit()
        session.refresh(new)
        active_pers = new.id

        user = Users(
            self.tg_id,
            active_pers
        )
        session.add(user)
        session.commit()




    @staticmethod
    def roll_4d6_drop_low():
        roll = [randint(1, 6) for _ in range(4)]
        roll.remove(min(roll))
        return sum(roll)
