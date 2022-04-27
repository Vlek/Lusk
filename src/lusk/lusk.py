"""The Lusk game object."""
import asyncio

from . import EventLoop
from lusk.map import Map


class Lusk:
    """The main game object that holds state for the game."""

    def __init__(self, config: str) -> None:
        """Instantiate the game object."""
        self.confg: str | None = config
        self.map: Map = Map([])

        self.eventloop: EventLoop = EventLoop()

    def play(self) -> None:
        """Starts the main game event loop."""
        asyncio.run(self.eventloop.start_loop())
