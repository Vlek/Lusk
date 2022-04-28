"""The base object class for handling anything that can move."""
from . import GameObject


class Mobile(GameObject):
    """The base class for any moving entity in the game."""

    def __init__(self, name: str, x: int, y: int) -> None:
        """Initialize a mobile object."""
        super().__init__(name, x, y)
