class Grid:
    def __init__(self, length_side) -> None:
        self.rows_indices = [i for i in range(1, length_side+1)]  # 1, 2, 3, ...
        self.columns_indices = [chr(ord('A') + i) for i in range(0, length_side)]  # A, B, C ...
        self.positions = []  # A1, A2, ..., J9, J10
        for row in self.rows_indices:
            for col in self.columns_indices:
                self.positions.append(str(row) + str(col))
        self.hits = []  # Empty list at the beginning

        super().__init__()

    def hit(self, col, row):
        position = Grid.tuple_coordinate_to_str(col, row)
        if position in self.hits:
            return False
        else:
            self.hits.append(position)
            return True

    @staticmethod
    def str_coordinate_to_tuple(coord: str):
        return coord[0], coord[1:]

    @staticmethod
    def tuple_coordinate_to_str(column: str, row: int):
        return f'{column}{row}'
