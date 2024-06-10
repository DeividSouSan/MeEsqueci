from tinydb import Query, TinyDB

from src.entities.category import Category


class CategoryRepository:
    def __init__(self):
        self.db = TinyDB("db.json")

    def add_category(self, category: Category) -> None:
        self.db.insert(category)

    def get_all_categories(self) -> list[Category]:
        return self.db.all()
