from mvc.model.ruleset.Ruleset import Ruleset


class ClassicRuleset(Ruleset):
    """
    Classic Rules set is :
    One 5-square boat,
    One 4-square boat,
    Two 3-square boat,
    One 2-square boat.

    You can play again when you hit.
    """

    def __init__(self) -> None:
        super().__init__()
        self.map_ship_square = {
            2: 1,
            3: 2,
            4: 1,
            5: 1
        }
        self.play_again_when_hit = True
        self.min_distance_between_boats = 1
        self.side_length = 10
