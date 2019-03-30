import pytest
from lib import PropertyError
from lib.model.bullet import Bullet


def test_bullet_velocity(bullet: Bullet) -> None:
    assert bullet.velocity() == 80


def test_bullet_axi_x(bullet: Bullet) -> None:
    assert bullet.axi_x == 300


def test_bullet_axi_y(bullet: Bullet) -> None:
    assert bullet.axi_y == 300


def test_set_bullet_axi_x(bullet: Bullet) -> None:
    bullet.axi_x = 100
    assert bullet.axi_x == 100


def test_set_bullet_axi_y(bullet: Bullet) -> None:
    bullet.axi_y = 100
    assert bullet.axi_y == 100


def test_set_error_bullet_axi_x(bullet: Bullet) -> None:
    with pytest.raises(PropertyError):
        bullet.axi_x = None


def test_set_error_bullet_axi_y(bullet: Bullet) -> None:
    with pytest.raises(PropertyError):
        bullet.axi_y = None
