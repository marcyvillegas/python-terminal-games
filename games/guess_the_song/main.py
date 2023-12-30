from beaupy import select
from termcolor import cprint

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
        self.start_game(self)

    # Logic of the game
    is_answer_correct = None

    @staticmethod
    def start_game(self):

        song_choices = random.sample(songs, 4)
        song_to_guess_index = random.randrange(len(song_choices))

        clear_terminal()

        super().display_welcome_message()

        if isinstance(self.is_answer_correct, bool):
            if self.is_answer_correct:
                cprint("🥳 You are correct!", color="light_green")
                print(f"Your current score is: {self.game_score}\n")

            if not self.is_answer_correct:
                cprint("🥺 WRONG!", color="light_red")
                print(f"Your current score is: {self.game_score}\n")

        cprint(f" 🎹 {song_choices[song_to_guess_index]['lyrics']} 🎸 ", color="white", on_color="on_light_blue")

        cprint("\nChoices:", color="cyan")

        song_choices_display = []

        for song in song_choices:
            song_choices_display.append(song['title'])
        song_choices_display.append("EXIT GAME")

        input_answer = select(
            options=song_choices_display,
            return_index=True
        )

        if input_answer == 4:
            self.close_game()

        if input_answer == song_to_guess_index:
            self.game_score += 1
            self.is_answer_correct = True
            self.start_game(self)
        else:
            self.is_answer_correct = False
            self.start_game(self)


# Create instance of class
guess_the_song = GuessTheSongGame()
