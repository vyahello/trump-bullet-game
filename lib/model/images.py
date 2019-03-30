from abc import ABC, abstractmethod
from typing import List, Tuple, Callable
from pygame import Surface, image


class Image(ABC):
    """Represent image abstraction."""

    @abstractmethod
    def load(self) -> Surface:
        """Load an image."""
        pass


class ScreenImages(ABC):
    """Represents images abstraction."""

    @abstractmethod
    def load_back_ground(self) -> Surface:
        """Loads back ground."""
        pass

    @abstractmethod
    def load_stand(self) -> Surface:
        """Loads stand point."""
        pass

    @abstractmethod
    def load_left_side(self) -> List[Surface]:
        """Loads left side images."""
        pass

    @abstractmethod
    def load_right_side(self) -> List[Surface]:
        """Loads right side images."""
        pass


class GameImage(Image):
    """The class represents screen image."""

    def __init__(self, image_path: str) -> None:
        self._image = image_path

    def load(self) -> Surface:
        return image.load(self._image)


class GameImages(ScreenImages):
    """Represents game images."""

    def __init__(self, initial_path: str) -> None:
        self._bg: GameImage = GameImage(f"{initial_path}pygame_bg.jpg")
        self._stand: GameImage = GameImage(f"{initial_path}pygame_idle.png")
        self._left: Callable[[], Tuple[GameImage, ...]] = lambda: tuple(
            map(lambda n: GameImage(f"{initial_path}pygame_left_{n}.png"), range(1, 7))
        )
        self._right: Callable[[], Tuple[GameImage, ...]] = lambda: tuple(
            map(lambda n: GameImage(f"{initial_path}pygame_right_{n}.png"), range(1, 7))
        )

    def load_back_ground(self) -> Surface:
        return self._bg.load()

    def load_stand(self) -> Surface:
        return self._stand.load()

    def load_left_side(self) -> List[Surface]:
        return list(map(lambda image_item: image_item.load(), self._left()))

    def load_right_side(self) -> List[Surface]:
        return list(map(lambda image_item: image_item.load(), self._right()))
