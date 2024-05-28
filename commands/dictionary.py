import requests
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import Message, CallbackQuery

from general import dp

from googletrans import Translator

class FindWord(StatesGroup):
    name = State()


def get_dictionary_definition(word):
    translator = Translator()
    eng_word = translator.translate(word).text

    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{eng_word}"
    response = requests.get(url)
    data = response.json()

    if 'title' in data: return None

    defi_eng = data[0]['meanings'][0]['definitions'][0]['definition']

    translator = Translator()
    return translator.translate(defi_eng, dest='ru').text


@dp.callback_query_handler(text="word")
async def find_word(call: CallbackQuery):
    """
    Function which answers callback "word" and shows requester meaning of written word
    :param call: Callback from TG
    :return: None
    """
    await call.message.answer(text='Введите слово📖')
    await FindWord.name.set()


@dp.message_handler(state=FindWord.name)
async def input_name(message: Message, state: FSMContext):
    word: str = message.text

    result = get_dictionary_definition(word)

    if result:
        answer = f"{word.capitalize()}:\n" + result
    else:
        answer = f"Значение слова \"{word.capitalize()}\" найти не удалось🔍"

    await state.finish()
    await message.answer(answer)
