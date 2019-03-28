from lib.games import Game, CubeGame


def _run() -> None:
    """Runs a game."""
    game: Game = CubeGame()
    game.run()


if __name__ == '__main__':
    _run()
