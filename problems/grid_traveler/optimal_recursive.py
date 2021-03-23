from test_utilities.dynamic_test_creator import dynamically_generate_tests, run_dynamic_tests
from problems.grid_traveler.test_resources.time_complexity_test_data import time_complexity_test_data


def optimal(n: int, m: int, source: list, target: list) -> int:
    """
    Time Complexity: O(n*m)
    Space Complexity: O(n + m)
    """
    memo: dict = {}

    def grid_traversal(row: int, column: int) -> int:
        if row == 0 or column == 0:
            return 0
        elif row == 1 and column == 1:
            return 1
        elif (row, column) in memo:
            return memo[(row, column)]
        elif (column, row) in memo:
            return memo[(column, row)]
        else:
            right_path_traversals: int = grid_traversal(row, column - 1)
            down_path_traversals: int = grid_traversal(row - 1, column)
            memo[(row, column)] = right_path_traversals + down_path_traversals
            return memo[(row, column)]

    if source_and_target_not_at_edges(n, m, source, target):
        n, m = get_sub_grid_from_source_to_target(n, m, source, target)
        return grid_traversal(n, m)
    else:
        return grid_traversal(n, m)


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


if __name__ == '__main__':
    dynamically_generate_tests(time_complexity_test_data, optimal, timed=True)
    run_dynamic_tests()
