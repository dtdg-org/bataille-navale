from tkinter import Frame, Canvas, Label

from mvc.view.GridView import GridView
from mvc.view.OpponentGridView import OpponentGridView
from mvc.view.PlayerGridView import PlayerGridView


class GameView(Frame):
    TITLE_TEXT = "Fight and defeat your opponent ! Your ship on the left grid, opponent ships on the right grid."

    def __init__(self, controller, game, **kw):
        super().__init__(**kw)
        self.grid(column=0, row=0, padx=5, pady=5, sticky="nsew")

        # Title definition
        title = Label(self, text=self.TITLE_TEXT, relief='groove', height=2)
        title.grid(column=0, row=0, padx=5, pady=5, columnspan=3, sticky="nsew")
        self.title = title

        # Available ship column definition
        ship_column = Frame(self)
        ship_column.grid(column=0, row=1, padx=5, pady=5)
        ship_column_canvas = Canvas(ship_column,
                                    bg='white',
                                    borderwidth=2,
                                    relief='groove',
                                    width=120,
                                    height=11 * GridView.SQUARE_SIZE_PX)
        ship_column_canvas.grid(column=0, row=0)
        ship_column_labels = {}
        for boat_size, boat_count in game.ruleset.map_ship_square.items():
            label = Label(ship_column_canvas, text=f"{boat_count} boat of size {boat_size}")
            label.grid(column=0, row=boat_size)
            ship_column_labels[boat_size] = label
        self.ship_column = ship_column

        # Player grid definition.
        player_battleship_grid = PlayerGridView(game, master=self)
        player_battleship_grid.grid(column=1, row=1, padx=20, pady=5)
        self.player_battleship_grid = player_battleship_grid

        # Opponent grid definition.
        opponent_battleship_grid = OpponentGridView(game, master=self)
        opponent_battleship_grid.grid(column=2, row=1, padx=20, pady=5)
        self.opponent_battleship_grid = opponent_battleship_grid

    def show(self):
        self.tkraise()
