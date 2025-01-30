#main.py

from aiogram import  executor
from config import bot, dp, Admins
import logging
from handlers import commands, echo, quiz, FSM_registration,webapp
from buttons import start
from db import main_db

async def on_startup(_):
    for admin in Admins:
        await bot.send_message(chat_id=admin, text='БОТ включен !', reply_markup=start)

    await main_db.create_db()

async def on_shutdown(_):
    for admin in Admins:
        await bot.send_message(chat_id=admin, text='БОТ выключен !')


commands.register_commands_handlers(dp)
quiz.register_quiz_handlers(dp)
webapp.register_handlers(dp)
FSM_registration.register_handlers_fsm_reg(dp)


echo.register_echo_handler(dp)




if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup ,
                           on_shutdown=on_shutdown)
