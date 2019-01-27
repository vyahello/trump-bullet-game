from abc import ABC, abstractmethod
from lib.engines import Engine
from lib.navigation import Navigation
from lib.properties import GameProperties
from lib.shapes import Shape
from lib.visual import Display


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

    def __init__(self, engine: Engine, display: Display, shape: Shape) -> None:
        self._engine = engine
        self._display = display
        self._window = display.set_resolution()
        self._shape = shape
        self._is_run = True
        self._color = (0, 0, 0)

    def start(self) -> None:
        self._engine.initialize()
        self._display.set_title()

        while self._is_run:
            self._run()

    def stop(self) -> None:
        self._engine.quit()

    def _run(self) -> None:
        self._engine.set_delay()

        for event in Navigation.events():
            if Navigation.is_quit(event):
                self._is_run = False

        if Navigation.is_left():
            GameProperties.axi_x -= GameProperties.speed
        if Navigation.is_right():
            GameProperties.axi_x += GameProperties.speed
        if Navigation.is_up():
            GameProperties.axi_y -= GameProperties.speed
        if Navigation.is_down():
            GameProperties.axi_y += GameProperties.speed

        self._window.fill(self._color)
        self._shape.draw()
        self._shape.location = GameProperties.coordinates()
        self._display.update()