from sqlalchemy import Column, Integer, String
from sqlalchemy_serializer import SerializerMixin

from general import SqlAlchemyBase


class Recipe(SqlAlchemyBase, SerializerMixin):
    __tablename__ = "recipe"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    name = Column("name", String)
    ingredients = Column("ingredients", String)
    categories = Column("categories", String)

    def __init__(self, name: str = "", ingredients: str = "", categories: str = ""):
        self.name = name
        self.ingredients = ingredients
        self.categories = categories

    def get_id(self) -> int:
        return self.id

    def get_name(self) -> str:
        return self.name

    def get_ingredients(self) -> str:
        return self.ingredients

    def get_categories(self) -> str:
        return self.categories

    def set_name(self, name: str) -> "Recipe":
        self.name = name

        return self

    def set_ingredients(self, ingredients: str) -> "Recipe":
        self.ingredients = ingredients

        return self

    def set_categories(self, categories: str) -> "Recipe":
        self.categories = categories

        return self

    def __repr__(self) -> str:
        return str(self)

    def __str__(self) -> str:
        return f'{self.get_id()}. {self.get_name()} \n{self.get_categories()} \n{self.get_categories()}'
