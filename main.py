import asyncio

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from tkn import API_TOKEN
from Dialogs import new_char, info, char, start, go

bot = Bot(token=API_TOKEN)
dp = Dispatcher(storage=MemoryStorage())


async def main():
    #подключаем созданные роутеры
    dp.include_router(start.router)
    dp.include_router(new_char.router)
    dp.include_router(char.router)
    dp.include_router(info.router)
    dp.include_router(go.router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
