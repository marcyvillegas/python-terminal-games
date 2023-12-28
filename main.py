# The goal of this project is to learn and be comfortable with Python classes

from data.enum_game_list import GameList
from data.game_list import game_list
from data.shared_data import shared_game_data


class StartGame:
    """
        StartGame class is the starting point of the game program.
    """

    def __init__(
            self,
            games
    ):
        self.games = games

    # Run the start menu of the game
    def __call__(self):
        self.display_start_menu(self)

    # Displays the start menu and runs the chosen game
    @staticmethod
    def display_start_menu(self):
        print("== Choose what game to play ==")

        game_number = 1
        for game_item in self.games:
            print(f"[{game_number}] {game_item.value}")
            game_number += 1

        input_game_name = input("Enter the game number you want to play: ")

        selected_game = self.games[int(input_game_name) - 1]
        run_game = game_list[selected_game.value]
        run_game()


# Runs main python file
def main():
    # Add the games on the class
    start_game = StartGame([
        GameList.GUESS_THE_SONG,
        GameList.SAMPLE_2
    ])

    # Make the instance of StartGame class global
    shared_game_data['start_game_class_instance'] = start_game

    # Runs the specific game
    start_game()


# Make the function that runs the whole program global
shared_game_data['start_game_program'] = main

# Call the function that will start the program
main()
