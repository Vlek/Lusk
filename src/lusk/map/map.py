"""Map object to hold map data and return map info."""


class Map:
    """Holds map information and returns map info."""

    def __init__(self, tiles: list[list[int]]) -> None:
        """Instantiate a map object."""
        self.tiles = tiles

        if self.tiles is None:
            self.tiles = []
