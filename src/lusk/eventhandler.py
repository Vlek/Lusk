"""Handle events within the game loop.

This handler class exists to receive and handle all of the
information that is passed to it within the context of the
game.

Events:
    - Player input
"""
from sys import exit

import pygame
from pygame.event import EventType


class EventHandler:
    """Handles events that happen within the game context."""

    def handle_event(self, event: EventType) -> None:
        """Takes an individual event object and handles accordingly.

        Currently this is just going through a glorified switch statement
        but in the future this should have a more robust setup that will
        allow for scene switching (like changing buttons from the main
        menu to the in-game button mapping as well as re-mapping)

        This needs to be an async def because the calling function
        is async and will expect it.
        """
        print(event)

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_q:
                print("Quiting the game!")

                exit("Quitting the game!")
