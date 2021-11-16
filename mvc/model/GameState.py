from enum import Enum


class GameState(Enum):
    MENU = "Menu"
    PLACING_SHIPS = "Placing ships"
    IN_GAME = "In game"
    GAME_OVER = "Game Over"
