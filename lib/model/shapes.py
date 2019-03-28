from abc import ABC, abstractmethod
from typing import Tuple
from pygame.draw import rect
from lib.model.visual import Display


class Shape(ABC):
    """The class represents abstract shape interface."""

    @property
    @abstractmethod
    def location(self) -> None:
        """Defines shape location."""
        pass

    @abstractmethod
    def draw(self) -> None:
        """Draws an abstract shape."""
        pass


class Rectangle(Shape):
    """The class represents rectangle shape."""

    def __init__(
        self, window: Display, color: Tuple[int, ...], location: Tuple[int, ...]
    ) -> None:
        self._window = window.set_resolution()
        self._color = color
        self._location = location

    def draw(self) -> None:
        rect(self._window.parent, self._color, self._location)

    @property
    def location(self) -> Tuple[int, ...]:
        return self._location

    @location.setter
    def location(self, location: Tuple[int, ...]) -> None:
        if isinstance(location, tuple):
            self._location = location
