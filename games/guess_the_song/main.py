from utils.base_game import GameBase


class GuessTheSongGame(GameBase):
    """
        Guess The Song is a game where you will guess a song through its lyrics.
    """

    def __init__(
            self
    ):
        super().__init__()

    def __call__(self):
        self.start_game(self)

    @staticmethod
    def start_game(self):
        print(f"Your score is {self.game_score}")


def main():
    guess_the_song = GuessTheSongGame()

    guess_the_song()
