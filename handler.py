from aiogram import types
from keyboard import create_order_keyboard,choose_type_keyboard
from aiogram.fsm.context import FSMContext
from state import CreateOrder

async def start_handler(message:types.Message,state:FSMContext):
    await state.clear()
    await message.answer("Привет!",reply_markup=create_order_keyboard())

async def create_order(message:types.Message,state:FSMContext):
    await message.delete()
    await state.set_state(CreateOrder.choose_type)
    await message.answer(text="Выберите спопсоб создания заказа",reply_markup=choose_type_keyboard())
