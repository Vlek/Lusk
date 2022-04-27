"""Game objects."""
from typing import Tuple

from .gameobject import GameObject as GameObject
from .mobile import Mobile as Mobile

__all__: Tuple[str, ...] = (
    "GameObject",
    "Mobile",
)
