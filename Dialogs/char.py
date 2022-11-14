from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram.filters import Command
from aiogram import Router

from database import UserData
import buttons as bt

router = Router()


@router.message(Command("char"))
async def char(message: Message, state: FSMContext):
    tid = float(str(message.chat.id) + '.' + str(message.from_user.id))
    user = UserData(tg_id=tid)
    #проверяем есть ли активный персонаж
    if user.is_user_inactive_char() or not user.is_user_created():
        await message.reply('У тебя ещё нет активного персонажа. '
                             'Создать его ты можешь с помощью команды /new', reply_markup=bt.ReplyKeyboardRemove())
    else:
        char = await user.get_char()
        name = char.get('name')
        con = char.get('con')
        dex = char.get('dex')
        mnd = char.get('mnd')
        gold = char.get('gold')
        hp = char.get('hp')
        await message.reply(f'*Имя персонажа:* {name}  *Здоровье:* {hp}\n'
                             f'*Телосложение:* {con}  *Ловкость:* {dex}  *Мудрость:* {mnd}\n'
                             f'*Золото:* {gold}', parse_mode="MarkdownV2")



