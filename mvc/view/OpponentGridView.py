from mvc.model.enum.Colors import Colors
from mvc.model.Game import Game
from mvc.view.GridView import GridView


class OpponentGridView(GridView):
    def __init__(self, game, **kw):
        super().__init__(game, **kw)

    def show(self):
        self.tkraise()

    def click_on_square(self, event, col, row, game: Game):
        hit = game.opponent.grid.hit(col, row)
        super().click_on_square(event, col, row, game)

    def right_click(self, event, col, row, game):
        self.battleship_grid[(col, row)]['background'] = Colors.FLAG.value
        # TODO add flag to model for persistence

    def cursor_enter_square(self, event, col, row, game):
        self.draw_hovered_square(col, row)
        super().cursor_enter_square(event, col, row, game)

    def cursor_leave_square(self, event, col, row, game):
        super().cursor_leave_square(event, col, row, game)

    def draw_square(self, col, row):
        if self.game.opponent.grid.squares[col][row].has_boat:
            if self.game.opponent.grid.squares[col][row].is_hit:
                color = Colors.HIT
            else:
                color = Colors.NO_BOAT
        else:
            if self.game.opponent.grid.squares[col][row].is_hit:
                color = Colors.MISS
            else:
                color = Colors.NO_BOAT
        self.battleship_grid[(col, row)]['background'] = color.value

    def draw_hovered_square(self, col, row):
        self.battleship_grid[(col, row)]['background'] = Colors.SELECTED.value

    def update_grid_view(self):
        for position in self.battleship_grid.keys():
            self.draw_square(position[0], position[1])

