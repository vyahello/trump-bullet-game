import pytest
from lib.model.character import Character, Trump
from lib.model.properties import PropertyError


@pytest.fixture(scope='module')
def trump() -> Character:
    return Trump(is_left=True, is_right=True)


def test_is_move_left(trump: Character) -> None:
    assert trump.is_move_left


def test_is_move_right(trump: Character) -> None:
    assert trump.is_move_right


def test_animation_count(trump: Character) -> None:
    assert trump.animation_count == 0


def test_set_is_move_left(trump: Character) -> None:
    trump.is_move_left = False
    assert not trump.is_move_left


def test_set_is_move_right(trump: Character) -> None:
    trump.is_move_right = False
    assert not trump.is_move_right


def test_set_animation_count(trump: Character) -> None:
    trump.animation_count = 1
    assert trump.animation_count == 1


def test_error_is_move_left(trump: Character) -> None:
    with pytest.raises(PropertyError):
        trump.is_move_left = None


def test_error_is_move_right(trump: Character) -> None:
    with pytest.raises(PropertyError):
        trump.is_move_right = None


def test_error_animation_count(trump: Character) -> None:
    with pytest.raises(PropertyError):
        trump.animation_count = None
