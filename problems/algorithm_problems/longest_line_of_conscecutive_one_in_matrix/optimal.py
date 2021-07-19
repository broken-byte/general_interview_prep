from typing import List

from numpy import zeros


class Solution:

    def __init__(self):
        self.rows: int = 0
        self.cols: int = 0
        self.graph: List[List[int]] = []
        self.dp: List[List[List[int]]] = []

    def longestLine(self, M: List[List[int]]) -> int:
        if len(M) == 0:
            return 0
        self.rows = len(M)
        self.cols = len(M[0])
        self.graph = M
        self.create_cache()
        longest_line: int = 0
        for row in range(self.rows):
            for col in range(self.cols):
                if self.graph[row][col] == 1:
                    self.cache_horizontal_progression(row, col)
                    self.cache_vertical_progression(row, col)
                    self.cache_diagonal_progression(row, col)
                    self.cache_anti_diagonal_progression(row, col)
                longest_line = \
                    max(
                        longest_line,
                        self.dp[row][col][0],
                        self.dp[row][col][1],
                        self.dp[row][col][2],
                        self.dp[row][col][3]
                    )

        return longest_line

    def create_cache(self):
        self.dp = zeros((self.rows, self.cols, 4), dtype=int)

    def cache_horizontal_progression(self, row: int, col: int):
        if col > 0:
            self.dp[row][col][0] = self.dp[row][col - 1][0] + 1  # Previous (left) horizontal cache + 1
        else:
            self.dp[row][col][0] = 1

    def cache_vertical_progression(self, row: int, col: int):
        if row > 0:
            self.dp[row][col][1] = self.dp[row - 1][col][1] + 1  # Previous (top) vertical cache + 1
        else:
            self.dp[row][col][1] = 1

    def cache_diagonal_progression(self, row: int, col: int):
        if row > 0 and col > 0:
            self.dp[row][col][2] = self.dp[row - 1][col - 1][2] + 1  # Previous (top-left) diagonal cache + 1
        else:
            self.dp[row][col][2] = 1

    def cache_anti_diagonal_progression(self, row: int, col: int):
        if row > 0 and col < self.cols - 1:
            self.dp[row][col][3] = self.dp[row - 1][col + 1][3] + 1  # Previous (top-right) anti-diagonal cache + 1
        else:
            self.dp[row][col][3] = 1


if __name__ == '__main__':
    solution = Solution()
    print(solution.longestLine(
        [
            [0, 1, 1, 0],
            [0, 1, 1, 0],
            [0, 0, 0, 1]
        ]
    ))
    print(solution.longestLine([[1,1,1,1],[0,1,1,0],[0,0,0,1]]))
