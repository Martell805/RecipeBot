import logging
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '6203341812:AAFuPdsP-g0kjW0XkiNRUxjsn6EJ1hwLY-8'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
