import asyncio
import logging
import sys
from os import getenv

from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from handler import start_handler,create_order
from callback import choose_type_callback,choose_price_callback,drop_state_callback,swith_month_callback,choose_first_date_callback,choose_last_date_callback
from state import CreateOrder
from aiogram import F




async def main() -> None:
    TOKEN = ""
    dp = Dispatcher()
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp.message.register(start_handler,CommandStart())
    dp.message.register(create_order,F.text=="Создать заказ")
    dp.callback_query.register(drop_state_callback,F.data == 'exit')
    dp.callback_query.register(swith_month_callback,F.data.startswith('month_'))
    dp.callback_query.register(choose_type_callback,F.data.startswith('choose_type_'),CreateOrder.choose_type)
    dp.callback_query.register(choose_price_callback,F.data.startswith('choose_cell_'),CreateOrder.choose_price)
    dp.callback_query.register(choose_first_date_callback,F.data.startswith('first_'),CreateOrder.choose_start_date)
    dp.callback_query.register(choose_last_date_callback,F.data.startswith('second_'),CreateOrder.choose_last_date)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())