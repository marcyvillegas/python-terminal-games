class GameBase:
    """
        GameBase class is the basis class for all of the games.
    """

    def __init__(
            self,
            game_score=0,
            game_name=None
    ):
        self.game_score = game_score
        self.game_name = game_name

    # Closes the current game and returns back to start menu
    def close_game(
            self
    ):
        from main import start_game
        start_game()
