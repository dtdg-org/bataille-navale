import random
from mvc.model.Direction import Direction


class Player:
    def __init__(self, name, grid, player_type, ai_strategy, ruleset):
        self.name = name
        self.grid = grid
        self.player_type = player_type
        self.ai = ai_strategy
        self.ruleset = ruleset
        self.boats_being_placed = Player.build_list_boats_being_placed(ruleset)

    @staticmethod
    def build_list_boats_being_placed(ruleset):
        """
        This method will build the list of boat sizes to be placed.
        """
        tab = []
        for k, v in ruleset.map_ship_square.items():
            for i in range(v):
                tab.append(k)
        return sorted(tab)  # We need to sort the map to have coherence

    def get_size_of_next_boat_to_place(self):
        if not self.boats_being_placed:
            return 0
        else:
            return self.boats_being_placed[-1]

    def place_boat(self, col, row, boat_size, direction):
        if self.get_size_of_next_boat_to_place() != 0:
            self.grid.place_boat(col, row, boat_size, direction)
            self.boats_being_placed.remove(boat_size)

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
                    print(f"Failed placing boat at {col} {row} {dir} because of", ex)  # Swallowing the exception
        return self.get_size_of_next_boat_to_place() == 0
