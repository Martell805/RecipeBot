from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from general import dp


@dp.message_handler(commands=["start", "help"])
async def send_welcome(message: Message):
    """
    Function which answers "/start" or "/help" and sends bot`s main menu
    :param message: Message from TG
    :return: None
    """

    keyboard = InlineKeyboardMarkup()\
        .row(InlineKeyboardButton(text="Случайный рецепт", callback_data="random_recipe"))\
        .row(InlineKeyboardButton(text="Поиск рецепта по категории", callback_data="category_search_hint"))\

    await message.answer("Привет, это бот с рецептами. Выберите кнопку для продолжения", reply_markup=keyboard)
