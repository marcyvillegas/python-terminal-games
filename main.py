# The goal of this project is to learn and be comfortable with Python classes

from data.enum_game_list import GameList
from utils.clear_terminal import clear_terminal

from termcolor import colored, cprint

from utils.text_to_space import text_to_character


# from utils.text_to_space import text_to_space


class StartGame:
    """
        StartGame class is the starting point of the game program.
    """

    def __init__(
            self,
            games=None
    ):
        self.games = games

    # Run the start menu of the game
    def __call__(self):
        self.display_start_menu(self)

    # Displays the start menu and runs the selected game
    @staticmethod
    def display_start_menu(self):
        clear_terminal()

        welcome_message = "---- Welcome to python-terminal-games! ----"

        cprint(text_to_character(text=welcome_message, character="-"), color="white", on_color="on_magenta")
        cprint(welcome_message, color="white", on_color="on_magenta")
        cprint(text_to_character(text=welcome_message, character="-", space_below=True), color="white", on_color="on_magenta")

        cprint("Choose what game to play🕹️", color="red")
        game_number = 1
        for game_item in self.games:
            print(f"[{game_number}] {game_item.value}")
            game_number += 1

        input_game_name = input(colored("\nEnter the game number you want to play: ", color="blue"))

        from data.game_list import game_list
        selected_game = self.games[int(input_game_name) - 1]
        run_game = game_list[selected_game.value]
        run_game()


# Create instance of class
start_game = StartGame([
    GameList.GUESS_THE_SONG,
    GameList.SAMPLE_2
])

# Runs the game program
start_game()
