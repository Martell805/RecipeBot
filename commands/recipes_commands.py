from aiogram.types import Message

from general import dp, session
from models.Recipe import Recipe


@dp.message_handler(regexp=r"/add *\n*\n*")
async def add_recipe(message: Message):
    text = message.text.split('\n')

    new_recipe = Recipe(text[0].split()[1], text[1], text[2])
    session.add(new_recipe)
    session.commit()

    await message.answer("Привет, это бот с рецептами. Выберете кнопку для продолжения")
