import asyncio
from datetime import datetime

from aiogram import Bot, Dispatcher, BaseMiddleware
from aiogram.fsm.storage.memory import MemoryStorage

import logging

from database import UserData
from tkn import API_TOKEN
from Dialogs import new_char, info, char, start, go, group

logging.basicConfig(level=logging.INFO, filename="mylog.log",
                    format="%(asctime)s - %(levelname)s - %(funcName)s: %(lineno)d - %(message)s")


class Log(BaseMiddleware):
    async def __call__(self,  handler, event, data):
        log = f'Пользователь {event.from_user.username} написал {event.text}. В чате {event.chat.title}'
        tid = float(str(event.chat.id) + '.' + str(event.from_user.id))
        user = UserData(tg_id=tid)
        if not user.is_user_created():
            await user.create_char()
        if not user.is_user_inactive_char():
            char = await user.get_char()
            if str(datetime.date(datetime.today())) != char.get('res_hp'):
                await user.hp_mod(100000)
        print(log)
        result = await handler(event, data)
        return result


bot = Bot(token=API_TOKEN)
dp = Dispatcher(storage=MemoryStorage())


async def main():
    #подключаем созданные роутеры
    dp.message.middleware(Log())
    dp.include_router(start.router)
    dp.include_router(new_char.router)
    dp.include_router(char.router)
    dp.include_router(info.router)
    dp.include_router(go.router)
    dp.include_router(group.router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
