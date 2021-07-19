from test_utilities.dynamic_test_creator import dynamically_generate_tests, run_dynamic_tests
from problems.algorithm_problems.dynamic_programming.grid_traveler.test_resources.time_complexity_test_data import time_complexity_test_data


def optimal(n: int, m: int, source: list, target: list) -> int:
    """
    Time Complexity: O(n*m)
    Space Complexity: O(n*m)
    """
    if grid_is_invalid(n, m):
        return 0
    if source_and_target_not_at_edges(n, m, source, target):
        n, m = get_sub_grid_from_source_to_target(n, m, source, target)
    dp = [
        [0 for _ in range(m)] for _ in range(n)
    ]
    dp[n - 1][m - 1] = 1
    for row in range(n - 1, -1, -1):
        for col in range(m - 1, -1, -1):
            neighbors: list = get_neighbors(n, m, row, col)
            if dp[row][col] == 0:
                for n_row, n_col in neighbors:
                    dp[row][col] += dp[n_row][n_col]
    return dp[0][0]


def grid_is_invalid(n: int, m: int) -> bool:
    return n is 0 or m is 0


def source_and_target_not_at_edges(n, m, source, target) -> bool:
    source_row, source_col = source
    target_row, target_column = target
    return (source_row, source_col) != (0, 0) and \
           (target_row, target_column) != (n - 1, m - 1)


def get_sub_grid_from_source_to_target(n, m, source, target) -> tuple:
    source_row: int = source[0]
    target_column: int = target[1]
    n_from_source_to_target: int = n - source_row
    m_from_source_to_target: int = m - target_column
    return n_from_source_to_target, m_from_source_to_target


def get_neighbors(n, m, row, col) -> list:
    right: tuple = (row, col + 1)
    down: tuple = (row + 1, col)
    potential_neighbors: list = [right, down]
    actual_neighbors: list = []
    for n_row, n_col in potential_neighbors:
        if not n_row > (n - 1) and \
                not n_col > (m - 1):
            actual_neighbors.append((n_row, n_col))
    return actual_neighbors


if __name__ == '__main__':
    dynamically_generate_tests(time_complexity_test_data, optimal, timed=True)
    run_dynamic_tests()

