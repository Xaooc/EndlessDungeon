from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram.filters import Command
from aiogram import Router

from database import UserData

router = Router()


@router.message(Command("start"))
async def start(message: Message, state: FSMContext):
    user = UserData(tg_id=message.from_user.id)
    #проверяем есть ли юзер(на всякий случай)
    if user.is_user_created():
        #если есть, проверяем есть ли у него активный чар
        if user.is_user_inactive_char():
            await message.answer('Привет! У тебя ещё нет персонажа. Создать его можно с помощью команды /new')
        else:
            char = await user.get_char_name()
            name = char.get('name')
            await message.answer(f'Привет! Твой {name} тебя заждался. '
                                 f'Посмотреть его характеристики можно с помощью команды /char')
    else:
        #если юзера нет, то отправляем приветы
        await message.answer('Добро пожаловать в бесконечные подземелья! '
                             'У тебя ещё нет персонажа. Создать его можно с помощью команды /new \n'
                             'Подробнее об игре по команде /info')
        #добавляем юзера в бд
        await user.create_char()


