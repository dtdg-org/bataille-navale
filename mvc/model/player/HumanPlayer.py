from mvc.model.player.Player import Player
from mvc.model.enum.PlayerType import PlayerType


class HumanPlayer(Player):
    def __init__(self, name, grid, ruleset):
        super().__init__(name, grid, ruleset)
        self.player_type = PlayerType.HUMAN
        self.ai = None
