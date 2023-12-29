from utils.clear_terminal import clear_terminal


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

    # Displays welcome message of the specific game
    def __call__(
            self
    ):
        clear_terminal()
        print(f">> Welcome to {self.game_name} <<")

    # Closes the current game and returns back to start menu
    def close_game(
            self
    ):
        from main import start_game
        start_game()
