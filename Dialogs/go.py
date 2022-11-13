import asyncio

from Dungeons import rooms
from Dungeons import events

from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram.filters import Command
from aiogram import Router

import states as st
import buttons as bt
from database import UserData

router = Router()


@router.message(st.Go.waiting)
async def wait(message: Message, state: FSMContext):
    user_data = await state.get_data()
    msg = user_data['msg']
    await message.answer(msg, reply_markup=bt.ReplyKeyboardRemove())


@router.message(st.Go.dung)
async def dung(message: Message, state: FSMContext):
    user_data = await state.get_data()
    level = user_data['level']
    path = user_data['path']
    gold = user_data['gold']
    room = await rooms.get_room(int(path[level]))
    btns = await events.get_button(room.get('event'))
    user = await user_data['user'].get_char_name()
    await user_data['user'].update_place(path[level])
    if message.text in btns:
        ev_to_id = await events.get_id(room.get('event'))
        event = ev_to_id.get(message.text)
        con = user.get('con')
        dex = user.get('dex')
        mnd = user.get('mnd')
        result = await events.get_result(event, con, dex, mnd)
        msg = result.get('msg')
        await state.update_data(msg=msg)
        await message.answer(msg, reply_markup=bt.ReplyKeyboardRemove())
        await state.set_state(st.Go.waiting)
        await asyncio.sleep(result.get('time'))
        await message.answer(result.get('description'), reply_markup=bt.kb_ok)
        if result.get('type') == 'damage':
            if not await user_data['user'].hp_mod(result.get('effect')):
                name = user.get('name')
                await message.answer(f'{name} теперь мёртв. Жаль, конечно, этого добряка...\n\n'
                                     f'Нового персонажа можешь создать по команде /new',
                                     reply_markup=bt.ReplyKeyboardRemove())
                await state.clear()
                return ''
        if result.get('type') == 'gold':
            await user_data['user'].gold_mod(result.get('effect'))
            gold += result.get('effect')
            await state.update_data(gold=gold)
        if level < len(path):
            level += 1
            await state.update_data(level=level)
            await state.set_state(st.Go.dung)
        else:
            name = user.get('name')
            hp = user.get('hp')
            gold = user_data['gold']
            await message.answer(f'Кажется, это была последняя комната. Можно возвращаться.\n'
                                 f'За этот заход было получено {gold} золота'
                                 f'Здоровье {name} = {hp}. Не забывайте, что жизни у него восстановятся только завтра.',
                                 reply_markup=bt.ReplyKeyboardRemove())
            await state.clear()
    else:
        await message.answer(room.get('description'), reply_markup=bt.room_kb(btns))


@router.message(Command("go"))
async def go(message: Message, state: FSMContext):
    # записываем экземпляр, чтобы передавать между статусами
    user = UserData(tg_id=message.from_user.id)
    level = 0
    gold = 0
    path = rooms.path()
    await state.update_data(gold=gold, path=path, level=level, user=user)
    if not user.is_user_created():
        await user.create_char()
    if user.is_user_inactive_char():
        await message.answer('Кажется, тебе некого отправить в подземелье. '
                             'Создать себе персонажа можешь с помощью команды /new',
                             reply_markup=bt.ReplyKeyboardRemove())
    else:
        await message.answer('Вы подходите к тёмному спуску в неизведанные туннели. Там наверняка много золота. '
                             'Но и опасности не меньше. Вы точно хотите туда пойти?', reply_markup=bt.kb_go)
        await state.set_state(st.Go.dung)



