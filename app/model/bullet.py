from typing import Tuple
from app import PropertyError
from app.model.shapes import Circle
from app.model.visual import Window


class Bullet:
    """The class represents a bullet."""

    def __init__(
        self,
        position: Tuple[int, ...],
        radius: int,
        color: Tuple[int, ...],
        facing: int,
    ) -> None:
        self._circle = Circle(color, position, radius)
        self._axi_x = position[0]
        self._axi_y = position[1]
        self._facing = facing
        self._velocity = 8 * facing

    def velocity(self) -> int:
        """Speed of a bullet,"""
        return self._velocity

    @property
    def axi_x(self) -> int:
        """X coordinate of a bullet."""
        return self._axi_x

    @property
    def axi_y(self) -> int:
        """Y coordinate of a bullet."""
        return self._axi_y

    @axi_x.setter
    def axi_x(self, axi_x: int):
        """Sets X coordinate of a bullet."""
        if not isinstance(axi_x, int):
            raise PropertyError(f"{axi_x} value is not valid!")
        self._axi_x = axi_x

    @axi_y.setter
    def axi_y(self, axi_y: int):
        """Sets Y coordinate of a bullet."""
        if not isinstance(axi_y, int):
            raise PropertyError(f"{axi_y} value is not valid!")
        self._axi_y = axi_y

    def draw(self, window: Window) -> None:
        """Draws a bullet."""
        self._circle.draw(window)
