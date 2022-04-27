"""Map object to hold map data and return map info."""


class Map:
    """Holds map information and returns map info."""

    def __init__(self, map_info: list[int]) -> None:
        """Instantiate a map object."""
        self.info = map_info

        if self.info is None:
            self.info = []
