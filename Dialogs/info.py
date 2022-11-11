from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram.filters import Command
from aiogram import Router

router = Router()


@router.message(Command("info"))
async def start(message: Message, state: FSMContext):
    await message.answer('Ты попал в бесконечные подземелья. '
                         'Здесь твой персонаж будет добывать золото, пока ты занимаешься своими делами\n'
                         'Иногда от тебя потребуется выбрать как поступить персонажу - '
                         'от твоего выбора будут зависеть его действия и шансы на успех\n\n'
                         'Позже планирую добавить в игру режим группы, где на группу будет создаваться '
                         'отдельный персонаж и выбор его действий будет происходить общим голосованием.\n\n'
                         'Предложения и пожелания можете писать @Xaoac41')


