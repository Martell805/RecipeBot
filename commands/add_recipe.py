from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import Message, InlineKeyboardMarkup, \
    InlineKeyboardButton, CallbackQuery

from general import dp, session
from models.Recipe import Recipe


class AddRecipe(StatesGroup):
    name = State()
    category = State()
    ingredients = State()
    description = State()
    photo = State()


@dp.callback_query_handler(text="add")
async def add_recipe(call: CallbackQuery):
    await call.message.answer(text='Отлично, давайте добавим новый рецепт! Для начала введите название рецепта 👨🏻‍🍳')
    await AddRecipe.name.set()


@dp.message_handler(state=AddRecipe.name)
async def input_name(message: Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text

    keyboard = InlineKeyboardMarkup() \
        .row(InlineKeyboardButton(text="Завтрак 🍳", callback_data="завтрак")) \
        .row(InlineKeyboardButton(text="Обед 🍲", callback_data="обед")) \
        .row(InlineKeyboardButton(text="Ужин 🍝", callback_data="ужин"))
    await message.answer(text="Название обещает нечто интересное! Теперь выберите категорию, к которой относится ваш "
                              "рецепт!", reply_markup=keyboard)
    await AddRecipe.category.set()


@dp.callback_query_handler(state=AddRecipe.category)
async def input_category(call: CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['category'] = call.data
    await call.message.answer(
        text="Думаю, этот рецепт отлично подойдёт для " + call.data + "а! Введите необходимые ингредиенты в формате: "
                                                                      "\n\"ингредиент 1\" - \"количество\" "
                                                                      "\n\"ингредиент 2\" - \"количество\"")
    await AddRecipe.ingredients.set()


@dp.message_handler(state=AddRecipe.ingredients)
async def input_ingredients(message: Message, state: FSMContext):
    async with state.proxy() as data:
        data['ingredients'] = message.text
    await message.answer(
        "С ингредиентами разобрались, перейдём к приготовлению! Введите описание процесса готовки👨🏻‍🍳")
    await AddRecipe.description.set()


@dp.message_handler(state=AddRecipe.description)
async def input_description(message: Message, state: FSMContext):
    async with state.proxy() as data:
        data['description'] = message.text
        print(data['name'])
        print(data['category'])
        print(data['description'])
    await message.answer(
        "Готово! И вишенка на торте - вид готового блюда🍰 Прикрепите фотографию")
    await AddRecipe.photo.set()


@dp.message_handler(content_types=['photo'], state=AddRecipe.photo)
async def input_photo(message: Message, state: FSMContext):
    await message.answer("Рецепт добавлен! 😌")
    async with state.proxy() as data:
        data['photo'] = message.photo[-1].file_id
        new_recipe = Recipe(data['name'], data['ingredients'], data['category'], data['description'], data['photo'])
        print(new_recipe)
        session.add(new_recipe)
        session.commit()
    await state.finish()


@dp.message_handler(content_types=['text'], state=AddRecipe.photo)
async def input_photo(message: Message, state: FSMContext):
    await message.answer("Это не фотография 😔")
