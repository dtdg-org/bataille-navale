class Player:
    def __init__(self, name, grid, player_type, ai_strategy):
        self.name = name
        self.grid = grid
        self.player_type = player_type
        self.ai = ai_strategy
