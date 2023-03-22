from aiogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton

from general import dp, session

from models.Recipe import Recipe


@dp.callback_query_handler(text="category_search_hint")
async def category_search_hint(callback: CallbackQuery) -> None:
    """
    Answer to callback category_search_hint. Gives user menu to choose category of recipe
    :param callback: Callback from TG
    :return: None
    """
    await callback.answer(cache_time=0)
    keyboard = InlineKeyboardMarkup() \
        .row(InlineKeyboardButton(text="Завтрак", callback_data="random_breakfast")) \
        .row(InlineKeyboardButton(text="Обед", callback_data="random_lunch")) \
        .row(InlineKeyboardButton(text="Ужин", callback_data="random_dinner"))

    await callback.message.answer("Выберите необходимую категорию", reply_markup=keyboard)


@dp.callback_query_handler(text="random_breakfast")
async def random_breakfast(callback: CallbackQuery) -> None:
    """
    Answer to callback random_breakfast. Sends back random recipe with "Завтрак" category
    :param callback: Callback from TG
    :return: None
    """
    result = session.query(Recipe).filter(Recipe.categories == "Завтрак").all()
    names = ', '.join([x.name for x in result])
    if not names:
        await callback.message.answer("Рецепты не найдены")
        return
    await callback.message.answer(names)


@dp.callback_query_handler(text="random_lunch")
async def random_lunch(callback: CallbackQuery) -> None:
    """
    Answer to callback random_lunch. Sends back random recipe with "Обед" category
    :param callback: Callback from TG
    :return: None
    """
    result = session.query(Recipe).filter(Recipe.categories == "Обед").all()
    names = ', '.join([x.name for x in result])
    if not names:
        await callback.message.answer("Рецепты не найдены")
        return
    await callback.message.answer(names)


@dp.callback_query_handler(text="random_dinner")
async def random_dinner(callback: CallbackQuery) -> None:
    """
    Answer to callback random_dinner. Sends back random recipe with "Ужин" category
    :param callback: Callback from TG
    :return: None
    """
    result = session.query(Recipe).filter(Recipe.categories == "Ужин").all()
    names = ', '.join([x.name for x in result])
    if not names:
        await callback.message.answer("Рецепты не найдены")
        return
    await callback.message.answer(names)
