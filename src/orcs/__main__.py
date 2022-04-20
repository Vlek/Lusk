"""Command-line interface."""
import click


@click.command()
@click.version_option()
def main() -> None:
    """Orcs."""


if __name__ == "__main__":
    main(prog_name="orcs")  # pragma: no cover
