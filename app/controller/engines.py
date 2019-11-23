from abc import ABC
import pygame


class Engine(ABC):
    """The class represents engine abstraction."""

    def initialize(self) -> None:
        """Initializes engine."""
        pass

    def quit(self) -> None:
        """Quites from engine."""
        pass

    def set_delay(self) -> None:
        """Sets delay for an engine."""
        pass


class GameEngine(Engine):
    """Represents engine for a game."""

    def __init__(self, delay: int) -> None:
        self._delay = delay

    def initialize(self) -> None:
        pygame.init()

    def quit(self) -> None:
        pygame.quit()

    def set_delay(self) -> None:
        pygame.time.delay(self._delay)
