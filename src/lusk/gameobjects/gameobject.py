"""The base game object for the game.

This object will be the base that will be used for everything in the
game aside from the map and any effects. This will allow us to both
keep our types in good order as well as make sure we're DRY when
adding methods and properties.
"""


class GameObject:
    """Base object type used for items and mobiles."""

    def __init__(self, name: str = "", x: int = 0, y: int = 0) -> None:
        """Initialize a base game object."""
        # What the item's display name is
        self.name = name

        # Coordinates
        self.x = x
        self.y = y

    def __str__(self) -> str:
        """Return the string representation of the object."""
        return f"x{self.x}y{self.y}: {self.name}"
