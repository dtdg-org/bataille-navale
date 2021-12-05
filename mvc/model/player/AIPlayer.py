import random

from mvc.model.enum.Direction import Direction
from mvc.model.player.Player import Player
from mvc.model.enum.PlayerType import PlayerType
from mvc.model.strategy.AIStategy import AIStrategy


class AIPlayer(Player):
    def __init__(self, name, grid, ruleset, ai_strategy):
        super().__init__(name, grid, ruleset)
        self.player_type = PlayerType.AI
        # self.ai = ai_strategy
        self.ai = AIStrategy()  # TODO : change this default value.

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
                except:
                    pass  # Swallowing the exception
        return self.get_size_of_next_boat_to_place() == 0

    def play_turn(self, grid):
        col, row = self.ai.next_move(grid)
        return grid.hit(col, row)
