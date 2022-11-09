from aiogram.types import KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

yes = KeyboardButton(text="Да")
no = KeyboardButton(text="Нет")

yesno = ['Да', 'Нет']
kb_yesno = ReplyKeyboardBuilder().add(yes).add(no).as_markup(resize_keyboard=True)
