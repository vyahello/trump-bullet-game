from abc import ABC, abstractmethod
from typing import Tuple
from pygame import display, Surface, time
from lib.model.properties import Resolution


class Window(ABC):
    """The class represents abstract window."""

    @abstractmethod
    def parent(self) -> Surface:
        """Returns parent window."""
        pass

    @abstractmethod
    def fill(self, color: Tuple[int, ...]) -> None:
        """Fills window with color."""
        pass

    @abstractmethod
    def blit(self, source: Surface, area: Tuple[int, int]) -> None:
        """Draws source on the surface."""
        pass


class Display(ABC):
    """The class represents display abstraction."""

    @property
    @abstractmethod
    def resolution(self) -> Resolution:
        """Returns game display resolution"""
        pass

    @abstractmethod
    def set_resolution(self) -> Window:
        """Sets resolution for a game."""
        pass

    @abstractmethod
    def set_title(self) -> None:
        """Sets title for a game."""
        pass

    @abstractmethod
    def update(self) -> None:
        """Updates game display."""
        pass


class GameDisplay(Display):
    """The class represents game display."""

    def __init__(self, resolution: Tuple[int, ...], title: str) -> None:
        self._resolution = resolution
        self._title = title

    @property
    def resolution(self) -> Resolution:
        """Returns game display resolution."""
        return Resolution(self._resolution)

    def set_resolution(self) -> Window:
        """Sets resolution for a game."""
        return GameWindow(display.set_mode(self._resolution))

    def set_title(self) -> None:
        """Sets title for a game."""
        display.set_caption(self._title)

    def update(self) -> None:
        """Updates game display."""
        display.update()


class GameWindow(Window):
    """The class represents game window."""

    def __init__(self, window: Surface) -> None:
        self._win = window

    @property
    def parent(self) -> Surface:
        return self._win

    def fill(self, color: Tuple[int, ...]) -> None:
        self._win.fill(color)

    def blit(self, source: Surface, area: Tuple[int, int]) -> None:
        self._win.blit(source, area)


def tick(frames: int) -> None:
    """Ticks number of frames."""
    time.Clock().tick(frames)
