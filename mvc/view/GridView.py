from tkinter import Frame, Canvas

from mvc.model.Colors import Colors


class GridView(Frame):
    """
    Parent class for all grid views. Is in charge of displaying a grid
    of a certain amount of squares and route mouse click and hovering
    to dedicated methods.
    """
    SQUARE_SIZE_PX = 30

    def __init__(self, game, **kw):
        super().__init__(**kw)
        self.grid(column=0, row=0, padx=5, pady=5, sticky="nsew")
        self.master = kw['master']

        # Add the game as an attribute to reuse it later
        self.game = game
        grid_model = game.player.grid

        # Battleship grid definition.
        grid_column = Frame(self)
        grid_column.grid(column=1, row=1, padx=5, pady=5)

        self.battleship_grid = {}
        # For each row and each column, create a canvas, representing one square
        i_row = 0
        for row_index in grid_model.rows_indices:
            i_column = 0
            for column_index in grid_model.columns_indices:
                square = Canvas(grid_column,
                                bg='white',
                                borderwidth=0,
                                width=GridView.SQUARE_SIZE_PX,
                                height=GridView.SQUARE_SIZE_PX)
                square.grid(row=i_row, column=i_column)
                square.bind("<Button-1>",
                            lambda event, col=column_index, row=row_index: self.click_on_square(event, col, row, game))
                square.bind("<Button-3>",
                            lambda event, col=column_index, row=row_index: self.right_click(event, col, row, game))
                square.bind("<Enter>",
                            lambda event, col=column_index, row=row_index: self.cursor_enter_square(event, col, row,
                                                                                                    game))
                square.bind("<Leave>",
                            lambda event, col=column_index, row=row_index: self.cursor_leave_square(event, col, row,
                                                                                                    game))

                self.battleship_grid[(column_index, row_index)] = square
                i_column += 1
            i_row += 1
        self.update_grid_view()

    def show(self):
        self.tkraise()

    def click_on_square(self, event, col, row, game):
        self.update_grid_view()

    def right_click(self, event, col, row, game):
        self.update_grid_view()

    def cursor_enter_square(self, event, col, row, game):
        pass

    def cursor_leave_square(self, event, col, row, game):
        self.update_grid_view()

    def draw_square(self, col, row):
        if self.game.player.grid.squares[col][row].has_boat:
            if self.game.player.grid.squares[col][row].is_hit:
                color = Colors.HIT
            else:
                color = Colors.BOAT
        else:
            color = Colors.NO_BOAT
        self.battleship_grid[(col, row)]['background'] = color.value

    def draw_hovered_square(self, col, row):
        self.battleship_grid[(col, row)]['background'] = Colors.SELECTED.value

    def update_grid_view(self):
        for position in self.battleship_grid.keys():
            self.draw_square(position[0], position[1])
