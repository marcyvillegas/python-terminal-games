from data.enum_game_list import GameList
from games.guess_the_song.main import main as guess_the_song

game_list = {
    GameList.GUESS_THE_SONG.value: guess_the_song,
    GameList.SAMPLE_2: "sample again"
}