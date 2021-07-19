from typing import List


def spiral_copy(input_matrix: List[List[int]]) -> List[int]:
    visited = set()
    spiral_copy_result = []
    current_position = (0, 0)
    number_of_elements = len(input_matrix) * len(input_matrix[0])
    while len(spiral_copy_result) < number_of_elements:
        current_position = copy_traverse('RIGHT', current_position, visited, spiral_copy_result, input_matrix)
        current_position = copy_traverse('DOWN', current_position, visited, spiral_copy_result, input_matrix)
        current_position = copy_traverse('LEFT', current_position, visited, spiral_copy_result, input_matrix)
        current_position = copy_traverse('UP', current_position, visited, spiral_copy_result, input_matrix)
    return spiral_copy_result


def copy_traverse(direction, current_position, visited, spiral_copy_result, input_matrix):
    directions = {
        'RIGHT': (0, 1),
        'DOWN': (1, 0),
        'LEFT': (0, -1),
        'UP': (-1, 0)
    }
    rows = len(input_matrix)
    cols = len(input_matrix[0])
    if current_position not in visited:  # First traversal edge case
        copied_value = input_matrix[current_position[0]][current_position[1]]
        spiral_copy_result.append(copied_value)
    while True:
        visited.add(current_position)
        vector_row, vector_col = directions[direction]
        next_row, next_col = current_position[0] + vector_row, current_position[1] + vector_col
        if in_bounds(next_row, next_col, rows, cols) and (next_row, next_col) not in visited:
            copied_value = input_matrix[next_row][next_col]
            spiral_copy_result.append(copied_value)
            current_position = (next_row, next_col)
        else:
            break
    return current_position


def in_bounds(next_row, next_col, rows, cols):
    return 0 <= next_row < rows and 0 <= next_col < cols


if __name__ == '__main__':
    inputMatrix = [[1, 2, 3, 4, 5],
                   [6, 7, 8, 9, 10],
                   [11, 12, 13, 14, 15],
                   [16, 17, 18, 19, 20]]
    print(spiral_copy(inputMatrix))
    print([1, 2, 3, 4, 5, 10, 15, 20, 19, 18, 17, 16, 11, 6, 7, 8, 9, 14, 13, 12])



