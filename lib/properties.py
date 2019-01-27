from typing import Tuple


class GameProperties:
    """The class represents game coordinates."""
    axi_x: int = 50
    axi_y: int = 50
    width: int = 50
    height: int = 60
    speed: int = 10

    @classmethod
    def coordinates(cls) -> Tuple[int, ...]:
        """Returns game coordinates."""
        return (
            cls.axi_x,
            cls.axi_y,
            cls.width,
            cls.height,
        )
