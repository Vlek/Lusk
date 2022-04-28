"""Handle the state of the user during the game."""
from . import Mobile


class Character(Mobile):
    """Holds state of user's character in game."""

    def __init__(self, name: str, x: int, y: int) -> None:
        """Initialize a character object."""
        super().__init__(name, x, y)
