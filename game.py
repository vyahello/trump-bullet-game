from lib.games import Game, PyGame


def _run() -> None:
    """Runs a game."""
    game: Game = PyGame('Cube game')
    game.run()


if __name__ == '__main__':
    _run()
