"""Command-line interface."""
import asyncio

import click

from . import Lusk
from . import start_loop


@click.command()
@click.version_option()
def main() -> None:
    """Lusk."""
    game: Lusk = Lusk("")

    asyncio.run(start_loop(game))


if __name__ == "__main__":
    main()  # pragma: no cover
