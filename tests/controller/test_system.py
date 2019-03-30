import pytest
from lib import PropertyError
from lib.controller.systems import SystemProperty
from lib.model.character import Character
from lib.model.images import ScreenImages
from lib.model.visual import Clock


def test_system_images(system_property: SystemProperty) -> None:
    assert isinstance(system_property.images(), ScreenImages)


def test_system_character(system_property: SystemProperty) -> None:
    assert isinstance(system_property.character(), Character)


def test_system_clock(system_property: SystemProperty) -> None:
    assert isinstance(system_property.clock(), Clock)


def test_system_empty_bullets(system_property: SystemProperty) -> None:
    assert not system_property.bullets()


def test_system_is_run(system_property: SystemProperty) -> None:
    assert system_property.is_run is True


def test_set_system_is_run(system_property: SystemProperty) -> None:
    system_property.is_run = False
    assert system_property.is_run is False


def test_set_error_system_is_run(system_property: SystemProperty) -> None:
    with pytest.raises(PropertyError):
        system_property.is_run = None


def test_system_last_move(system_property: SystemProperty) -> None:
    assert system_property.last_move == "right"


def test_set_system_last_move(system_property: SystemProperty) -> None:
    system_property.last_move = "left"
    assert system_property.last_move == "left"


def test_set_error_system_last_move(system_property: SystemProperty) -> None:
    with pytest.raises(PropertyError):
        system_property.last_move = None
