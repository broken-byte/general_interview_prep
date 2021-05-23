

class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> list[list[int]]:
        return spiral_traversal(rStart, cStart, rows, cols)


def spiral_traversal(rStart: int, cStart: int, rows: int, cols: int) -> list[list[int]]:
    spiral_pattern_map = get_spiral_pattern_map()
    spiral_ordering = ["RIGHT", "DOWN", "LEFT", "UP"]
    n: int = rows*cols
    result: list[list[int]] = []
    current_coordinates: list[int] = [rStart, cStart]
    result.append(current_coordinates.copy())
    if len(result) == n:
        return result
    while True:
        for direction in spiral_ordering:
            vector: GridVector = spiral_pattern_map[direction]["vector"]
            repetitions: int = spiral_pattern_map[direction]["repetitions"]
            for _ in range(repetitions):
                current_coordinates[0] += vector.row
                current_coordinates[1] += vector.col
                if in_bounds(current_coordinates, rows, cols):
                    result.append(current_coordinates.copy())
                if len(result) == n:
                    return result
            spiral_pattern_map[direction]["repetitions"] += 2


def get_spiral_pattern_map() -> dict:
    return {
        "RIGHT": {
            "vector": GridVector(0, 1),
            "repetitions": 1
        },
        "DOWN": {
            "vector": GridVector(1, 0),
            "repetitions": 1
        },
        "LEFT": {
            "vector": GridVector(0, -1),
            "repetitions": 2
        },
        "UP": {
            "vector": GridVector(-1, 0),
            "repetitions": 2
        }
    }


class GridVector:
    def __init__(self, row: int, col: int):
        self.row = row
        self.col = col


def in_bounds(coordinates: list, rows: int, cols: int) -> bool:
    current_row: int = coordinates[0]
    current_col: int = coordinates[1]
    return 0 <= current_row < rows and 0 <= current_col < cols
