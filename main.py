import asyncio

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from tkn import API_TOKEN
from Dialogs import new_char

bot = Bot(token=API_TOKEN)
dp = Dispatcher(storage=MemoryStorage())


async def main():
    dp.include_router(new_char.router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
