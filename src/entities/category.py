from src.entities.item import Item


class Category:
    name: str
    items: list[Item]

    def __init__(self, name: str):
        self.name: str = name
        self.items: list[Item] = []

    def __str__(self):
        return f"Category: {self.name} - Items: {self.items}"
