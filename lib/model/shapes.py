from abc import ABC, abstractmethod
from typing import Tuple
from pygame.draw import rect, circle
from lib.model.visual import Window


class Shape(ABC):
    """The class represents abstract shape interface."""

    @property
    @abstractmethod
    def location(self) -> None:
        """Defines shape location."""
        pass

    @abstractmethod
    def draw(self, window: Window) -> None:
        """Draws an abstract shape."""
        pass


class Rectangle(Shape):
    """The class represents rectangle shape."""

    def __init__(self, color: Tuple[int, ...], location: Tuple[int, ...]) -> None:
        self._color = color
        self._location = location

    def draw(self, window: Window) -> None:
        rect(window.parent, self._color, self._location)

    @property
    def location(self) -> Tuple[int, ...]:
        return self._location

    @location.setter
    def location(self, location: Tuple[int, ...]) -> None:
        if isinstance(location, tuple):
            self._location = location


class Circle(Shape):
    def __init__(
        self, color: Tuple[int, ...], location: Tuple[int, ...], radius: int
    ) -> None:
        self._color = color
        self._location = location
        self._radius = radius

    def draw(self, window: Window) -> None:
        circle(window.parent, self._color, self._location, self._radius)

    @property
    def location(self) -> Tuple[int, ...]:
        return self._location

    @location.setter
    def location(self, location: Tuple[int, ...]) -> None:
        if isinstance(location, tuple):
            self._location = location
