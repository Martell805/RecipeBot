from sqlalchemy import Column, Integer
from sqlalchemy_serializer import SerializerMixin

from general import SqlAlchemyBase
from models.Recipe import Recipe


class Favourite(SqlAlchemyBase, SerializerMixin):
    """
    Favourite DTO and entity
    """
    __tablename__ = "favourite"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    user_id = Column("user_id", Integer, default=0)
    recipe_id = Column("recipe_id", Integer, default=0)

    def __init__(self, user_id: int, recipie_id: int):
        self.user_id = user_id
        self.recipe_id = recipie_id

    def get_id(self) -> int:
        return self.id

    def get_user_id(self) -> int:
        return self.user_id

    def get_recipe_id(self) -> int:
        return self.recipe_id
