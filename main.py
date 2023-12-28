# The goal of this project is to learn and be comfortable with Python classes

from data.enum_game_list import Game
from data.game_list import game_list


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

    # Close the current game - rethink if close game will be here
    def close(self):
        print(f"Are you sure you want to close?")

    # Displays the start menu and runs the chosen game
    @staticmethod
    def display_start_menu(self):
        print("== Choose what game to play ==")

        game_number = 1
        for game_item in self.games:
            print(f"[{game_number}] {game_item.value}")
            game_number += 1

        input_game_name = input("Enter the game number you want to play: ")

        chosen_game = self.games[int(input_game_name) - 1]
        run_game = game_list[chosen_game.value]
        run_game()


# Run main python file
if __name__ == '__main__':
    # Add the games on the class
    start_game = StartGame([
        Game.GUESS_THE_SONG,
        Game.SAMPLE_2
    ])

    start_game()
