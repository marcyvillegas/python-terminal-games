from data.enum_game_list import GameList
from games.base_game import GameBase
from games.guess_the_song.data.songs import songs
import random


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
    @staticmethod
    def start_game(self):

        song_choices = random.sample(songs, 4)
        song_to_guess_index = random.randrange(len(song_choices))

        print("======================")
        print("Guess this song:")
        print(f"🎶 {song_choices[song_to_guess_index]['lyrics']} 🎶")

        print("Choices:")

        for song in song_choices:
            print(f"[{str(song_choices.index(song) + 1)}] {song['title']}")

        input_answer = input("Your answer: ")

        if input_answer == str(song_to_guess_index + 1):
            self.game_score += 1
            print("You are correct!")
            print(f"Your current score is: {self.game_score}")
            self.start_game(self)
        else:
            print("WRONG!")
            print(f"Your current score is: {self.game_score}")
            self.start_game(self)

        # Exits the current game
        # input_exit_game = input(f"Are you sure you want to exit {self.game_name}? (Y/N): ")
        # if input_exit_game == "Y":
        #     self.close_game()
        # else:
        #     rerun_game = self.__call__
        #     rerun_game()


# Create instance of class
guess_the_song = GuessTheSongGame()
