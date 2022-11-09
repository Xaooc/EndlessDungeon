from aiogram.fsm.state import StatesGroup, State


class StartDialog(StatesGroup):
    start = State()
    info = State()


class CreateChar(StatesGroup):
    start = State()
    choice = State()
    name = State()


