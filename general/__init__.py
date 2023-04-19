import sqlalchemy.orm
from aiogram import Bot, Dispatcher

import sqlalchemy.orm as orm
import sqlalchemy.ext.declarative as dec

from config import TOKEN, DB_FILE

from .Context import Context

SqlAlchemyBase = dec.declarative_base()


bot = Bot(token=TOKEN)
dp: Dispatcher = Dispatcher(bot)
context: Context = Context()

conn_str = f'sqlite:///{DB_FILE}?check_same_thread=False'

engine = sqlalchemy.create_engine(conn_str, echo=False)
factory = orm.sessionmaker(bind=engine)

SqlAlchemyBase.metadata.create_all(engine)

session: sqlalchemy.orm.Session = factory()
