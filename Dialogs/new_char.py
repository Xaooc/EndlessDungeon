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
    user = UserData(tg_id=message.from_user.id)
    await state.update_data(user=user)
    user_data = await state.get_data()
    if user_data['user'].is_user_inactive_char():
        await message.answer('Как зовут твоего персонажа?')
        await state.set_state(st.CreateChar.name)
    else:
        await message.answer('У тебя уже есть персонаж. Хочешь создать нового?', reply_markup=bt.kb_yesno)
        await state.set_state(st.CreateChar.choice)


@router.message(st.CreateChar.choice, F.text.in_(bt.yesno))
async def name(message: Message, state: FSMContext):
    user_data = await state.get_data()
    if message.text.lower() == 'да':
        await message.answer('Как будут звать твоего нового персонажа?', reply_markup=bt.ReplyKeyboardRemove())
        await state.set_state(st.CreateChar.name)
    else:
        char = await user_data['user'].get_char_name()
        name = char.get('name')
        await message.answer(f'Понимаю, сложно бросить своего мистера {name}', reply_markup=bt.ReplyKeyboardRemove())
        await state.clear()


@router.message(st.CreateChar.name)
async def new_done(message: Message, state: FSMContext):
    char = GeneratorPers(message.text, message.from_user.id)
    await char.new()
    await message.answer(f'Отныне звать его будут так. Чтобы посмотреть характеристику своего персонажа,'
                         f' введи команду /char', reply_markup=bt.ReplyKeyboardRemove())
    await state.clear()
