from tkinter import Frame, Canvas, Label, Button, DISABLED, NORMAL

from mvc.view.GridView import GridView
from mvc.view.PlaceShipGridView import PlaceShipGridView


class PlaceShipView(Frame):
    TITLE_TEXT = "Ship definition screen. Left click: place ship. Right click: rotate ship"

    def __init__(self, controller, game, **kw):
        super().__init__(**kw)
        self.grid(column=0, row=0, padx=5, pady=5, sticky="nsew")

        self.controller = controller
        self.game = game

        # Title definition
        title = Label(self, text=self.TITLE_TEXT, relief='groove', height=2)
        title.grid(column=0, row=0, padx=5, pady=5, columnspan=2, sticky="nsew")
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

        # Battleship grid definition.
        battleship_grid = PlaceShipGridView(game, master=self)
        battleship_grid.grid(column=1, row=1, padx=5, pady=5)
        self.battleship_grid = battleship_grid

        # Fight against AI Opponent button
        continue_button = Button(master=self,
                                 text='Fight against AI Opponent',
                                 state=DISABLED,
                                 command=controller.load_game_view)
        continue_button.grid(column=0, row=2, padx=5, pady=5, columnspan=2)
        self.continue_button = continue_button

    def update_continue_button(self):
        """
        This method is in charge of updating the state of the continue button.
        """
        if self.game.get_size_of_next_boat_to_place() == 0:
            self.continue_button['state'] = NORMAL

    def show(self):
        self.tkraise()
