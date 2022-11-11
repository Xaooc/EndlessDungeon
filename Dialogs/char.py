from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram.filters import Command
from aiogram import Router

from database import UserData


router = Router()


@router.message(Command("char"))
async def char(message: Message, state: FSMContext):
    user = UserData(tg_id=message.from_user.id)
    #проверяем есть ли активный персонаж
    if user.is_user_inactive_char() or not user.is_user_created():
        await message.answer('У тебя ещё нет активного персонажа. Создать его ты можешь с помощью команды /new')
    else:
        char = await user.get_char_name()
        name = char.get('name')
        con = char.get('con')
        dex = char.get('dex')
        mnd = char.get('mnd')
        gold = char.get('gold')
        await message.answer(f'*Имя персонажа:* {name}\n'
                             f'*Телосложение:* {con}  *Ловкость:* {dex}  *Мудрость:* {mnd}\n'
                             f'*Золото:* {gold}', parse_mode="MarkdownV2")



