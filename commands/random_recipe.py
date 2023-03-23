from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

from sqlalchemy.sql import func

from general import dp, session
from models.Recipe import Recipe


@dp.callback_query_handler(text="random_recipe")
async def random_recipe(callback: CallbackQuery) -> None:
    """
    Answer to callback random_recipe. Sends back random recipe
    :param callback: Callback from TG
    :return: None
    """
    recipe = session.query(Recipe).order_by(func.random()).first()

    keyboard = InlineKeyboardMarkup(one_time_keyboard=True).row(
        InlineKeyboardButton(text="+", callback_data="upvote " + str(recipe.id)),
        InlineKeyboardButton(text="-", callback_data="downvote " + str(recipe.id)),
    )

    await callback.answer(cache_time=0)
    await callback.message.answer(recipe, reply_markup=keyboard)
