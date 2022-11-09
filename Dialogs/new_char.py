from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram.filters import Command
from aiogram import Router, F

import states as st
import buttons as bt

router = Router()


@router.message(Command("new"))
async def star(message: Message, state: FSMContext):
    tg_id = message.from_user.id
    await message.answer('Привет. У тебя уже есть персонаж. Хочешь Создать нового?', reply_markup=bt.kb_yesno)
    await state.set_state(st.CreateChar.choice)


@router.message(st.CreateChar.choice, F.text.in_(bt.yesno))
async def food_size_chosen(message: Message, state: FSMContext):
    if message.text.lower() == 'да':
        await message.answer('Тогда введи имя', reply_markup=bt.ReplyKeyboardRemove())
        await state.set_state(st.CreateChar.name)
    else:
        await message.answer('Хорошо. Приходи ещё', reply_markup=bt.ReplyKeyboardRemove())
        await state.clear()


@router.message(st.CreateChar.name)
async def food_size_chosen(message: Message, state: FSMContext):
    await message.answer(f'Крутое имя {message.text}', reply_markup=bt.ReplyKeyboardRemove())
    await state.clear()
