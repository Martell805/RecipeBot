from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

from sqlalchemy.sql import func

from general import dp, session, bot
from models.Recipe import Recipe
from models.Avoided import Avoided
from models.Favourite import Favourite

@dp.callback_query_handler(regexp=r"favourite [0-9]*")
async def favourite(callback: CallbackQuery) -> None:
    """
    Answer to callback favourite. Adds recipe to favourites.
    :param callback: Callback from TG
    :return: None
    """
    recipe_id = int(callback.data.split()[1])
    user_id = callback.from_user.id

    fav = session.query(Favourite).filter(Favourite.recipe_id == recipe_id and Favourite.user_id == user_id).first()
    avoided = session.query(Avoided).filter(Avoided.recipe_id == recipe_id and Avoided.user_id == user_id).first()

    if fav: return

    if avoided:
        session.delete(avoided)

    fav = Favourite(user_id, recipe_id)

    session.add(fav)
    session.commit()

    ans = f"🌟Рецепт успешно добавлен в избранное!🌟"
    await callback.answer(cache_time=0)
    await callback.message.answer(ans)

@dp.callback_query_handler(regexp=r"avoid [0-9]*")
async def avoid(callback: CallbackQuery) -> None:
    """
    Answer to callback avoid. Adds recipe to avoided.
    :param callback: Callback from TG
    :return: None
    """
    recipe_id = int(callback.data.split()[1])
    user_id = callback.from_user.id

    fav = session.query(Favourite).filter(Favourite.recipe_id == recipe_id and Favourite.user_id == user_id).first()
    avoided = session.query(Avoided).filter(Avoided.recipe_id == recipe_id and Avoided.user_id == user_id).first()

    if avoided: return

    if fav:
        session.delete(fav)

    avoided = Avoided(user_id, recipe_id)

    session.add(avoided)
    session.commit()

    ans = f"🚫Рецепт успешно скрыт!🚫"
    await callback.answer(cache_time=0)
    await callback.message.answer(ans)


@dp.callback_query_handler(text="random_favourite_recipe")
async def random_recipe(callback: CallbackQuery) -> None:
    """
    Answer to callback random_recipe. Sends back random recipe
    :param callback: Callback from TG
    :return: None
    """
    user_id = callback.from_user.id

    fav = session.query(Favourite).filter(Favourite.user_id == user_id).order_by(func.random()).first()

    if fav is None:
        await callback.answer(cache_time=0)
        await callback.message.answer("У вас пока нет избранных рецептов!")
        return

    recipe = session.query(Recipe).filter(Recipe.id == fav.recipe_id).order_by(func.random()).first()

    keyboard = InlineKeyboardMarkup(one_time_keyboard=True).row(
        InlineKeyboardButton(text="👍🏻", callback_data="upvote " + str(recipe.id)),
        InlineKeyboardButton(text="👎🏻", callback_data="downvote " + str(recipe.id)),
        InlineKeyboardButton(text="🌟", callback_data="favourite " + str(recipe.id)),
        InlineKeyboardButton(text="🚫", callback_data="avoid " + str(recipe.id)),
    )

    await callback.answer(cache_time=0)
    await bot.send_photo(callback.message.chat.id, recipe.get_photo_id(), caption=recipe, reply_markup=keyboard)
