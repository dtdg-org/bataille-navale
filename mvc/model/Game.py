from mvc.model.GameState import GameState
from mvc.model.Grid import Grid
from mvc.model.Player import Player
from mvc.model.PlayerType import PlayerType


class Game:
    def __init__(self, ruleset):
        self.ruleset = ruleset

        # At initialization, State is in Menu mode.
        self.state = GameState.MENU
        self.boats_being_placed = Game.build_list_boats_being_placed(ruleset)

        # When we initialize a game, we init the player objects
        self.player = Player("Player", Grid(ruleset.side_length), PlayerType.HUMAN, None)
        self.opponent = Player("AI opponent", Grid(ruleset.side_length), PlayerType.AI, None)

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
            try:
                self.player.grid.place_boat(col, row, boat_size, direction)
                self.boats_being_placed.remove(boat_size)
            except Exception as ex:
                print(ex)  # Swallowing the exception.
