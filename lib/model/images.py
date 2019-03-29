from typing import List, Tuple
from pygame import Surface, image


class Image:
    """The class represents screen image."""

    def __init__(self, image_path: str) -> None:
        self._image = image_path

    def load(self) -> Surface:
        return image.load(self._image)


class GameImages:
    """Represents game images."""
    def __init__(self, initial_path: str) -> None:
        self._bg: Image = Image(f'{initial_path}pygame_bg.jpg')
        self._stand: Image = Image(f'{initial_path}pygame_idle.png')
        self._left: Tuple[Image, ...] = tuple(map(lambda n: Image(f'{initial_path}pygame_left_{n}.png'), range(1, 7)))
        self._right: Tuple[Image, ...] = tuple(map(lambda n: Image(f'{initial_path}pygame_right_{n}.png'), range(1, 7)))

    def load_back_ground(self) -> Surface:
        return self._bg.load()

    def load_stand(self) -> Surface:
        return self._stand.load()

    def load_left_side(self) -> List[Surface]:
        return list(map(lambda image_item: image_item.load(), self._left))

    def load_right_side(self) -> List[Surface]:
        return list(map(lambda image_item: image_item.load(), self._right))


