# The goal of this project is to learn and be comfortable with Python classes

from data.enum_game_list import Game


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

    # Close the current game
    def close(self):
        print(f"Are you sure you want to close?")

    # Helper functions inside the class
    @staticmethod
    def display_start_menu(self):
        print("== Choose what game to play ==")

        game_number = 1
        for game_item in self.games:
            print(f"[{game_number}] {game_item.value}")
            game_number += 1

        input_game_name = input("Please enter some text: ")


# Run main python file
if __name__ == '__main__':

    # Add the games on the class
    game = StartGame([
        Game.GUESS_THE_SONG,
        Game.SAMPLE_2
    ])

    game()
