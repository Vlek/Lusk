"""Command-line interface."""
import click

from lusk import Lusk


@click.command()
@click.version_option()
def main() -> None:
    """Lusk."""
    game: Lusk = Lusk("")

    game.play()


if __name__ == "__main__":
    main()  # pragma: no cover
