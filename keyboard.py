from aiogram import types
from datetime import datetime
import calendar


def create_order_keyboard():
    keyboard_buttons = [[types.KeyboardButton(text="Создать заказ")]]
    return types.ReplyKeyboardMarkup(keyboard=keyboard_buttons)

def choose_type_keyboard():
    keyboard_buttons = [[types.InlineKeyboardButton(text='Услуга курьера',callback_data='choose_type_deliver')],
                        [types.InlineKeyboardButton(text='Доаставка в пункт самовывоза',callback_data='choose_type_place')]]
    keyboard_buttons += [[types.InlineKeyboardButton(
        text="Отмена", callback_data="exit")]]
    return types.InlineKeyboardMarkup(inline_keyboard=keyboard_buttons)

def choose_type_cell():
    # Добавить из бд ?
    keyboard_buttons = [[types.InlineKeyboardButton(text="1м2 300",callback_data="choose_cell_first")],
                        [types.InlineKeyboardButton(text="2м2 300",callback_data="choose_cell_second")],
                        [types.InlineKeyboardButton(text="3м2 300",callback_data="choose_cell_threed")],]
    keyboard_buttons += [[types.InlineKeyboardButton(
        text="Отмена", callback_data="exit")]]
    return types.InlineKeyboardMarkup(inline_keyboard=keyboard_buttons)

def choose_type_place():
    # Добавить из бд ?
    keyboard_buttons = [[types.InlineKeyboardButton(text="Кукушкино",callback_data="choose_place_first")],
                        [types.InlineKeyboardButton(text="Хующкино",callback_data="choose_place_second")],
                        [types.InlineKeyboardButton(text="Залупино",callback_data="choose_place_threed")],]
    keyboard_buttons += [[types.InlineKeyboardButton(
        text="Отмена", callback_data="exit")]]
    return types.InlineKeyboardMarkup(inline_keyboard=keyboard_buttons)    





def create_calendar(year, month, type_callback):
    keyboard_buttons = [[types.InlineKeyboardButton(
        text='<<', callback_data=f'month_prev_{year}_{month}'),
        types.InlineKeyboardButton(
            text="{} - {}".format(calendar.month_name[month],year), callback_data='ignore'),
        types.InlineKeyboardButton(
            text='>>', callback_data=f'month_next_{year}_{month}')],]

    month_days = calendar.monthcalendar(year, month)
    print("test",year, month)
    for week in month_days:
        row = []
        for day in week:
            if day == 0:
                row.append(types.InlineKeyboardButton(
                    text=' ', callback_data='ignore'))
            else:
                row.append(types.InlineKeyboardButton(text=str(day),
                           callback_data=f'{type_callback}_day_{year}_{month}_{day}'))
        keyboard_buttons += [row]
    keyboard_buttons += [[types.InlineKeyboardButton(
        text="Отмена", callback_data="exit")]]

    return types.InlineKeyboardMarkup(inline_keyboard=keyboard_buttons)

