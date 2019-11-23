from typing import Tuple
from game.model.shapes import Shape

_color: Tuple[int, ...] = (0, 0, 0)
_resolution: Tuple[int, ...] = (0, 0, 0)
_location: Tuple[int, ...] = (0, 0, 0)
_new_location: Tuple[int, ...] = (1, 1, 1)
_title: str = "title"


def test_get_rectangle_location(rectangle: Shape) -> None:
    assert rectangle.location == _location


def test_set_rectangle_location(rectangle: Shape) -> None:
    rectangle.location = _new_location
    assert rectangle.location == _new_location
