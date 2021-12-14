import tkinter as tk

from mvc.model.Game import Game
from mvc.model.enum.GameState import GameState
from mvc.model.ruleset.ClassicRuleset import ClassicRuleset
from mvc.model.Option import Option
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
        self.game, self.options = self.init_new_game()

        # Init home view
        self.view_root = root
        self.view = HomeView(self, master=self.view_root)
        self.view.show()

    @staticmethod
    def init_new_game():
        options = Option()
        options.set_ruleset(ClassicRuleset())
        options.set_ai(None)  # TODO
        game = Game(options)
        return game, options

    def run(self):
        self.view_root.mainloop()

    def load_place_ship_view(self):
        self.view = PlaceShipView(self, self.game, master=self.view_root)
        self.game.state = GameState.PLACING_SHIPS
        self.view.show()

    def load_option_view(self):
        pass

    def load_game_view(self):
        """
        Make the Opponent choose his boat placements and then load the game view
        """
        self.game.opponent.place_all_boats()
        self.view = GameView(self, self.game, master=self.view_root)
        self.game.state = GameState.IN_GAME
        self.view.show()

    def load_home_menu(self):
        """
        Load the Home Menu
        """
        self.game, self.options = self.init_new_game()
        self.view = HomeView(self, master=self.view_root)
        self.view.show()
