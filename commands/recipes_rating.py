from aiogram.types import CallbackQuery

from general import dp, session
from models.Recipe import Recipe


@dp.callback_query_handler(regexp=r"upvote [0-9]*")
async def upvote(callback: CallbackQuery) -> None:
    """
    Answer to callback upvote. Adds recipe's thumb up.
    :param callback: Callback from TG
    :return: None
    """
    recipe_id = int(callback.data.split()[1])
    recipe = session.query(Recipe).filter(Recipe.id == recipe_id).first()
    recipe.inc_rating()
    session.commit()

    ans = f"Спасибо за ваше мнение!\n\nРейтинг блюда \"{recipe.get_name()}\"🏆" \
          f"\nПонравилось: {recipe.get_thumbs_up()}👍🏻\nНе понравилось: {recipe.get_thumbs_down()}👎🏻"
    await callback.answer(cache_time=0)
    await callback.message.answer(ans)


@dp.callback_query_handler(regexp=r"downvote [0-9]*")
async def downvote(callback: CallbackQuery) -> None:
    """
    Answer to callback downvote. Adds recipe's thumb down.
    :param callback: Callback from TG
    :return: None
    """
    recipe_id = int(callback.data.split()[1])
    recipe = session.query(Recipe).filter(Recipe.id == recipe_id).first()
    recipe.dec_rating()
    session.commit()

    ans = f"Спасибо за ваше мнение!\n\nРейтинг блюда \"{recipe.get_name()}\"🏆" \
          f"\nПонравилось: {recipe.get_thumbs_up()}👍🏻\nНе понравилось: {recipe.get_thumbs_down()}👎🏻"
    await callback.answer(cache_time=0)
    await callback.message.answer(ans)
