import tkinter as tk

from mvc.model.Game import Game
from mvc.model.GameState import GameState
from mvc.model.Grid import Grid
from mvc.model.ClassicRuleset import ClassicRuleset
from mvc.view.PlaceShipView import PlaceShipView
from mvc.view.HomeView import HomeView


class MainController:
    def __init__(self) -> None:
        # Init model
        self.grid = Grid(10)

        root = tk.Tk()
        root.geometry("550x550")
        root.title("Battleship game")

        # Init state of the game
        self.state = GameState.MENU
        self.ruleset = ClassicRuleset()
        self.game = Game(self.ruleset, self.grid)

        # Init home view
        self.view_root = root
        self.view = HomeView(self, master=self.view_root)
        self.view.show()

    def run(self):
        self.view_root.mainloop()

    def load_place_ship_view(self):
        self.view = PlaceShipView(self, master=self.view_root)
        self.state = GameState.PLACING_SHIPS
        self.view.show()

    def click_on_grid(self, event, col, row):
        if self.state == GameState.PLACING_SHIPS:
            pass
        if self.state == GameState.IN_GAME:
            is_hit = self.grid.hit(col, row)
            if is_hit:
                pass

    def cursor_enter_cell(self, event, col, row):
        if self.state == GameState.PLACING_SHIPS:
            self.view.set_hovered_background_color(event.widget, col, row)
        if self.state == GameState.IN_GAME:
            self.view.set_hovered_background_color(event.widget, col, row)

    def cursor_leave_cell(self, event, col, row):
        if self.state == GameState.PLACING_SHIPS:
            self.view.reset_background_color(event.widget, col, row)
        if self.state == GameState.IN_GAME:
            self.view.reset_background_color(event.widget, col, row)

