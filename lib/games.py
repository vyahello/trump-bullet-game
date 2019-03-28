from abc import ABC, abstractmethod
from typing import Tuple
from lib.model.properties import GameProperties, Resolution, Color
from lib.controller.systems import PySystem
from lib.model.visual import GameDisplay, Display
from lib.model.shapes import Rectangle


class Game(ABC):
    """Represents game abstraction."""

    @abstractmethod
    def run(self) -> None:
        """Runs a game."""
        pass


class PyGame(Game):
    """Represents concrete game."""

    def __init__(self, resolution: Resolution, color: Color, name: str) -> None:
        display: Display = GameDisplay(resolution.as_sequence(), name)
        self._system = PySystem(display, Rectangle(display, color.as_rgba(), GameProperties.coordinates()))

    def run(self) -> None:
        self._system.start()
        self._system.stop()


class CubeGame(Game):
    """Represents `Cube Game.`"""

    _resolution: Tuple[int, ...] = (500, 500)
    _color: Tuple[int, ...] = (0, 0, 255)

    def __init__(self) -> None:
        self._game = PyGame(Resolution(self._resolution), Color(*self._color), 'Cube Game')

    def run(self) -> None:
        self._game.run()
