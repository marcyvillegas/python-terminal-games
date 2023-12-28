from data.shared_data import shared_game_data
from games.base_game import GameBase


class GuessTheSongGame(GameBase):
    """
        Guess The Song is a game where you will guess a song through its lyrics.
    """

    def __init__(
            self
    ):
        super().__init__(
            game_name="Guess The Song"
        )

    def __call__(self):
        self.start_game(self)

    @staticmethod
    def start_game(self):
        print(f">> Welcome to {self.game_name} <<")
        print(f"Your score is {self.game_score}")

        input_exit_game = input(f"Are you sure you want to exit {self.game_name}? (Y/N): ")
        if input_exit_game == "Y":
            self.close_game()
        else:
            del shared_game_data['guess_the_song_class_instance']
            rerun_game = shared_game_data['start_guess_the_song']
            rerun_game()


def main():
    guess_the_song = GuessTheSongGame()

    # Make the instance of GuessTheSongGame class global
    shared_game_data['guess_the_song_class_instance'] = guess_the_song

    guess_the_song()


# Make the function that runs the whole program global
shared_game_data['start_guess_the_song'] = main
