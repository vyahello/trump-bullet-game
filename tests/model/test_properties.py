from typing import Tuple
import pytest
from game.model.properties import GameProperty, Color, Resolution, Border
from game import PropertyError

_rdba_color: Tuple[int, ...] = (1, 2, 3)
_resolution: Tuple[int, ...] = (10, 20)
_bottom: int = 5


def test_property_coordinates() -> None:
    assert len(GameProperty.coordinates()) == 4


def test_calculate_jumper() -> None:
    assert GameProperty.calculate_jumper() == 50


def test_color_as_rgba(color: Color) -> None:
    assert color.as_rgba() == _rdba_color


def test_resolution_as_sequence(resolution: Resolution) -> None:
    assert resolution.as_sequence() == _resolution


def test_resolution_top_height(resolution: Resolution) -> None:
    assert resolution.top_height == _resolution[0]


def test_resolution_top_width(resolution: Resolution) -> None:
    assert resolution.top_width == _resolution[1]


def test_resolution_bottom(resolution: Resolution) -> None:
    assert resolution.bottom == _bottom


def test_border_is_top_left(screen_border: Border) -> None:
    assert screen_border.is_top_left(10)


def test_border_is_top_right(screen_border: Border) -> None:
    assert screen_border.is_top_right(10, 2)


def test_border_is_top_upper(screen_border: Border) -> None:
    assert screen_border.is_top_upper(15)


def test_border_is_top_lower(screen_border: Border) -> None:
    assert screen_border.is_top_lower(3, -10)


def test_border_is_not_top_left(screen_border: Border) -> None:
    assert not screen_border.is_top_left(1)


def test_border_is_not_top_right(screen_border: Border) -> None:
    assert not screen_border.is_top_right(30, 3)


def test_border_is_not_top_upper(screen_border: Border) -> None:
    assert not screen_border.is_top_upper(1)


def test_border_is_not_top_lower(screen_border: Border) -> None:
    assert not screen_border.is_top_lower(15, 2)


def test_resolution_error() -> None:
    with pytest.raises(PropertyError):
        Resolution(resolution=(0, 0, 0)).as_sequence()
