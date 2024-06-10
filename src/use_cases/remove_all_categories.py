from src.repositories.category_repository import CategoryRepository


class RemoveAllCategories:
    def __init__(self, repository: CategoryRepository):
        self.repository = repository

    def execute(self) -> None:
        self.repository.remove_all_categories()
