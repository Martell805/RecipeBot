from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

from general import dp, session, bot
from models.Recipe import Recipe


class FindRecipe(StatesGroup):
    name = State()


@dp.callback_query_handler(text="find_recipe")
async def find_recipe(call: CallbackQuery):
    """
    Function which answers "/find" and shows requester recipe from database to user
    :param call: Callback from TG
    :return: None
    """
    await call.message.answer(text='Введите название рецепта 👨🏻‍🍳')
    await FindRecipe.name.set()


@dp.message_handler(state=FindRecipe.name)
async def input_name(message: Message, state: FSMContext):
    result = session.query(Recipe).filter(Recipe.name == message.text).first()
    await state.finish()

    if not result:
        await message.answer("Рецепт с таким название не найден😣")
        return

    keyboard = InlineKeyboardMarkup(one_time_keyboard=True).row(
        InlineKeyboardButton(text="👍🏻", callback_data="upvote " + str(result.id)),
        InlineKeyboardButton(text="👎🏻", callback_data="downvote " + str(result.id)),
        InlineKeyboardButton(text="🌟", callback_data="favourite " + str(result.id)),
        InlineKeyboardButton(text="🚫", callback_data="avoid " + str(result.id)),
    )

    await bot.send_photo(message.chat.id, result.get_photo_id(), caption=result, reply_markup=keyboard)
