from enum import Enum
from typing import Tuple, Iterable
from pygame import (
    K_DOWN,
    K_UP,
    K_LEFT,
    K_RIGHT,
    QUIT,
    K_SPACE,
)
from pygame.event import Event
from pygame import key, event


class Navigation(Enum):
    """Navigation keyboards for a game."""

    down: int = K_DOWN
    up: int = K_UP
    left: int = K_LEFT
    right: int = K_RIGHT
    quit: int = QUIT
    space: int = K_SPACE

    @classmethod
    def is_down(cls) -> int:
        return cls._pressed_keys()[cls.down.value]

    @classmethod
    def is_up(cls) -> int:
        return cls._pressed_keys()[cls.up.value]

    @classmethod
    def is_left(cls) -> int:
        return cls._pressed_keys()[cls.left.value]

    @classmethod
    def is_right(cls) -> int:
        return cls._pressed_keys()[cls.right.value]

    @classmethod
    def is_quit(cls, event_: Event) -> bool:
        return event_.type == cls.quit.value

    @classmethod
    def is_space(cls) -> bool:
        return cls._pressed_keys()[cls.space.value]

    @classmethod
    def events(cls) -> Iterable[Event]:
        return event.get()

    @classmethod
    def _pressed_keys(cls) -> Tuple[int, ...]:
        return key.get_pressed()
