from abc import ABC, abstractmethod
from typing import List
from app import PropertyError
from app.controller.engines import Engine
from app.model.bullet import Bullet
from app.model.character import Trump, Character
from app.model.images import ScreenImages, GameImages
from app.model.navigation import Navigation
from app.model.properties import (
    GameProperty,
    Color,
    Border,
    ScreenBorder,
)
from app.model.visual import Display, Window, Clock


IMAGES_PATH = "images/"


class System(ABC):
    """Represents system abstraction."""

    @abstractmethod
    def start(self) -> None:
        """Starts system."""
        pass

    @abstractmethod
    def stop(self) -> None:
        """Stops system."""
        pass


class _InternalGameSystem(System):
    """Represents concrete internal game system."""

    def __init__(
        self,
        engine: Engine,
        display: Display,
        images: ScreenImages,
        character: Character,
    ) -> None:
        self._engine: Engine = engine
        self._display: Display = display
        self._window: Window = display.set_resolution()
        self._border: Border = ScreenBorder(self._display.resolution)
        self._property = SystemProperty(images, character)

    def start(self) -> None:
        while self._property.is_run:
            self._engine.set_delay()
            self._navigate_player()
            self._draw_window()

    def stop(self) -> None:
        self._engine.quit()

    def _draw_window(self):
        """Draws a window on a screen."""
        self._window.blit(self._property.images().load_back_ground(), area=(0, 0))
        if self._property.character().animation_count + 1 >= 30:
            self._property.character().animation_count = 0
        if self._property.character().is_move_left:
            self._window.blit(
                self._property.images().load_left_side()[
                    self._property.character().animation_count // 5
                ],
                (GameProperty.axi_x, GameProperty.axi_y),
            )
            self._property.character().animation_count += 1
        elif self._property.character().is_move_right:
            self._window.blit(
                self._property.images().load_right_side()[
                    self._property.character().animation_count // 5
                ],
                (GameProperty.axi_x, GameProperty.axi_y),
            )
            self._property.character().animation_count += 1
        else:
            self._window.blit(
                self._property.images().load_stand(),
                (GameProperty.axi_x, GameProperty.axi_y),
            )

        for bullet in self._property.bullets():
            bullet.draw(self._window)

        self._display.update()

    def _navigate_player(self) -> None:
        """Performs navigation process of a player."""
        self._property.clock().tick()
        for event in Navigation.events():
            if Navigation.is_quit(event):
                self._property.is_run = False

        for bullet in self._property.bullets():
            if self._display.resolution.top_width > bullet.axi_x > 0:
                bullet.axi_x += bullet.velocity()
            else:
                self._property.bullets().pop(self._property.bullets().index(bullet))

        if Navigation.is_f():
            if self._property.last_move == "right":
                self._property.facing = 1
            else:
                self._property.facing = -1

            if len(self._property.bullets()) < 15:
                self._property.bullets().append(
                    Bullet(
                        (
                            round(GameProperty.axi_x + GameProperty.width // 2),
                            round(GameProperty.axi_y + GameProperty.height // 2),
                        ),
                        radius=5,
                        color=Color(255, 0, 0).as_rgba(),
                        facing=self._property.facing,
                    )
                )

        if Navigation.is_left() and self._border.is_top_left(GameProperty.axi_x):
            GameProperty.axi_x -= GameProperty.speed
            self._property.character().is_move_left = True
            self._property.character().is_move_right = False
            self._property.last_move = "left"

        elif Navigation.is_right() and self._border.is_top_right(
            GameProperty.axi_x, GameProperty.width
        ):
            GameProperty.axi_x += GameProperty.speed
            self._property.character().is_move_left = False
            self._property.character().is_move_right = True
            self._property.last_move = "right"
        else:
            self._property.character().is_move_left = False
            self._property.character().is_move_right = False
        if not GameProperty.is_jump:
            if Navigation.is_space():
                GameProperty.is_jump = True
        else:
            if GameProperty.jump_count >= -10:
                if GameProperty.jump_count < 0:
                    GameProperty.axi_y += GameProperty.calculate_jumper()
                else:
                    GameProperty.axi_y -= GameProperty.calculate_jumper()
                GameProperty.jump_count -= 1
            else:
                GameProperty.is_jump = False
                GameProperty.jump_count = 10


class UsableGameSystem(System):
    """Represents concrete user system."""

    def __init__(self, engine: Engine, display: Display) -> None:
        self._engine: Engine = engine
        self._display: Display = display
        self._system: System = _InternalGameSystem(
            engine, display, GameImages(initial_path=IMAGES_PATH), Trump()
        )

    def start(self) -> None:
        self._engine.initialize()
        self._display.set_title()
        self._system.start()

    def stop(self) -> None:
        self._system.stop()


class SystemProperty:
    """Represents system property."""

    def __init__(self, images: ScreenImages, character: Character) -> None:
        self._images: ScreenImages = images
        self._character: Character = character
        self._is_run: bool = True
        self._last_move: str = "right"
        self._facing: int = 0
        self._clock = Clock(frames=30)
        self._bullets: List[Bullet] = []

    def images(self) -> ScreenImages:
        return self._images

    def character(self) -> Character:
        return self._character

    def clock(self) -> Clock:
        return self._clock

    def bullets(self) -> List[Bullet]:
        return self._bullets

    @property
    def is_run(self) -> bool:
        return self._is_run

    @is_run.setter
    def is_run(self, is_run: bool) -> None:
        if not isinstance(is_run, bool):
            raise PropertyError(f"{is_run} value is not valid value to set!")
        self._is_run = is_run

    @property
    def last_move(self) -> str:
        return self._last_move

    @last_move.setter
    def last_move(self, last_move: str) -> None:
        if not isinstance(last_move, str):
            raise PropertyError(f"{last_move} value is not valid value to set!")
        self._last_move = last_move

    @property
    def facing(self) -> int:
        return self._facing

    @facing.setter
    def facing(self, facing: int) -> None:
        if not isinstance(facing, int):
            raise PropertyError(f"{facing} value is not valid value to set!")
        self._facing = facing
