from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

from dispatcher import dp


@dp.message_handler(commands=["start", "help"])
async def send_welcome(message: Message):

    keyboard = InlineKeyboardMarkup()\
        .row(InlineKeyboardButton(text="Случайный рецепт", callback_data="random_recipe"))\
        .row(InlineKeyboardButton(text="Поиск рецепта по категории", callback_data="category_search_hint"))\
        .row(InlineKeyboardButton(text="Поиск рецепта по ингредиентам", callback_data="ingredient_search_hint"))\

    await message.answer("Привет, это бот с рецептами. Выберете кнопку для продолжения", reply_markup=keyboard)


@dp.callback_query_handler(text="random_recipe")
async def random_recipe(callback: CallbackQuery):
    keyboard = InlineKeyboardMarkup(one_time_keyboard=True).row(
        InlineKeyboardButton(text="+", callback_data="upvote:0"),
        InlineKeyboardButton(text="-", callback_data="downvote:0"),
    )

    await callback.answer(cache_time=0)
    await callback.message.answer("Типа случайный рецепт", reply_markup=keyboard)


@dp.callback_query_handler(text="category_search_hint")
async def category_search_hint(callback: CallbackQuery):
    await callback.answer(cache_time=0)
    await callback.message.answer("Для поиска введите: '`Категории: `<Категории блюда>'", parse_mode="MarkDown")


@dp.message_handler(regexp=r"Категории: *")
async def category_search(message: Message):
    await message.answer("Суп, каша")


@dp.callback_query_handler(text="ingredient_search_hint")
async def ingredient_search_hint(callback: CallbackQuery):
    await callback.answer(cache_time=0)
    await callback.message.answer("Для поиска введите: '`Ингредиенты: `<Ингредиенты блюда>'", parse_mode="MarkDown")


@dp.message_handler(regexp=r"Ингредиенты: *")
async def ingredient_search(message: Message):
    await message.answer("Разные салаты")
