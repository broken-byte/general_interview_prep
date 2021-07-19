from collections import deque
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.grid = grid
        self.n = len(grid)
        self.m = len(grid[0])
        self.visited = set()
        numIslands = 0
        for row in range(self.n):
            for col in range(self.m):
                if grid[row][col] == "1" and (row, col) not in self.visited:
                    self.bfs(row, col)
                    numIslands += 1
        return numIslands

    def bfs(self, row: int, col: int):
        queue = deque()
        current_node = (row, col)
        queue.append(current_node)
        self.visited.add(current_node)
        while len(queue) != 0:
            current = queue.popleft()
            neighbors = self.get_neighbors(*current)
            for n_node in neighbors:
                if n_node not in self.visited:
                    queue.append(n_node)
                    self.visited.add(n_node)

    def get_neighbors(self, row: int, col: int):
        directions = {
            "UP": (-1, 0),
            "DOWN": (1, 0),
            "LEFT": (0, -1),
            "RIGHT": (0, 1)
        }
        neighbors = []
        for v_row, v_col in directions.values():
            neighbor_row, neighbor_col = row - v_row, col - v_col
            if 0 <= neighbor_row < self.n and \
                    0 <= neighbor_col < self.m and \
                    self.grid[neighbor_row][neighbor_col] == "1":
                neighbor = (neighbor_row, neighbor_col)
                neighbors.append(neighbor)
        return neighbors
