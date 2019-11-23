from typing import Tuple, List
from pygame import Surface

from game.model.images import ScreenImages
from game.model.properties import Resolution
from game.model.visual import Display, Window


class FakeWindow(Window):
    """Represents fake window."""

    def parent(self) -> Surface:
        pass

    def fill(self, color: Tuple[int, ...]) -> None:
        pass

    def blit(self, source: Surface, area: Tuple[int, int]) -> None:
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


class FakeScreenImages(ScreenImages):
    """Represents fake screen images display."""

    def load_back_ground(self) -> Surface:
        pass

    def load_stand(self) -> Surface:
        pass

    def load_left_side(self) -> List[Surface]:
        pass

    def load_right_side(self) -> List[Surface]:
        pass
