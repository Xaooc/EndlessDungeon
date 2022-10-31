from aiogram import Bot, Dispatcher, executor, types
from dng.tkn import API_TOKEN
from dng.create_pers import GeneratorPers
import dng.database as db
from sqlalchemy.orm import Session

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

engine = db.create_engine(f'sqlite:///{db.DATABASE_NAME}')
session = Session(bind=engine)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    tg_id = message.from_user.id
    await message.answer("Введите имя персонажа.")

    @dp.message_handler()
    async def new_char(message: types.Message):
        name = message.text
        print(message.from_user.id)
        new = GeneratorPers(name, tg_id=tg_id)
        await message.reply(f"Персонаж {name} создан!")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)

