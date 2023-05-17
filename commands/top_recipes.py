from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

from general import dp, session, bot
from models.Recipe import Recipe


@dp.callback_query_handler(text="top_recipes")
async def find_recipe(call: CallbackQuery):
    """
    Function which answers "top_recipes" and shows requester 5 best recipes from database to user
    :param message: Message from TG
    :return: None
    """
    result = session.query(Recipe).all()
    result.sort(key=lambda x: x.get_thumbs_up(), reverse=True)
    ans = f'\n\n1️⃣{result[0].get_name()} (Категория: {result[0].get_categories().title()})\nПонравилось: {result[0].get_thumbs_up()}👍🏻\n\n' \
          f'2️⃣{result[1].get_name()} (Категория: {result[1].get_categories().title()})\nПонравилось: {result[1].get_thumbs_up()}👍🏻\n\n' \
          f'3️⃣{result[2].get_name()} (Категория: {result[2].get_categories().title()})\nПонравилось: {result[2].get_thumbs_up()}👍🏻\n\n' \
          f'4️⃣{result[3].get_name()} (Категория: {result[3].get_categories().title()})\nПонравилось: {result[3].get_thumbs_up()}👍🏻\n\n' \
          f'5️⃣{result[4].get_name()} (Категория: {result[4].get_categories().title()})\nПонравилось: {result[4].get_thumbs_up()}👍🏻\n\n'
    await call.message.answer("Топ 5 рецептов нашего бота:" + ans)
