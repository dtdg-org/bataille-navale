from mvc.model.enum.Direction import Direction
from mvc.model.Square import Square


class Grid:
    def __init__(self, length_side) -> None:
        self.rows_indices = [i for i in range(1, length_side + 1)]  # 1, 2, 3, ...
        self.columns_indices = [chr(ord('A') + i) for i in range(0, length_side)]  # A, B, C ...

        # Definition of the content of the grid. Every square is initialized as empty.
        self.squares = {}
        for column_indice in self.columns_indices:
            self.squares[column_indice] = {}
            for row_indice in self.rows_indices:
                self.squares[column_indice][row_indice] = Square()

    def hit(self, col, row) -> bool:
        if self.squares[col][row].has_boat and not self.squares[col][row].is_hit:
            self.squares[col][row].set_hit(True)
            return True
        else:
            return False

    def place_boat(self, col, row, boat_size, direction):
        """
        Check if the boat is placeable or not.
        If not, throws an error.
        If yes, returns the coordinates.
        """
        try:
            positions = self.compute_positions(col, row, boat_size, direction)
        except Exception as ex:
            raise Exception(f"Boat cannot be placed because of {ex}")

        # Check that a boat is not already there.
        for position in positions:
            _col = position[0]
            _row = position[1]
            if self.squares[_col][_row].has_boat:
                raise Exception("Boat cannot be placed because of boat already there !")

        # Then verify that the placement is okay according to the ruleset.
        for position in positions:
            _col = position[0]
            _row = position[1]
            for neighbor in self.get_neighbors(_col, _row):
                if neighbor.has_boat:
                    raise Exception("Boat cannot be placed because of boat next to it.")

        # Finally place the ship.
        for position in positions:
            _col = position[0]
            _row = position[1]
            self.squares[_col][_row].set_boat(True)

    def compute_positions(self, col, row, boat_size, direction) -> list[tuple]:
        """
        Compute the positions of a boat of size 'boat_size', in direction 'direction'
        and starting at position ('col', 'row')
        Returns the positions as an array of tuple.
        """
        positions = []

        col_index = self.columns_indices.index(col)
        row_index = self.rows_indices.index(row)

        try:
            for i in range(boat_size):
                if direction == Direction.EAST:
                    col_pos = self.columns_indices[col_index + i]
                    positions.append((col_pos, row))
                elif direction == Direction.SOUTH:
                    row_pos = self.rows_indices[row_index + i]
                    positions.append((col, row_pos))
        except Exception as ex:
            raise Exception(f"Invalid position for boat_size {boat_size} and direction {direction}")
        return positions

    def get_square(self, col_index, row_index) -> Square:
        """
        Get the square located to the col, row position with col
        and row integer indices of self.rows_indices and self.column_indices.
        Throws an exception if col, row not a valid position.
        """
        if col_index < 0 or col_index >= len(self.columns_indices) or row_index < 0 or row_index >= len(
                self.rows_indices):
            raise Exception("Invalid coordinates")
        col = self.columns_indices[col_index]
        row = self.rows_indices[row_index]
        return self.squares[col][row]

    def get_neighbors(self, col, row) -> list[Square]:
        """
        Get the neighbors of a specific square located at (col, row)
        """
        col_index = self.columns_indices.index(col)
        row_index = self.rows_indices.index(row)

        neighbors = []
        self.append_neighbor(neighbors, col_index, row_index - 1)  # North neighbor
        self.append_neighbor(neighbors, col_index + 1, row_index)  # East neighbor
        self.append_neighbor(neighbors, col_index, row_index + 1)  # South neighbor
        self.append_neighbor(neighbors, col_index - 1, row_index)  # West neighbor
        self.append_neighbor(neighbors, col_index + 1, row_index - 1)  # North-East neighbor
        self.append_neighbor(neighbors, col_index + 1, row_index + 1)  # South-East neighbor
        self.append_neighbor(neighbors, col_index - 1, row_index - 1)  # North-West neighbor
        self.append_neighbor(neighbors, col_index - 1, row_index + 1)  # South-West neighbor
        return neighbors

    def append_neighbor(self, neighbors, col_index, row_index):
        try:
            square = self.get_square(col_index, row_index)
            neighbors.append(square)
        except:
            pass  # Dégagez y'a rien à voir !


# TODO : Montrer à Grégoire cette manière de débug
if __name__ == "__main__":
    a = Grid(10)
    print(a.get_neighbors('J', 10))
