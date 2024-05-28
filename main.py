import asyncio

import aioschedule
from aiogram import executor

from general import SqlAlchemyBase, engine

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from sqlalchemy.sql import func

from general import dp, session, bot
from models.Recipe import Recipe
from models.Subscription import Subscription

from commands import *


async def send_all_recipies():
    subs = session.query(Subscription).all()

    recipe = session.query(Recipe).order_by(func.random()).first()

    keyboard = InlineKeyboardMarkup(one_time_keyboard=True).row(
        InlineKeyboardButton(text="👍🏻", callback_data="upvote " + str(recipe.id)),
        InlineKeyboardButton(text="👎🏻", callback_data="downvote " + str(recipe.id)),
        InlineKeyboardButton(text="🌟", callback_data="favourite " + str(recipe.id)),
        InlineKeyboardButton(text="🚫", callback_data="avoid " + str(recipe.id)),
    )

    for sub in subs:
        await bot.send_photo(sub.user_id, recipe.get_photo_id(), caption=recipe, reply_markup=keyboard)


async def scheduler():
    aioschedule.every().day.at("12:00").do(send_all_recipies)

    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)

async def on_startup(_):
    asyncio.create_task(scheduler())


SqlAlchemyBase.metadata.create_all(engine)

executor.start_polling(dp, skip_updates=False, on_startup=on_startup)
