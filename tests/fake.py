from typing import Tuple
from pygame import Surface
from lib.model.properties import Resolution
from lib.model.visual import Display, Window


class FakeWindow(Window):
    """Represents fake window."""

    def parent(self) -> Surface:
        pass

    def fill(self, color: Tuple[int, ...]) -> None:
        pass


class FakeDisplay(Display):
    """Represents fake window display."""

    def __init__(self, resolution: Tuple[int, ...], title: str) -> None:
        self._resolution = resolution
        self._title = title

    @property
    def resolution(self) -> Resolution:
        return Resolution(self._resolution)

    def set_resolution(self) -> Window:
        return FakeWindow()

    def set_title(self) -> None:
        pass

    def update(self) -> None:
        pass
