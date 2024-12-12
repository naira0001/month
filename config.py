#config.py
from aiogram import Bot, Dispatcher
from decouple import config

Admins = [738723836, ]

token = config('TOKEN')

bot = Bot(token=token)
dp = Dispatcher(bot)