from data.enum_game_list import Game
from games.guess_the_song.main import main as guess_the_song

game_list = {
    Game.GUESS_THE_SONG.value: guess_the_song,
    Game.SAMPLE_2: "sample again"
}