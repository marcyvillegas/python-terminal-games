from data.shared_data import shared_game_data


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
        del shared_game_data['start_game_class_instance']
        del shared_game_data['guess_the_song_class_instance']
        run_game_program = shared_game_data['start_game_program']
        run_game_program()
