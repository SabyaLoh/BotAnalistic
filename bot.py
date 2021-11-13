from aiogram import executor
from dispatcher import dp
from handlers import personal_actions
import asyncio
from db import BotDB
BotDB = BotDB('account.db')

if __name__ == '__main__':
	loop = asyncio.get_event_loop()
	executor.start_polling(dp, skip_updates=True)