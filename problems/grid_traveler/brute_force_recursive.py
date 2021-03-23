from test_utilities.dynamic_test_creator import dynamically_generate_tests, run_dynamic_tests
from problems.grid_traveler.test_resources.functionality_test_data import functionality_test_data


def brute_force(n: int, m: int, source: list, target: list) -> int:
    """
    Time Complexity: O(2^(n + m))
    Space Complexity: O(n + m)
    """
    def grid_traversal(row: int, column: int) -> int:
        if row == 0 or column == 0:
            return 0
        elif row == 1 and column == 1:
            return 1
        else:
            right_path_traversals: int = grid_traversal(row, column - 1)
            down_path_traversals: int = grid_traversal(row - 1, column)
            return right_path_traversals + down_path_traversals

    if not source_and_target_at_edges(n, m, source, target):
        source_row: int = source[0]
        target_column: int = target[1]
        n_from_source_to_target: int = n - source_row
        m_from_source_to_target: int = m - target_column
        return grid_traversal(n_from_source_to_target, m_from_source_to_target)
    else:
        return grid_traversal(n, m)


def source_and_target_at_edges(n, m, source, target) -> bool:
    source_row, source_col = source
    target_row, target_column = target
    return (source_row, source_col) == (0, 0) and \
           (target_row, target_column) == (n - 1, m - 1)


if __name__ == '__main__':
    dynamically_generate_tests(functionality_test_data, brute_force)
    run_dynamic_tests()
