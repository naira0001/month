#main.py
import logging

from aiogram import types, executor
from config import bot, dp
import logging
import os


@dp.message_handler(commands=["start", "help"])
async def start_handler(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text=f'hello {message.from_user.first_name}!\n'
                                f'Твой Telegram ID - {message.from_user.id}')

@dp.message_handler(commands=["mem"])
async def mem_handler(message: types.Message):
    photo_path = os.path.join('media', 'img.png')
    with open(photo_path, 'rb') as photo:
        await message.answer_photo(photo=photo, caption='мемчик')

#===============================================

@dp.message_handler()
async def echo_handler(message: types.Message):
   if message.text.isdigit():  # Проверяем, состоит ли текст только из цифр
        number = int(message.text)
        await message.answer(f"Квадрат числа: {number ** 2}")
   else:
        await message.answer(message.text)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)