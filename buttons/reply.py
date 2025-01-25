from aiogram import types

def actions():
    keyboard_buttons = [
        [types.KeyboardButton(text="Создать заказ")],
        [types.KeyboardButton(text="Просмотр заказов")]
    ]
    return types.ReplyKeyboardMarkup(keyboard=keyboard_buttons)

