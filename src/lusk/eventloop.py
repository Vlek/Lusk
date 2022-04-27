"""Main game event loop.

The game loop is the event loop that is able to take input from the
user, draw things on screen, perform game logic, and process any
network calls within a timeframe that will allow for there to be
no perceiveable lag.

This loop is templates off of the one given in an article written
about trying to create a better pygame event loop than the main
ones that are given. This is supposed to be able to better handle
events using async functionality as opposed to the ones that
throttle the CPU and cause tearing.

https://glyph.twistedmatrix.com/2022/02/a-better-pygame-mainloop.html
"""
import asyncio
import time
from math import inf

from pygame import Event
from pygame import image
from pygame.constants import SCALED
from pygame.display import flip
from pygame.display import set_mode
from pygame.event import get
from pygame.surface import Surface

from . import EventHandler

event_handler = EventHandler()


async def pygame_loop(framerate_limit: float = inf) -> None:
    """Acts as the main game event loop.

    The pygame loop performs a number of functions:
        - Waits for and responds to user input.
        - Draws things to the screen.
        - Handles game logic.
        - Accepts and responds to network calls.
          This part we won't be doing just yet, it is possible in the
          future that network play will be added, but that will
          definitely be a >1.0 edition item.
    """
    loop: asyncio.AbstractEventLoop = asyncio.get_event_loop()

    screen_surface: Surface = set_mode(size=(256, 256), flags=SCALED, vsync=1)

    next_frame_target: float = 0.0
    limit_frame_duration: float = 1.0 / framerate_limit

    drawables: list[Surface] = [
        # The docs say we should use the convert method to make them draw faster.
        # convert_alpha is used on PNGs that have alpha transparency.
        image.load("./src/lusk/assets/ground.png").convert()
    ]

    while True:

        if limit_frame_duration:
            # framerate limiter
            this_frame: float = time.time()
            delay: float = next_frame_target - this_frame
            if delay > 0:
                await asyncio.sleep(delay)
            next_frame_target = this_frame + limit_frame_duration

        for drawable in drawables:
            # drawable.draw(screen_surface)
            # drawable.blit(screen_surface, (10, 10))
            screen_surface.blit(drawable, (10, 10))

        events_to_handle: list[Event] = list(get())
        events_handled: asyncio.Task[None] = loop.create_task(
            handle_events(events_to_handle)
        )

        await loop.run_in_executor(None, flip)
        # don’t want to accidentally start drawing again until events are done
        await events_handled


async def handle_events(events_to_handle: list[Event]) -> None:
    """Event queue handler function.

    Note that this must be async def even if it is not awaiting.
    """
    for event in events_to_handle:
        event_handler.handle_event(event)


asyncio.run(pygame_loop(60))
