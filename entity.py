from typing import Tuple

class Entity:
    """
    A generic obeject for evrythign
    """
    def __init__(self, x: int, y: int, char: str, color : Tuple[int, int, int]):
        self.x = x
        self.y = y
        self.char = char
        self.color = color

    def move(self, dx: int, dy: int) -> None:
        # Move by amount
        self.x += dx
        self.y += dy