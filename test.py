import asyncio

from aiogram import Bot, Dispatcher, Router
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from aiogram_dialog import Window, Dialog, DialogRegistry, DialogManager, StartMode
from aiogram_dialog.widgets.kbd import Button
from aiogram_dialog.widgets.text import Const

bot = Bot(token='5171317422:AAFjOCgrdBn2bFEa-RFIXmglSAmGH1TfdX4')
dp = Dispatcher(storage=MemoryStorage())
registry = DialogRegistry(dp)
router = Router()


async def next(c: CallbackQuery, button: Button, manager: DialogManager):
    await manager.next()


class StartDialog(StatesGroup):
    start = State()
    info = State()
    info = State()


new_pers = Dialog(
    Window(
        Const('Привет. Вижу, ты тут впервые...'),
        Button(Const('Куда я попал?'), id="sd_q", on_click=next),
        state=StartDialog.start
    ),
    Window(
        Const('Ух, тут всё не так просто. Наверное, всё-таки не туда, куда хотел'),
        Button(Const('Куда я попал?'), id="sd_i", on_click=next),
        state=StartDialog.start
    )
)
dp.add_dialog(new_pers)


# registry.register()


@dp.message(Command(commands=["start"]))
async def start(m: Message, dialog_manager: DialogManager):
    await dialog_manager.start(StartDialog.start, mode=StartMode.RESET_STACK)



