from enum import Enum


class ItemEnum(Enum):
    GOT = 1
    GOT_BUT_NOT_SAFE = 2
    NOT_GOT = 3
    NO_NEED = 4


class Item:
    def __init__(self, name: str, category: str, status: int):
        self.name: str = name
        self.category: str = category
        self.status: int = status

    @property
    def status(self) -> int:
        return self.status

    @status.setter
    def status(self, status: int) -> None:
        if status in ItemEnum:
            self.status = status

        raise Exception("Invalid Status.")
