from sqlalchemy.ext.asyncio import AsyncSession
from aiogram import types
from buttons import actions

async def say_hello(message:types.Message,session:AsyncSession):
    await message.answer(text="test",reply_markup=actions())