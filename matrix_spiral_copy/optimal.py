from typing import List


def optimal(input_matrix: List[List[int]]) -> List[int]:
    n, m = len(input_matrix), len(input_matrix[0])
    row, col = len(input_matrix), len(input_matrix[0])
    loop_bound_row, loop_bound_col = row, col
    output = []
    i, j = 0, 0
    while len(output) < n*m:
        j = go_right(input_matrix, i, j, col, output)
        col -= 1
        i = go_down(input_matrix, i, j, row, output)


def go_right(input_matrix: List[List[int]], i, j, col, output: List[int]) -> int:
    while j < col:
        output.append(input_matrix[i][j])
        j += 1
    return j


def go_down(input_matrix: List[List[int]], i, j, col, output: List[int]) -> int:
    # TODO: Not done yet
    return 0
