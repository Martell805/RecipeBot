from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from general import dp


@dp.message_handler(commands=["start", "help"])
async def send_welcome(message: Message) -> None:
    """
    Function which answers "/start" or "/help" and sends bot`s main menu
    :param message: Message from TG
    :return: None
    """

    keyboard = InlineKeyboardMarkup()\
        .row(InlineKeyboardButton(text="Случайный рецепт", callback_data="random_recipe"))\
        .row(InlineKeyboardButton(text="Поиск рецепта по названию", callback_data="find_recipe"))\
        .row(InlineKeyboardButton(text="Поиск рецепта по категории", callback_data="category_search_hint"))\
        .row(InlineKeyboardButton(text="Добавить рецепт", callback_data="add"))\
        .row(InlineKeyboardButton(text="Топ 5 рецептов", callback_data="top_recipes"))\

    await message.answer("Привет, это бот с рецептами!👋🏻👨🏻‍🍳\nВыберите кнопку для продолжения", reply_markup=keyboard)
