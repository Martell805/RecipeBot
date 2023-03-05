from aiogram.types import Message, CallbackQuery

from general import dp


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
