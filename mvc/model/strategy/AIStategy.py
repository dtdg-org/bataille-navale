import random

from mvc.model.Grid import Grid


class AIStrategy:
    def __init__(self):
        pass

    def next_move(self, grid: Grid):
        col = random.choice(grid.columns_indices)
        row = random.choice(grid.rows_indices)
        return col, row
