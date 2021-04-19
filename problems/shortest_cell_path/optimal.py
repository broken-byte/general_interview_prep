from typing import List

from test_utilities.dynamic_test_creator import dynamically_generate_tests, run_dynamic_tests
from problems.shortest_cell_path.test_resources.functionality_test_data import functionality_test_data


def optimal(grid: List[List[int]], sr: int, sc: int, tr: int, tc: int):
    visited = set()
    queue = [(sr, sc, 0)]
    visited.add((sr, sc))
    while queue:
        row, col, depth = queue.pop(0)
        if (row, col) == (tr, tc):
            return depth
        neighbors = get_neighbors(row, col, grid)
        for neighbor in neighbors:
            if neighbor not in visited:
                neighbor_with_depth = (neighbor[0], neighbor[1], depth + 1)
                queue.append(neighbor_with_depth)
                visited.add(neighbor)
    return -1


def get_neighbors(row, col, grid):
    directions: dict = {
        "UP": (-1, 0),
        "DOWN": (1, 0,),
        "RIGHT": (0, 1),
        "LEFT": (0, -1)
    }
    n = len(grid)
    m = len(grid[0])
    neighbors = []
    for v_row, v_col in directions.values():
        n_row, n_col = row + v_row, col + v_col
        if 0 <= n_row < n and 0 <= n_col < m and grid[n_row][n_col] == 1:
            neighbors.append((n_row, n_col))
    return neighbors


if __name__ == '__main__':
    dynamically_generate_tests(functionality_test_data, optimal, timed=True)
    run_dynamic_tests()
