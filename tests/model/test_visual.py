from typing import Tuple
from lib.model.properties import Resolution
from lib.model.visual import GameDisplay


_resolution: Tuple[int, ...] = (500, 500)
_title: str = 'title'


def test_display_resolution() -> None:
    assert isinstance(GameDisplay(_resolution, _title).resolution, Resolution)
