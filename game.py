from game.games import Game, TrumpBulletGame


def _run_game() -> None:
    """Runs a game."""
    game: Game = TrumpBulletGame()
    game.run()


if __name__ == "__main__":
    _run_game()
