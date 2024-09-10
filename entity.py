from typing import Tuple


class Entity:
    """
    GENERIC OBJECT TO REPRESENT PLAYERS, ENEMIES, ITEMS etc.
    """
    def __init__(self, x: int, y: int, char: str, color: Tuple[int, int, int]):
        self.x = x
        self.y = y
        self.char = char
        self.color = color

    def move(self, dx: int, dy: int) -> None:
        # MOVE THE ENTITY BY A GIVEN AMOUNT
        self.x += dx
        self.y += dy

