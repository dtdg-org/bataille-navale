from mvc.model.enum.Direction import Direction
from mvc.model.Game import Game
from mvc.view.GridView import GridView


class PlaceShipGridView(GridView):
    def __init__(self, game, **kw):
        super().__init__(game, **kw)

        # Default direction
        self.direction = Direction.SOUTH

    def show(self):
        self.tkraise()

    def click_on_square(self, event, col, row, game: Game):
        try:
            boat_size = game.player.get_size_of_next_boat_to_place()
            game.player.place_boat(col, row, boat_size, self.direction)
        except Exception as ex:
            print("Invalid position.", ex)
        self.master.update_continue_button()
        super().click_on_square(event, col, row, game)

    def right_click(self, event, col, row, game):
        self.direction = Direction.SOUTH if self.direction == Direction.EAST else Direction.EAST
        super().right_click(event, col, row, game)
        self.cursor_enter_square(event, col, row, game)

    def cursor_enter_square(self, event, col, row, game):
        boat_size = self.game.player.get_size_of_next_boat_to_place()
        positions = []
        try:
            positions = self.game.player.grid.compute_positions(col, row, boat_size, self.direction)
        except:
            pass  # Swallow exception completely.

        for position in positions:
            _col = position[0]
            _row = position[1]
            self.draw_hovered_square(_col, _row)
        super().cursor_enter_square(event, col, row, game)

    def cursor_leave_square(self, event, col, row, game):
        super().cursor_leave_square(event, col, row, game)
