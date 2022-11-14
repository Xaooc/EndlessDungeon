from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram.filters import Command
from aiogram import Router
import buttons as bt

router = Router()


@router.message(Command("info"))
async def start(message: Message, state: FSMContext):
    await message.reply('Ты попал в бесконечные подземелья. '
                         'Здесь твой персонаж будет добывать золото, пока ты занимаешься своими делами.\n'
                         'Иногда от тебя потребуется выбрать как поступить персонажу - '
                         'действия требуют разных проверок: выносливость, ловкость, мудрость.\n\n'
                         'Не забывайте, что ваш персонаж может умереть. Жизни восстанавливаются каждый день\n\n'
                         'В планах добавить:\n'
                        '•Повышение уровня за золото\n'
                        '•Воскрешение за золото\n'
                        '•Таблицу лидеров для групповых чатов\n'
                        '•Вызов на дуэли\n'
                        '•Возможно, ставки на дуэли\n'
                        '•Режим для групповых чатов, где создаётся один персонаж на весь чат и действия выбираются голосованием\n\n'
                         'Предложения и пожелания можете писать @Xaoac41', reply_markup=bt.ReplyKeyboardRemove())


