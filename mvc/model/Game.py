from mvc.model.player.AIPlayer import AIPlayer
from mvc.model.enum.GameState import GameState
from mvc.model.Grid import Grid
from mvc.model.player.HumanPlayer import HumanPlayer
from mvc.model.Option import Option


class Game:
    def __init__(self, option: Option):
        self.ruleset = option.ruleset
        self.ai = option.ai

        # At initialization, State is in Menu mode.
        self.state = GameState.MENU

        # When we initialize a game, we init the player objects
        self.player = HumanPlayer("Player", Grid(self.ruleset.side_length), self.ruleset)
        self.opponent = AIPlayer("AI opponent", Grid(self.ruleset.side_length), self.ruleset, self.ai)

        self.player_turn = True  # Will act as a mutex

    def play_turn(self, col, row):
        if self.player_turn:
            self.player_turn = False
            self.player.play_turn(self.opponent.grid, col, row)
            self.opponent.grid.hit(col, row)

            # Now time for opponent to play.
            self.opponent.play_turn(self.player.grid)
            self.player_turn = True
        else:
            print("Not player's turn.")
