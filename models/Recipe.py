from sqlalchemy import Column, Integer, String
from sqlalchemy_serializer import SerializerMixin

from general import SqlAlchemyBase


class Recipe(SqlAlchemyBase, SerializerMixin):
    """
    Recipe DTO and entity
    """
    __tablename__ = "recipe"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    name = Column("name", String)
    ingredients = Column("ingredients", String)
    categories = Column("categories", String)
    description = Column("description", String)
    thumbs_up = Column("thumbs_up", Integer, default=0)
    thumbs_down = Column("thumbs_down", Integer, default=0)

    def __init__(self, name: str = "", ingredients: str = "", categories: str = "",
                 description: str = "", thumbs_up: int = 0, thumbs_down: int = 0):
        self.name = name
        self.ingredients = ingredients
        self.categories = categories
        self.description = description
        self.thumbs_up = thumbs_up
        self.thumbs_down = thumbs_down

    def get_id(self) -> int:
        return self.id

    def get_name(self) -> str:
        return self.name

    def get_ingredients(self) -> str:
        return self.ingredients

    def get_categories(self) -> str:
        return self.categories

    def get_description(self) -> str:
        return self.description

    def get_thumbs_up(self) -> int:
        return self.thumbs_up

    def get_thumbs_down(self) -> int:
        return self.thumbs_down

    def set_name(self, name: str) -> "Recipe":
        self.name = name
        return self

    def set_ingredients(self, ingredients: str) -> "Recipe":
        self.ingredients = ingredients
        return self

    def set_categories(self, categories: str) -> "Recipe":
        self.categories = categories
        return self

    def set_description(self, description: str) -> "Recipe":
        self.description = description
        return self

    def inc_rating(self) -> None:
        self.thumbs_up += 1

    def dec_rating(self) -> None:
        self.thumbs_down += 1

    def __repr__(self) -> str:
        return str(self)

    def __str__(self) -> str:
        return f'{self.get_name()} {self.get_thumbs_up()}👍🏻 {self.get_thumbs_down()}👎🏻 ' \
               f'\n\n{self.get_categories()} \n\n{self.get_ingredients()} ' \
               f' \n\n{self.get_description()}'
