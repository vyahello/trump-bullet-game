from abc import ABC, abstractmethod
from lib.engines import GameEngine
from lib.properties import GameProperties
from lib.systems import PySystem
from lib.visual import GameDisplay, Display
from lib.shapes import Rectangle


class Game(ABC):
    """Represents game abstraction."""

    @abstractmethod
    def run(self) -> None:
        """Runs a game."""
        pass


class PyGame(Game):
    """Represents concrete game."""

    def __init__(self, name: str) -> None:
        display: Display = GameDisplay(
            resolution=(500, 500),
            title=name
        )
        self._system = PySystem(
            GameEngine(delay=100),
            display,
            Rectangle(
                display,
                color=(0, 0, 255),
                location=GameProperties.coordinates()
            )
        )

    def run(self) -> None:
        self._system.start()
        self._system.stop()

