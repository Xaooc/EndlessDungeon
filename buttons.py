from aiogram.types import KeyboardButton, ReplyKeyboardRemove
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from random import choice

yesno = ['Да', 'Нет']
yes = KeyboardButton(text="Да")
no = KeyboardButton(text="Нет")

go = KeyboardButton(text="Отправиться в подземелье")
back = KeyboardButton(text="Назад")
go_btn = ['Отправиться в подземелье']

ok_bt = ['Понятно', 'Ок', 'Хорошо', 'Ладно', 'Дальше']
ok = KeyboardButton(text=choice(ok_bt))


kb_yesno = ReplyKeyboardBuilder().add(yes).add(no) \
    .as_markup(resize_keyboard=True, input_field_placeholder="У тебя уже есть персонаж. "
                                                             "Хочешь создать нового?", selective=True)
kb_back = ReplyKeyboardBuilder().add(back) \
    .as_markup(resize_keyboard=True, input_field_placeholder="Как будут звать твоего нового персонажа?", selective=True)
kb_go = ReplyKeyboardBuilder().add(go).add(back) \
    .as_markup(resize_keyboard=True, input_field_placeholder="Вы точно хотите спуститься в подземелье?", selective=True)
kb_ok = ReplyKeyboardBuilder().add(ok) \
    .as_markup(resize_keyboard=True, input_field_placeholder="Продолжим?", selective=True)


def room_kb(events: list):
    first_event = KeyboardButton(text=events[0])
    second_event = KeyboardButton(text=events[1])
    return ReplyKeyboardBuilder().add(first_event).add(second_event) \
        .as_markup(resize_keyboard=True, input_field_placeholder="Что будете делать?", selective=True)
