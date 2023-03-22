from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton

from general import dp, session

from models.Recipe import Recipe


@dp.callback_query_handler(text="category_search_hint")
async def category_search_hint(callback: CallbackQuery):
    await callback.answer(cache_time=0)
    keyboard = InlineKeyboardMarkup() \
        .row(InlineKeyboardButton(text="Завтрак", callback_data="random_breakfast")) \
        .row(InlineKeyboardButton(text="Обед", callback_data="random_lunch")) \
        .row(InlineKeyboardButton(text="Ужин", callback_data="random_dinner"))

    await callback.message.answer("Выберите необходимую категорию", reply_markup=keyboard)


@dp.callback_query_handler(text="random_breakfast")
async def random_breakfast(callback: CallbackQuery):
    result = session.query(Recipe).filter(Recipe.categories == "Завтрак").all()
    names = ', '.join([x.name for x in result])
    if len(names) == 0:
        await callback.message.answer("Рецепты не найдены")
    else:
        await callback.message.answer(names)


@dp.callback_query_handler(text="random_lunch")
async def random_lunch(callback: CallbackQuery):
    result = session.query(Recipe).filter(Recipe.categories == "Обед").all()
    names = ', '.join([x.name for x in result])
    if len(names) == 0:
        await callback.message.answer("Рецепты не найдены")
    else:
        await callback.message.answer(names)


@dp.callback_query_handler(text="random_dinner")
async def random_dinner(callback: CallbackQuery):
    result = session.query(Recipe).filter(Recipe.categories == "Ужин").all()
    names = ', '.join([x.name for x in result])
    if len(names) == 0:
        await callback.message.answer("Рецепты не найдены")
    else:
        await callback.message.answer(names)


@dp.callback_query_handler(text="ingredient_search_hint")
async def ingredient_search_hint(callback: CallbackQuery):
    await callback.answer(cache_time=0)
    await callback.message.answer("Для поиска введите: '`Ингредиенты: `<Ингредиенты блюда>'", parse_mode="MarkDown")


@dp.message_handler(regexp=r"Ингредиенты: *")
async def ingredient_search(message: Message):
    await message.answer("Разные салаты")
