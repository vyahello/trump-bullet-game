from lib.model.properties import PropertyError


class Character:
    """The class represents user property."""

    def __init__(self, is_left: bool = False, is_right: bool = False) -> None:
        self._is_left = is_left
        self._is_right = is_right
        self._anim_count: int = 0

    @property
    def is_move_left(self) -> bool:
        return self._is_left

    @property
    def is_move_right(self) -> bool:
        return self._is_right

    @property
    def anim_count(self) -> int:
        return self._anim_count

    @anim_count.setter
    def anim_count(self, count: int) -> None:
        if not isinstance(count, int):
            raise PropertyError(f'Cannot set animation attribute as {count} count value is not valid!')
        self._anim_count = count

    @is_move_left.setter
    def is_move_left(self, direction: bool) -> None:
        if not isinstance(direction, bool):
            raise PropertyError(f'Cannot set left attribute as {direction} direction is not valid!')
        self._is_left = direction

    @is_move_right.setter
    def is_move_right(self, direction: bool) -> None:
        if not isinstance(direction, bool):
            raise PropertyError(f'Cannot set right attribute as {direction} direction is not valid!')
        self._is_right = direction
