from typing import List


class Solution:

    def __init__(self):
        self.graph = List[List[int]]
        self.rows: int = 0
        self.cols: int = 0
        self.longest_line_length: int = 0
        self.cardinal_directions: dict = {
            "DOWN": (1, 0),
            "RIGHT": (0, 1),
            "DOWN-RIGHT": (1, 1),
            "DOWN-LEFT": (1, -1),
        }

    def longestLine(self, M: List[List[int]]) -> int:
        """
        Time Complexity: O(N^2*M^2)
        Space Complexity: O(N*M)
            [
                [0, 1, 1, 0],
                [0, 1, 1, 0],
                [0, 0, 0, 1]
            ]
        """
        if len(M) == 0:
            return 0
        self.rows = len(M)
        self.cols = len(M[0])
        self.graph = M
        for row in range(self.rows):
            for col in range(self.cols):
                node: tuple = (row, col)
                if self.graph[row][col] == 1:
                    for direction in self.cardinal_directions.keys():
                        self.depth_traversal(node, direction)
        return self.longest_line_length

    def depth_traversal(self, current_node: tuple, direction: str):
        line_length: int = 0
        while self.is_valid(current_node):
            line_length += 1
            next_row, next_col = [sum(x) for x in zip(current_node, self.cardinal_directions[direction])]
            current_node = (next_row, next_col)
        if line_length > self.longest_line_length:
            self.longest_line_length = line_length

    def is_valid(self, node: tuple) -> bool:
        row = node[0]
        col = node[1]
        if (0 <= row < self.rows) and (0 <= col < self.cols):
            return self.graph[row][col] == 1
        else:
            return False


if __name__ == '__main__':
    solution = Solution()
    print(solution.longestLine(
            [
                [0, 1, 1, 0],
                [0, 1, 1, 0],
                [0, 0, 0, 1]
            ]
        )
    )








