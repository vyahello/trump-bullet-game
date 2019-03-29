from lib.games import Game, TrumpBulletGame


def _run() -> None:
    """Runs a game."""
    game: Game = TrumpBulletGame()
    game.run()


if __name__ == "__main__":
    _run()
