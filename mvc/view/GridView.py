from tkinter import Frame, Canvas

from mvc.model.Colors import Colors

SQUARE_SIZE = 30


class GridView(Frame):
    def __init__(self, controller, **kw):
        super().__init__(**kw)
        self.grid(column=0, row=0, padx=5, pady=5, sticky="nsew")

        # Add the controller as an attribute to reuse it later
        self.controller = controller

        # Battleship grid definition.
        grid_column = Frame(self)
        grid_column.grid(column=1, row=1, padx=5, pady=5)

        self.battleship_grid = {}
        # For each row and each column, create a canvas, representing one square
        i_row = 0
        for row in controller.grid.rows_indices:
            i_column = 0
            for column in controller.grid.columns_indices:
                square = Canvas(grid_column,
                                bg='white',
                                borderwidth=0,
                                width=SQUARE_SIZE,
                                height=SQUARE_SIZE)
                square.grid(row=i_row, column=i_column)
                square.bind("<ButtonRelease>",
                            lambda event, col=column, row=row: controller.click_on_grid(event, col, row))
                square.bind("<Enter>", lambda event, col=column, row=row: controller.cursor_enter_cell(event, col, row))
                square.bind("<Leave>", lambda event, col=column, row=row: controller.cursor_leave_cell(event, col, row))
                i_column += 1
            i_row += 1

    def show(self):
        self.tkraise()

    def set_background_color(self, widget, col, row):
        if (col, row) in self.controller.game.boats:
            color = Colors.BOAT
        else:
            color = Colors.NO_BOAT
        widget['background'] = color.value

    def set_hovered_background_color(self, widget, col, row):
        widget['background'] = Colors.SELECTED.value

    def reset_background_color(self, widget, col, row):
        self.set_background_color(widget, col, row)
