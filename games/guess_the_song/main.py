from data.enum_game_list import GameList
from games.base_game import GameBase
from games.guess_the_song.data.songs import songs
import random

from utils.clear_terminal import clear_terminal


class GuessTheSongGame(GameBase):
    """
        Guess The Song is a game where you will guess a song through its lyrics.
    """

    def __init__(self):
        super().__init__(
            game_name=GameList.GUESS_THE_SONG.value
        )

    def __call__(self):
        super().__call__()
        self.start_game(self)

    # Logic of the game
    is_answer_correct = None

    @staticmethod
    def start_game(self):

        song_choices = random.sample(songs, 4)
        song_to_guess_index = random.randrange(len(song_choices))

        clear_terminal()

        if isinstance(self.is_answer_correct, bool):
            if self.is_answer_correct:
                print("You are correct!")
                print(f"Your current score is: {self.game_score}")

            if not self.is_answer_correct:
                print("WRONG!")
                print(f"Your current score is: {self.game_score}")

        print("======================")
        print("Guess this song:")
        print(f"🎶 {song_choices[song_to_guess_index]['lyrics']} 🎶")

        print("Choices:")

        for song in song_choices:
            print(f"[{str(song_choices.index(song) + 1)}] {song['title']}")

        input_answer = input("Your answer: ")

        if input_answer == "x":
            self.close_game()

        if input_answer == str(song_to_guess_index + 1):
            self.game_score += 1
            self.is_answer_correct = True
            self.start_game(self)
        else:
            self.is_answer_correct = False
            self.start_game(self)


# Create instance of class
guess_the_song = GuessTheSongGame()
