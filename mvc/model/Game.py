from mvc.model.GameState import GameState
from mvc.model.Grid import Grid
from mvc.model.Player import Player
from mvc.model.PlayerType import PlayerType


class Game:
    def __init__(self, ruleset):
        self.ruleset = ruleset

        # At initialization, State is in Menu mode.
        self.state = GameState.MENU

        # When we initialize a game, we init the player objects
        self.player = Player("Player", Grid(ruleset.side_length), PlayerType.HUMAN, None, ruleset)
        self.opponent = Player("AI opponent", Grid(ruleset.side_length), PlayerType.AI, None, ruleset)
