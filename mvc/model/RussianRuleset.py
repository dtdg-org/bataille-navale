from mvc.model.Ruleset import Ruleset


class RussianRuleset(Ruleset):
    """
    Russian Rules set is :
    One 4-square boat,
    Two 3-square boat,
    Three 2-square boat,
    Four 1-square boat.

    You can play again when you hit.
    """

    def __init__(self) -> None:
        super().__init__()
        self.map_ship_square = {
            1: 4,
            2: 3,
            3: 2,
            4: 1,
        }
        self.play_again_when_hit = True
        self.min_distance_between_boats = 1
        self.side_length = 10
