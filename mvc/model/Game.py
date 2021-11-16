from mvc.model.Player import Player


class Game:
    def __init__(self, ruleset, grid):
        # When we initialize a game, we init a player and boats positions arrays
        self.player = Player()
        self.opponent = Player()

        # Boats is a map, for each ship specified in the ruleset, it stores the position of the ship.
        self.boats = {}
        for boat_size in ruleset.map_ship_square.keys():
            self.boats[boat_size] = []  # Initialized with empty array.
