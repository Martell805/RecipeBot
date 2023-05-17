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
    result = session.query(Recipe).filter(Recipe.categories == "завтрак").all()
    ans = "Завтрак 🍳\n\n"
    for i in range(len(result)):
        ans += f'{i+1}. {result[i].get_name()}\n'
    if not result:
        await callback.message.answer("Рецепты с такой категорией не найдены😣")
        return
    await callback.message.answer(ans)


@dp.callback_query_handler(text="random_lunch")
async def random_lunch(callback: CallbackQuery) -> None:
    """
    Answer to callback random_lunch. Sends back random recipe with "Обед" category
    :param callback: Callback from TG
    :return: None
    """
    result = session.query(Recipe).filter(Recipe.categories == "обед").all()
    ans = "Обед 🍲\n\n"
    for i in range(len(result)):
        ans += f'{i+1}. {result[i].get_name()}\n'
    if not result:
        await callback.message.answer("Рецепты с такой категорией не найдены😣")
        return
    await callback.message.answer(ans)


@dp.callback_query_handler(text="random_dinner")
async def random_dinner(callback: CallbackQuery) -> None:
    """
    Answer to callback random_dinner. Sends back random recipe with "Ужин" category
    :param callback: Callback from TG
    :return: None
    """
    result = session.query(Recipe).filter(Recipe.categories == "ужин").all()
    ans = "Ужин 🍝\n\n"
    for i in range(len(result)):
        ans += f'{i+1}. {result[i].get_name()}\n'
    if not result:
        await callback.message.answer("Рецепты с такой категорией не найдены😣")
        return
    await callback.message.answer(ans)
