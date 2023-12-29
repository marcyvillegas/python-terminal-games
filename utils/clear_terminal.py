import os


def clear_terminal():
    os.system('cls' if os.name == 'nt' else "printf '\033c'")
