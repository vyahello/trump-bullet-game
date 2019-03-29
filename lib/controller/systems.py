from abc import ABC, abstractmethod
from lib.controller.engines import Engine, GameEngine
from lib.model.character import Character
from lib.model.images import GameImages
from lib.model.navigation import Navigation
from lib.model.properties import GameProperty, ScreenBorder, Border
from lib.model.shapes import Shape
from lib.model.visual import Display, Window, tick


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


class PySystem(System):
    """Represents concrete system."""

    def __init__(self, display: Display, shape: Shape) -> None:
        self._engine: Engine = GameEngine(delay=50)
        self._display: Display = display
        self._border: Border = ScreenBorder(self._display.resolution)
        self._window: Window = display.set_resolution()
        self._shape: Shape = shape
        self._is_run: bool = True
        self._images: GameImages = GameImages("lib/images/")
        self._character = Character()

    def start(self) -> None:
        self._engine.initialize()
        self._display.set_title()

        while self._is_run:
            self._run()

    def stop(self) -> None:
        self._engine.quit()

    def _run(self) -> None:
        """Game runner proxy."""
        self._engine.set_delay()
        self._navigate_player()
        self._draw_window()

    def _draw_window(self):
        self._window.blit(self._images.load_back_ground(), area=(0, 0))
        if self._character.anim_count + 1 >= 30:
            self._character.anim_count = 0
        if self._character.is_move_left:
            self._window.blit(
                self._images.load_left_side()[self._character.anim_count // 5],
                (GameProperty.axi_x, GameProperty.axi_y),
            )
            self._character.anim_count += 1
        elif self._character.is_move_right:
            self._window.blit(
                self._images.load_right_side()[self._character.anim_count // 5],
                (GameProperty.axi_x, GameProperty.axi_y),
            )
            self._character.anim_count += 1
        else:
            self._window.blit(
                self._images.load_stand(), (GameProperty.axi_x, GameProperty.axi_y)
            )
        self._shape.draw()
        self._shape.location = GameProperty.coordinates()
        self._display.update()

    def _navigate_player(self) -> None:
        """Performs navigation process of a player."""
        tick(frames=30)
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
