from aiogram import Bot, Dispatcher, executor, types
from sqlalchemy import exists

from dng.tkn import API_TOKEN
from dng.create_pers import GeneratorPers, Session
import dng.database as db


bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

engine = db.create_engine(f'sqlite:///{db.DATABASE_NAME}')
session = Session(bind=engine)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    tg_id = message.from_user.id
    if not session.query(exists().where(db.Users.tg_id == tg_id)).scalar() or \
            session.query(exists().where(db.Users.tg_id == tg_id)).where(db.Users.active_pers == 0).scalar():
        await message.answer("Введите имя персонажа.")

        @dp.message_handler()
        async def new_char(message: types.Message):
            name = message.text
            new = GeneratorPers(name, tg_id=tg_id)
            await message.reply(f"Персонаж {name} создан!")
    else:
        await message.answer("У вас есть персонаж!")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)

