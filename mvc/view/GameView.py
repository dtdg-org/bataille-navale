from tkinter import Frame, Canvas, Label

from mvc.view.GridView import GridView

SQUARE_SIZE = 30


class PlaceShipView(Frame):
    def __init__(self, controller, **kw):
        super().__init__(**kw)
        self.grid(column=0, row=0, padx=5, pady=5, sticky="nsew")

        # Title definition
        title = Label(self, text="Ship definition YO")
        title.grid(column=0, row=0, padx=5, pady=5, columnspan=2, sticky="nw")

        # Available ship column definition
        ship_column = Frame(self)
        ship_column.grid(column=0, row=1, padx=5, pady=5)
        ship_column_canvas = Canvas(ship_column,
                                    bg='white',
                                    borderwidth=2,
                                    relief='groove',
                                    width=120,
                                    height=11 * SQUARE_SIZE)
        ship_column_canvas.grid(column=0, row=0)
        ship_column_labels = {}
        for boat_size, boat_count in controller.ruleset.map_ship_square.items():
            label = Label(ship_column_canvas, text=f"{boat_count} boat of size {boat_size}")
            label.grid(column=0, row=boat_size)
            ship_column_labels[boat_size] = label

        # Battleship grid definition.
        grid_column = GridView(controller.grid, master=self)
        grid_column.grid(column=1, row=1, padx=5, pady=5)

    def show(self):
        self.tkraise()
