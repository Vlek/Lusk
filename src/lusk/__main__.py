"""Command-line interface."""
import click


@click.command()
@click.version_option()
def main() -> None:
    """Lusk."""


if __name__ == "__main__":
    main(prog_name="lusk")  # pragma: no cover
