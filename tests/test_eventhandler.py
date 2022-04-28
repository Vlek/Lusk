"""Test the event handler code."""
from lusk import EventHandler


def test_instantiation() -> None:
    """Test that we can instantiate a new eventhandler object."""
    eh: EventHandler = EventHandler()

    print(eh)
