from abc import ABC, abstractmethod
from lib.controller.engines import Engine, GameEngine
from lib.model.navigation import Navigation
from lib.model.properties import GameProperty, ScreenBorder, Border, Color
from lib.model.shapes import Shape
from lib.model.visual import Display, Window


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
        self._color: Color = Color(red=0, green=0, blue=0)

    def start(self) -> None:
        self._engine.initialize()
        self._display.set_title()

        while self._is_run:
            self._run()

    def stop(self) -> None:
        self._engine.quit()

    def _navigate_player(self) -> None:
        """Performs navigation process of a player."""
        for event in Navigation.events():
            if Navigation.is_quit(event):
                self._is_run = False

        if Navigation.is_left() and self._border.is_top_left(GameProperty.axi_x):
            GameProperty.axi_x -= GameProperty.speed
        if Navigation.is_right() and self._border.is_top_right(GameProperty.axi_x, GameProperty.width):
            GameProperty.axi_x += GameProperty.speed
        if not GameProperty.is_jump:
            if Navigation.is_up() and self._border.is_top_upper(GameProperty.axi_y):
                GameProperty.axi_y -= GameProperty.speed
            if Navigation.is_down() and self._border.is_top_lower(GameProperty.axi_y, GameProperty.height):
                GameProperty.axi_y += GameProperty.speed
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

    def _run(self) -> None:
        """Game runner proxy."""
        self._engine.set_delay()
        self._navigate_player()
        self._window.fill(self._color.as_rgba())
        self._shape.draw()
        self._shape.location = GameProperty.coordinates()
        self._display.update()
