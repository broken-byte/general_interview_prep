

def num_of_paths_to_dest(n):
    """
    Time Complexity: O(n^2)
    Space Complexity: O(n)

    Since this problem, once stripped
    of the inverted traversal and (i, j)
    notation, is an incredibly easy
    "how many ways to traverse an n^n
    grid given down right movement",
    One can just solve that problem
    recursively with the only change
    being to limit the column reductions
    to stay at column >= row range
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
        right_path_traversals: int = grid_traversal(row, column - 1) if column - 1 >= row else 0
        down_path_traversals: int = grid_traversal(row - 1, column)
        memo[(row, column)] = right_path_traversals + down_path_traversals
        return memo[(row, column)]

    return grid_traversal(n, n)
