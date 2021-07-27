from enum import Enum


class Solution:
    def gameOfLife(self, board: list[list[int]]) -> None:
        """
        M = Len(board)
        N = Len(board[0])
        Time Complexity: O(M*N)
        Space Complexity: O(M*N) for cell bag

        To optimize to O(1) space, I would move
        the logic of the Cell class into the solution
        class, and encode the Cell State in place as
        follows:

        class CellState(Enum):
            ALIVE_TO_ALIVE = 3
            DEAD_TO_ALIVE = 2
            ALIVE_TO_DEAD = 1
            DEAD_TO_DEAD = 0

        So that I can store all possible states
        in the board itself without losing information
        """
        m, n = len(board), len(board[0])
        cell_bag: {tuple: Cell} = {}
        for row in range(m):
            for col in range(n):
                cell_state = board[row][col]
                cell = Cell(CellState(cell_state), row, col)
                cell_bag[(row, col)] = cell
                cell.discover_surrounding_neighbor_states(board)
                cell.prepare_for_next_state()
        for row in range(m):
            for col in range(n):
                next_state: CellState = cell_bag[(row, col)].next_state
                board[row][col] = next_state.value


class CellState(Enum):
    DEAD, ALIVE = 0, 1


class Cell:

    _direction_vectors = [
        (0, 1),  # RIGHT
        (1, 0),  # DOWN
        (0, -1),  # LEFT
        (-1, 0),  # UP
        (-1, -1),  # UP_LEFT
        (-1, 1),  # UP_RIGHT
        (1, 1),  # DOWN_RIGHT
        (1, -1),  # DOWN_LEFT
    ]

    def __init__(self, state: CellState, row: int, col: int):
        self.state = state
        self.row, self.col = row, col
        self.living_neighbors = 0
        self.next_state = None

    def prepare_for_next_state(self):
        if self._is_under_populated():
            self.next_state = CellState.DEAD
        elif self._will_live_on():  # Just right
            self.next_state = CellState.ALIVE
        elif self._is_over_populated():  # Underpopulated
            self.next_state = CellState.DEAD
        elif self._can_be_resurrected():  # resurrection
            self.next_state = CellState.ALIVE
        else:
            self.next_state = CellState.DEAD

    def _is_under_populated(self) -> bool:
        return self.state == CellState.ALIVE and self.living_neighbors < 2

    def _will_live_on(self) -> bool:
        return self.state == CellState.ALIVE and self.living_neighbors == 2 or self.living_neighbors == 3

    def _is_over_populated(self) -> bool:
        return self.state == CellState.ALIVE and self.living_neighbors > 3

    def _can_be_resurrected(self) -> bool:
        return self.state == CellState.DEAD and self.living_neighbors == 3

    def discover_surrounding_neighbor_states(self, board: list[list[int]]):
        m, n = len(board), len(board[0])
        for r_vector, c_vector in Cell._direction_vectors:
            neighbor_row, neighbor_col = self.row + r_vector, self.col + c_vector
            if self._coordinate_in_bounds(neighbor_row, neighbor_col, m, n):
                neighbor: int = board[neighbor_row][neighbor_col]
                if CellState(neighbor) == CellState.ALIVE:
                    self.living_neighbors += 1

    def _coordinate_in_bounds(self, row: int, col: int, m: int, n: int) -> bool:
        return 0 <= row < m and 0 <= col < n
