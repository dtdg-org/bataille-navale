import random

from mvc.model.Direction import Direction
from mvc.model.Player import Player
from mvc.model.PlayerType import PlayerType


class AIPlayer(Player):
    def __init__(self, name, grid, ruleset, ai_strategy):
        super().__init__(name, grid, ruleset)
        self.player_type = PlayerType.AI
        self.ai = ai_strategy

    def place_all_boats(self):
        for boat_size in Player.build_list_boats_being_placed(self.ruleset):
            flag = False
            while not flag:
                try:
                    col = random.choice(self.grid.columns_indices)
                    row = random.choice(self.grid.rows_indices)
                    dir = random.choice([Direction.EAST, Direction.SOUTH])
                    self.place_boat(col, row, boat_size, dir)
                    flag = True
                except Exception as ex:
                    pass  # Swallowing the exception
        return self.get_size_of_next_boat_to_place() == 0
