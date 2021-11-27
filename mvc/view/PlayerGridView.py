from mvc.model.Game import Game
from mvc.model.enum.Colors import Colors
from mvc.view.GridView import GridView


class PlayerGridView(GridView):
    def __init__(self, game, **kw):
        super().__init__(game, **kw)
        self.observe(game.player.grid)

    def show(self):
        self.tkraise()

    def click_on_square(self, event, col, row, game: Game):
        pass

    def right_click(self, event, col, row, game):
        pass

    def cursor_enter_square(self, event, col, row, game):
        pass

    def cursor_leave_square(self, event, col, row, game):
        pass

    def draw_square(self, col, row):
        square = self.game.player.grid.squares[col][row]
        color = Colors.NO_BOAT
        if square.is_miss:
            color = Colors.MISS
        if square.has_boat:
            color = Colors.BOAT
        if square.is_hit:
            color = Colors.HIT
        self.battleship_grid[(col, row)]['background'] = color.value
