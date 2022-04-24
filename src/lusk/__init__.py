"""Lusk."""
from typing import Tuple

from .eventhandler import EventHandler as EventHandler
from .eventloop import pygame_loop as lusk

__all__: Tuple[str, ...] = (
    "EventHandler",
    "lusk",
)
