"""Command-line interface."""
import click

from lusk import lusk


@click.command()
@click.version_option()
def main() -> None:
    """Lusk."""
    game = lusk()

    print(game)


if __name__ == "__main__":
    main(prog_name="lusk")  # pragma: no cover
