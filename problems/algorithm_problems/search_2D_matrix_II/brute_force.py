from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        N = len(matrix) or number of rows
        M = len(matrix[0]) or number of columns

        Time Complexity: O(N(log(M))

        Space Complexity: O(1)
        """
        for row in matrix:
            if self.binary_search(row, target):
                return True
        return False

    def binary_search(self, arr: list, target: int) -> bool:
        lo: int = 0
        hi: int = len(arr) - 1
        while lo <= hi:
            middle: int = (lo + hi) // 2
            if target == arr[middle]:
                return True
            elif target < arr[middle]:
                hi = middle - 1
            else:
                lo = middle + 1
        return False
