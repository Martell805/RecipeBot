from aiogram import executor

from general import dp, SqlAlchemyBase, engine
from commands import *

SqlAlchemyBase.metadata.create_all(engine)

executor.start_polling(dp)
