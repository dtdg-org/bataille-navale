import tkinter as tk

from mvc.model.Game import Game
from mvc.model.GameState import GameState
from mvc.model.ClassicRuleset import ClassicRuleset
from mvc.view.GameView import GameView
from mvc.view.PlaceShipView import PlaceShipView
from mvc.view.HomeView import HomeView


class MainController:
    def __init__(self) -> None:
        # Init view processor
        root = tk.Tk()
        root.geometry("1000x470")
        root.title("Battleship game")

        # Init state of the game
        self.ruleset = ClassicRuleset()
        self.game = Game(self.ruleset)

        # Init home view
        self.view_root = root
        self.view = HomeView(self, master=self.view_root)
        self.view.show()

    def run(self):
        self.view_root.mainloop()

    def load_place_ship_view(self):
        self.view = PlaceShipView(self, self.game, master=self.view_root)
        self.game.state = GameState.PLACING_SHIPS
        self.view.show()

    def load_option_view(self):
        pass

    def load_game_view(self):
        self.view = GameView(self, self.game, master=self.view_root)
        self.game.state = GameState.IN_GAME
        self.view.show()
