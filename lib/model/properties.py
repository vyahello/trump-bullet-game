from abc import ABC, abstractmethod
from typing import Tuple, Callable
from lib import PropertyError


class Border(ABC):
    """The class represents game border."""

    @abstractmethod
    def is_top_left(self, axi_x: int) -> bool:
        """Defines if it is a top left border."""
        pass

    @abstractmethod
    def is_top_right(self, axi_x: int, width: int) -> bool:
        """Defines if it is a top right border."""
        pass

    @abstractmethod
    def is_top_upper(self, axi_y: int) -> bool:
        """Defines if it is a top upper border."""
        pass

    @abstractmethod
    def is_top_lower(self, axi_y: int, height: int) -> bool:
        """Defines if it is a top lower border."""
        pass


class GameProperty:
    """The class represents game property."""

    axi_x: int = 50
    axi_y: int = 425
    width: int = 60
    height: int = 71
    speed: int = 5
    jump_count: int = 10
    is_jump: bool = False

    @classmethod
    def coordinates(cls) -> Tuple[int, ...]:
        """Returns game coordinates."""
        return cls.axi_x, cls.axi_y, cls.width, cls.height

    @classmethod
    def calculate_jumper(cls) -> int:
        """Calculates game jumper."""
        return cls.jump_count ** 2 / 2


class Color:
    """The class represents specific game color."""

    def __init__(self, red: int, green: int, blue: int) -> None:
        self._red = red
        self._green = green
        self._blue = blue

    def as_rgba(self) -> Tuple[int, ...]:
        """Returns RGBA color"""
        return self._red, self._green, self._blue


class Resolution:
    """The class represents specific resolution."""

    _bottom: int = 5

    def __init__(self, resolution: Tuple[int, ...]) -> None:
        def save_resolution() -> Tuple[int, ...]:
            if len(resolution) != 2:
                raise PropertyError(
                    "Resolution should contain 2 values: width and height"
                )
            return resolution

        self._resolution: Callable[[], Tuple[int, ...]] = save_resolution

    def as_sequence(self) -> Tuple[int, ...]:
        return self._resolution()

    @property
    def top_height(self) -> int:
        """Defines height parameter for a resolution.

        Returns:
            specific height
        """
        return self._resolution()[0]

    @property
    def top_width(self) -> int:
        """Defines width parameter for a resolution.

        Returns:
            specific width
        """
        return self._resolution()[1]

    @property
    def bottom(self) -> int:
        """Defines parameter for a bottom resolution.

        Returns:
            specific bottom value
        """
        return self._bottom


class ScreenBorder(Border):
    """Defined screen border for a game."""

    def __init__(self, resolution: Resolution) -> None:
        self._resolution = resolution

    def is_top_left(self, axi_x: int) -> bool:
        return axi_x > self._resolution.bottom

    def is_top_right(self, axi_x: int, width: int) -> bool:
        return axi_x < self._resolution.top_width - width - self._resolution.bottom

    def is_top_upper(self, axi_y: int) -> bool:
        return axi_y > self._resolution.bottom

    def is_top_lower(self, axi_y: int, height: int) -> bool:
        return axi_y < self._resolution.top_height - height - self._resolution.bottom
