from src.entities.category import Category
from src.repositories.category_repository import CategoryRepository


class SaveCategoriesToDatabase:
    def __init__(self, category_repository: CategoryRepository):
        self.category_repository = category_repository

    def execute(self, categories: list[Category]):
        for category in categories:
            self.category_repository.add_category(category)
