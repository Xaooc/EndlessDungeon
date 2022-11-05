import asyncio

from aiogram import Bot, Dispatcher, Router
from aiogram.filters import Command
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import Message
from aiogram_dialog import DialogRegistry


from dng.tkn import API_TOKEN
from dng.create_pers import GeneratorPers


bot = Bot(token=API_TOKEN)
dp = Dispatcher(storage=MemoryStorage())
registry = DialogRegistry(dp)
router = Router()


@dp.message(Command(commands=["start"]))
async def send_welcome(message: Message):
    tg_id = message.from_user.id
    new = GeneratorPers(str(tg_id), tg_id)
    await new.new()


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
