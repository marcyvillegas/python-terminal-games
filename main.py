# The goal of this project is to learn and be comfortable with Python classes

class GameBase:
    """
        Game Base class is the foundation of all games.
    """

    def __init__(
            self,
            game_name: str = None,
            game_score: int = 0
    ):
        self.game_name = game_name
        self.game_score = game_score

    # Run the start menu of the game
    def __call__(self):
        print("This will run the start menu of the game")
        self.display_start_menu()

    # Close the current game
    def close(self):
        print(f"Are you sure you want to close {self.game_name}?")

    # Helper function inside the class
    @staticmethod
    def display_start_menu():
        print("Displayed start menu")


# Run main python file
if __name__ == '__main__':
    game = GameBase("sample_game")
    game()
