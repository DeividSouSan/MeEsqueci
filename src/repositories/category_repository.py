from tinydb import Query, TinyDB

from src.entities.category import Category


class CategoryRepository:
    def __init__(self):
        self.db = TinyDB("db.json")

    def get_all_categories(self) -> list[Category]:
        """
        Get all categories from the database.

        Returns:
            list[Category]: A list of all categories objects (Category) in the database.
        """
        return self.db.all()

    def add_category(self, category: Category) -> None:
        """
        Add a category to the database.

        Args:
            category (Category): A category object to be added to the database.
        """
        self.db.insert(category)

    def remove_all_categories(self) -> None:
        """
        Remove all categories from the database.
        """
        self.db.truncate()
