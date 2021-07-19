from typing import List


class Solution:

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        N = len(matrix) or number of rows
        M = len(matrix[0]) or number of columns

        Time Complexity: O(N + M)

        Space Complexity: O(1)
        """
        rows: int = len(matrix)
        cols: int = len(matrix[0])
        current_row: int = rows - 1
        current_col: int = 0
        while current_row >= 0 and current_col < cols:
            current_element: int = matrix[current_row][current_col]
            if target == current_element:
                return True
            elif target < current_element:
                current_row -= 1  # Go up
            elif target > current_element:
                current_col += 1  # Go right
        return False
