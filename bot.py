from dotenv import load_dotenv
from os import environ
import asyncio
import logging
import sys
from os import getenv
from aiogram import Bot, Dispatcher, html, Router
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery
from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.ext.asyncio import AsyncSession
from aiogram import F
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from aiogram.utils.callback_answer import CallbackAnswerMiddleware
from sqlalchemy.ext.declarative import declarative_base
from middleware import DbSessionMiddleware
from handlers import say_hello
from db import Client, Order, Base


async def test(message: Message, session: AsyncSession):
    await message.answer("TEST")


async def init_db(async_engine):
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def main():
    load_dotenv()
    engine = create_async_engine(url=environ['DATABASE_URL'], echo=True)
    sessionmaker = async_sessionmaker(engine, expire_on_commit=False)
    await init_db(engine)
    bot_token = environ['BOT_TOKEN']
    bot = Bot(token=bot_token, default=DefaultBotProperties(
        parse_mode=ParseMode.HTML))
    dp = Dispatcher()
    dp.update.middleware(DbSessionMiddleware(session_pool=sessionmaker))
    dp.message.register(say_hello, CommandStart())
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
