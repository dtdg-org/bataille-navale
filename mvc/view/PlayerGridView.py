from mvc.model.Game import Game
from mvc.view.GridView import GridView


class PlayerGridView(GridView):
    def __init__(self, game, **kw):
        super().__init__(game, **kw)

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
