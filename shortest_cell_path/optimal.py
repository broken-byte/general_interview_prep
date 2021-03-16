from typing import List

from test_utilities.dynamic_test_creator import dynamically_generate_tests, run_dynamic_tests
from shortest_cell_path.test_resources.functionality_test_data import functionality_test_data


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
    n = len(grid)
    m = len(grid[0])
    left = (row, col - 1)
    right = (row, col + 1)
    up = (row - 1, col)
    down = (row + 1, col)
    potential_neighbors = [left, right, up, down]
    neighbors = []
    for neigh_row, neigh_col in potential_neighbors:
        if neighbor_is_in_bounds(neigh_row, neigh_col, n, m) and neighbor_is_open(grid[neigh_row][neigh_col]):
            neighbors.append((neigh_row, neigh_col))
    return neighbors


def neighbor_is_in_bounds(row, col, n, m):
    return 0 <= row < n and \
           0 <= col < m


def neighbor_is_open(neighbor_value):
    return neighbor_value == 1


if __name__ == '__main__':
    dynamically_generate_tests(functionality_test_data, optimal, timed=True)
    run_dynamic_tests()
