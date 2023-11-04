import asyncio
import logging
import aiogram
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command

logging.basicConfig(level=logging.INFO)

BOT_TOKEN = Bot(token="№№№")


dp = Dispatcher()


@dp.message(Command("start"))
async def cmd_start(message:types.Message):
    await message.answer("Добрый день!Я бот который показует время! Вы можете узнать время по команде /time")


@dp.message(Command("time"))
async def cmd_time(message:types.Message):
    await message.answer(f"Время h:{message.date.hour + 2}, m:{message.date.minute}, s: {message.date.second}")

@dp.message()
async def message_handler(message: types.Message):
    await message.answer(f"Не поничаю вашу команду!Доступные команды: /time, /start")

async def main():
    await dp.start_polling(BOT_TOKEN)

if __name__ == "__main__":
    asyncio.run(main())