from aiogram.types import CallbackQuery

from general import dp, session
from models.Subscription import Subscription


@dp.callback_query_handler(text="subscribe")
async def subscribe(callback: CallbackQuery) -> None:
    """
    Answer to callback subscribe. Subscribes user to daily recipe.
    :param callback: Callback from TG
    :return: None
    """
    user_id = callback.from_user.id

    sub = session.query(Subscription).filter(Subscription.user_id == user_id).first()

    if sub: return

    sub = Subscription(user_id)

    session.add(sub)
    session.commit()

    ans = f"🕛Вы успешно подписались на рассылку!🕛"
    await callback.answer(cache_time=0)
    await callback.message.answer(ans)

@dp.callback_query_handler(text="unsubscribe")
async def unsubscribe(callback: CallbackQuery) -> None:
    """
    Answer to callback unsubscribe. Unsubscribe user to daily recipe.
    :param callback: Callback from TG
    :return: None
    """
    user_id = callback.from_user.id

    sub = session.query(Subscription).filter(Subscription.user_id == user_id).first()

    if not sub: return

    session.delete(sub)
    session.commit()

    ans = f"❌Вы успешно отписались от рассылки!❌"
    await callback.answer(cache_time=0)
    await callback.message.answer(ans)
