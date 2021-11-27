from mvc.model.enum.Colors import Colors
from mvc.model.Game import Game
from mvc.view.GridView import GridView


class OpponentGridView(GridView):
    def __init__(self, game, **kw):
        super().__init__(game, **kw)
        self.observe(game.opponent.grid)

    def show(self):
        self.tkraise()

    def click_on_square(self, event, col, row, game: Game):
        game.play_turn(col, row)
        # hit = game.opponent.grid.hit(col, row)
        super().click_on_square(event, col, row, game)

    def right_click(self, event, col, row, game):
        game.opponent.grid.flag(col, row)
        super().right_click(event, col, row, game)

    def cursor_enter_square(self, event, col, row, game):
        self.draw_hovered_square(col, row)
        super().cursor_enter_square(event, col, row, game)

    def cursor_leave_square(self, event, col, row, game):
        super().cursor_leave_square(event, col, row, game)

    def draw_square(self, col, row):
        square = self.game.opponent.grid.squares[col][row]
        color = Colors.NO_BOAT
        if square.is_flag:
            color = Colors.FLAG
        if square.is_miss:
            color = Colors.MISS
        if square.is_hit:
            color = Colors.HIT
        self.battleship_grid[(col, row)]['background'] = color.value

    def draw_hovered_square(self, col, row):
        self.battleship_grid[(col, row)]['background'] = Colors.SELECTED.value

    def update_grid_view(self):
        for position in self.battleship_grid.keys():
            self.draw_square(position[0], position[1])

