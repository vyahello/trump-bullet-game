import pytest
from lib.model.navigation import Navigation


def test_count_navigation_options() -> None:
    assert len(Navigation) == 5


def test_navigation_option() -> None:
    for option in Navigation:
        assert isinstance(option, Navigation)


@pytest.mark.parametrize("option", [
    Navigation.up,
    Navigation.down,
    Navigation.left,
    Navigation.right,
    Navigation.quit,
])
def test_contains_navigation(option: Navigation) -> None:
    assert option in Navigation
