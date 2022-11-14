from datetime import datetime

from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram.filters import Command
from aiogram import Router, F

import states as st
import buttons as bt
from database import UserData
from create_pers import GeneratorPers

router = Router()


@router.message(Command("new"))
async def new(message: Message, state: FSMContext):
    #записываем экземпляр, чтобы передавать между статусами
    tid = float(str(message.chat.id) + '.' + str(message.from_user.id))
    user = UserData(tg_id=tid)
    await state.update_data(user=user)
    if not user.is_user_created():
        await user.create_char()
    date = await user.get_char()
    date = date.get('date')
    if user.is_user_inactive_char():
        await message.reply('Как зовут твоего персонажа?', reply_markup=bt.ReplyKeyboardRemove())
        await state.set_state(st.CreateChar.name)
    elif str(datetime.date(datetime.today())) == date:
        await message.reply('Что-то ты зачастил со сменой персонажа. Давай завтра.', reply_markup=bt.ReplyKeyboardRemove())
    else:
        await message.reply('У тебя уже есть персонаж. Хочешь создать нового?', reply_markup=bt.kb_yesno)
        await state.set_state(st.CreateChar.choice)


@router.message(st.CreateChar.choice, F.text.in_(bt.yesno))
async def name(message: Message, state: FSMContext):
    user_data = await state.get_data()
    if message.text.lower() == 'да':
        await message.reply('Как будут звать твоего нового персонажа?', reply_markup=bt.kb_back)
        await state.set_state(st.CreateChar.name)
    else:
        char = await user_data['user'].get_char()
        name = char.get('name')
        await message.reply(f'Понимаю, сложно бросить такое чудо как {name}', reply_markup=bt.ReplyKeyboardRemove())
        await state.clear()


@router.message(st.CreateChar.name)
async def new_done(message: Message, state: FSMContext):
    if message.text.lower() == 'назад':
        user_data = await state.get_data()
        char = await user_data['user'].get_char()
        name = char.get('name')
        await message.reply(f'Понимаю, сложно бросить такое чудо как {name}',
                             reply_markup=bt.ReplyKeyboardRemove())
        await state.clear()
    else:
        await state.set_state(st.CreateChar.choice)
        tid = float(str(message.chat.id) + '.' + str(message.from_user.id))
        char = GeneratorPers(message.text, tid)
        await char.new()
        await message.reply(f'Отныне звать его будут так. Чтобы посмотреть характеристики своего персонажа'
                             f' введи команду /char', reply_markup=bt.ReplyKeyboardRemove())
        await state.clear()
