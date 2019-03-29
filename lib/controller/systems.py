from abc import ABC, abstractmethod
from lib.controller.engines import Engine
from lib.model.character import Trump
from lib.model.images import ScreenImages, GameImages
from lib.model.navigation import Navigation
from lib.model.properties import GameProperty, ScreenBorder, Border
from lib.model.visual import Display, Window, Clock


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
        character: Trump,
    ) -> None:
        self._engine: Engine = engine
        self._display: Display = display
        self._images: ScreenImages = images
        self._character: Trump = character
        self._window: Window = display.set_resolution()
        self._border: Border = ScreenBorder(self._display.resolution)
        self._clock = Clock(frames=30)
        self._is_run: bool = True

    def start(self) -> None:
        while self._is_run:
            self._engine.set_delay()
            self._navigate_player()
            self._draw_window()

    def stop(self) -> None:
        self._engine.quit()

    def _draw_window(self):
        """Draws a window on a screen."""
        self._window.blit(self._images.load_back_ground(), area=(0, 0))
        if self._character.animation_count + 1 >= 30:
            self._character.animation_count = 0
        if self._character.is_move_left:
            self._window.blit(
                self._images.load_left_side()[self._character.animation_count // 5],
                (GameProperty.axi_x, GameProperty.axi_y),
            )
            self._character.animation_count += 1
        elif self._character.is_move_right:
            self._window.blit(
                self._images.load_right_side()[self._character.animation_count // 5],
                (GameProperty.axi_x, GameProperty.axi_y),
            )
            self._character.animation_count += 1
        else:
            self._window.blit(
                self._images.load_stand(), (GameProperty.axi_x, GameProperty.axi_y)
            )
        self._display.update()

    def _navigate_player(self) -> None:
        """Performs navigation process of a player."""
        self._clock.tick()
        for event in Navigation.events():
            if Navigation.is_quit(event):
                self._is_run = False

        if Navigation.is_left() and self._border.is_top_left(GameProperty.axi_x):
            GameProperty.axi_x -= GameProperty.speed
            self._character.is_move_left = True
            self._character.is_move_right = False
        elif Navigation.is_right() and self._border.is_top_right(
            GameProperty.axi_x, GameProperty.width
        ):
            GameProperty.axi_x += GameProperty.speed
            self._character.is_move_left = False
            self._character.is_move_right = True
        else:
            self._character.is_move_left = False
            self._character.is_move_right = False
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
            engine, display, GameImages(initial_path="lib/images/"), Trump()
        )

    def start(self) -> None:
        self._engine.initialize()
        self._display.set_title()
        self._system.start()

    def stop(self) -> None:
        self._system.stop()
