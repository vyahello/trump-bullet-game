from abc import ABC, abstractmethod
from typing import Tuple


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


class GameProperties:
    """The class represents game coordinates."""
    axi_x: int = 50
    axi_y: int = 50
    width: int = 50
    height: int = 60
    speed: int = 10

    @classmethod
    def coordinates(cls) -> Tuple[int, ...]:
        """Returns game coordinates."""
        return (
            cls.axi_x,
            cls.axi_y,
            cls.width,
            cls.height,
        )


class Resolution:
    """The class represents specific resolution."""

    _bottom: int = 5

    def __init__(self, resolution: Tuple[int, ...]) -> None:
        self._height: int = resolution[0]
        self._width: int = resolution[1]

    @property
    def top_height(self) -> int:
        """Defines height parameter for a resolution.

        Returns:
            specific height
        """
        return self._height

    @property
    def top_width(self) -> int:
        """Defines width parameter for a resolution.

        Returns:
            specific width
        """
        return self._width

    @property
    def bottom_height(self) -> int:
        """Defines width parameter for a resolution.

        Returns:
            specific width
        """
        return self._bottom

    @property
    def bottom_width(self) -> int:
        """Defines width parameter for a resolution.

        Returns:
            specific width
        """
        return self._bottom


class ScreenBorder(Border):
    """Defined screen border for a game."""

    def __init__(self, resolution: Resolution) -> None:
        self._resolution = resolution

    def is_top_left(self, axi_x: int) -> bool:
        return axi_x > self._resolution.bottom_width

    def is_top_right(self, axi_x: int, width: int) -> bool:
        return axi_x < self._resolution.top_width - width

    def is_top_upper(self, axi_y: int) -> bool:
        return axi_y > self._resolution.bottom_height

    def is_top_lower(self, axi_y: int, height: int) -> bool:
        return axi_y < self._resolution.top_height - height
