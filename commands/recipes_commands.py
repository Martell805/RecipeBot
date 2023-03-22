from aiogram.types import Message

from general import dp, session
from models.Recipe import Recipe


@dp.message_handler(regexp=r"/add *\n*\n*\n*")
async def add_recipe(message: Message) -> None:
    """
    Function which answers "/add" and adds given recipe to database
    :param message: Message from TG
    :return: None
    """
    text = message.text.split('\n')

    new_recipe = Recipe(text[0].split()[1], text[1], text[2], text[3])
    session.add(new_recipe)
    session.commit()

    await message.answer(f"Рецепт {new_recipe.name} успешно добавлен!")


@dp.message_handler(regexp=r"/find [а-яА-я0-9 ]*")
async def add_recipe(message: Message) -> None:
    """
    Function which answers "/find" and shows requester recipe from database to user
    :param message: Message from TG
    :return: None
    """
    name = message.text[6:]

    result = session.query(Recipe).filter(Recipe.name == name).first()

    if not result:
        await message.answer("Такой рецепт не найден")
        return

    await message.answer(result)
