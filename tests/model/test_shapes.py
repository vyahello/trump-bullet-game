from typing import Tuple
import pytest
from lib.model.shapes import Shape, Rectangle
from tests.fake import FakeDisplay

_color: Tuple[int, ...] = (0, 0, 0)
_resolution: Tuple[int, ...] = (0, 0, 0)
_location: Tuple[int, ...] = (0, 0, 0)
_new_location: Tuple[int, ...] = (1, 1, 1)
_title: str = "title"


@pytest.fixture(scope="module")
def rectangle() -> Shape:
    return Rectangle(FakeDisplay(_resolution, _title), _color, _location)


def test_get_rectangle_location(rectangle: Shape) -> None:
    assert rectangle.location == _location


def test_set_rectangle_location(rectangle: Shape) -> None:
    rectangle.location = _new_location
    assert rectangle.location == _new_location
