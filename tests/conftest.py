import pytest

from game.controller.systems import SystemProperty
from game.model.bullet import Bullet
from game.model.character import Character, Trump
from game.model.properties import Resolution, Border, ScreenBorder, Color
from game.model.shapes import Shape, Rectangle
from tests.fake import FakeScreenImages


@pytest.fixture(scope="module")
def bullet() -> Bullet:
    return Bullet(position=(300, 300), radius=5, color=(0, 0, 0), facing=10)


@pytest.fixture(scope="module")
def trump() -> Character:
    return Trump(is_left=True, is_right=True)


@pytest.fixture(scope="module")
def resolution() -> Resolution:
    return Resolution(resolution=(10, 20))


@pytest.fixture(scope="module")
def screen_border(resolution: Resolution) -> Border:
    return ScreenBorder(resolution)


@pytest.fixture(scope="module")
def rectangle() -> Shape:
    return Rectangle(color=(0, 0, 0), location=(0, 0, 0))


@pytest.fixture(scope="module")
def color() -> Color:
    return Color(red=1, green=2, blue=3)


@pytest.fixture(scope="module")
def system_property(trump: Character) -> SystemProperty:
    return SystemProperty(FakeScreenImages(), trump)
