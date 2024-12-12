#echo.py
from aiogram import types, Dispatcher

async def echo_handler(message: types.Message):
   if message.text.isdigit():  # Проверяем, состоит ли текст только из цифр
        number = int(message.text)
        await message.answer(f"Квадрат числа: {number ** 2}")
   else:
        await message.answer(message.text)

def register_echo_handler(dp: Dispatcher):
    dp.register_message_handler(echo_handler)