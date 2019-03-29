from abc import ABC, abstractmethod
from typing import Tuple
from lib.controller.engines import GameEngine, Engine
from lib.model.properties import Resolution
from lib.controller.systems import UsableGameSystem
from lib.model.visual import GameDisplay


class Game(ABC):
    """Represents game abstraction."""

    @abstractmethod
    def run(self) -> None:
        """Runs a game."""
        pass


class PyGame(Game):
    """Represents concrete game."""

    def __init__(self, engine: Engine, resolution: Resolution, name: str) -> None:
        self._system = UsableGameSystem(
            engine, GameDisplay(resolution.as_sequence(), name)
        )

    def run(self) -> None:
        self._system.start()
        self._system.stop()


class TrumpBulletGame(Game):
    """Represents `Cheerful Trump Bullet Game`."""

    _resolution: Tuple[int, ...] = (500, 500)
    _name: str = "Trump Bullet Game"

    def __init__(self) -> None:
        self._game = PyGame(
            engine=GameEngine(delay=5),
            resolution=Resolution(self._resolution),
            name=self._name,
        )

    def run(self) -> None:
        self._game.run()
