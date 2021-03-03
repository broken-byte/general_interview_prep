from typing import List


def shortest_cell_path(grid: List[List[int]], source_row: int, source_col: int, target_row: int, target_col: int):
    visited = set()
    queue = [(source_row, source_col, 0)]
    visited.add((source_row, source_col))
    while queue:
        row, col, depth = queue.pop(0)
        if (row, col) == (target_row, target_col):
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
    left = (row - 1, col)
    right = (row + 1, col)
    up = (row, col - 1)
    down = (row, col + 1)
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
