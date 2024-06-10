from src.entities.category import Category
from src.repositories.category_repository import CategoryRepository


class GetAllCategories:
    def __init__(self, category_repository: CategoryRepository):
        self.category_repository = category_repository

    def execute(self) -> list[Category]:
        return self.category_repository.get_all_categories()
