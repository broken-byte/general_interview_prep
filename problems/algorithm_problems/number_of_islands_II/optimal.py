from numpy import zeros
from typing import List
from collections import defaultdict


# TODO: Why is this slower than my previous solution? (with sets)

class Solution:
    def __init__(self):
        self.grid = []
        self.islands = defaultdict(set)
        self.island_id = 0
        self.result = []
        self.rows = 0
        self.cols = 0

    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        self.grid = zeros((m, n), dtype=int)
        self.rows = m
        self.cols = n
        for index, (row, col) in enumerate(positions):
            self.add_land(row, col)
            self.result.append(len(self.islands))
        return self.result

    def add_land(self, row: int, col: int):
        if self.grid[row][col] == 1:  # Repeat add operation, do nothing
            return
        self.grid[row][col] = 1
        neighbors: set = self.get_neighbors(row, col)
        islands_in_common = self.get_common_island_ids(neighbors)
        if len(islands_in_common) == 0:
            self.islands[self.island_id] = {(row, col)}
            self.island_id += 1
        elif len(islands_in_common) == 1:
            self.islands[islands_in_common[0]].add((row, col))
        else:
            self.merge_islands(row, col, islands_in_common)

    def get_neighbors(self, row, col) -> set:
        directions: dict = {
            "UP": (-1, 0),
            "DOWN": (1, 0),
            "LEFT": (0, -1),
            "RIGHT": (0, 1)
        }
        neighbors: set = set()
        for v_row, v_col in directions.values():
            neighbor_row = row + v_row
            neighbor_col = col + v_col
            if 0 <= neighbor_row < self.rows and 0 <= neighbor_col < self.cols:
                neighbor = (neighbor_row, neighbor_col)
                neighbors.add(neighbor)
        return neighbors

    def get_common_island_ids(self, neighbors: set):
        islands_in_common = []
        for island_id, island in self.islands.items():
            if island & neighbors:
                islands_in_common.append(island_id)
        return islands_in_common

    def merge_islands(self, row: int, col: int, island_ids: List[int]):
        new_island: set = self.islands[island_ids[0]].copy()
        new_island.add((row, col))
        new_island_id: int = island_ids[0]
        for island_id in island_ids:
            new_island.update(self.islands[island_id].copy())
            self.islands.pop(island_id)
        self.islands[new_island_id] = new_island


if __name__ == '__main__':
    solution = Solution()
    result = solution.numIslands2(m = 3, n = 3, positions = [[0,0],[0,1],[1,2],[2,1]])
    print(result)

    new_solution = Solution()
    result = new_solution.numIslands2(m=3, n=3, positions=[[0,0],[0,1],[1,2],[1,2]])
    print(result)

    new_new_solution = Solution()
    result = new_new_solution.numIslands2(9, 9, positions=[[8,5],[8,0],[3,4],[0,3],[1,0],[5,4],[0,8],[5,7],[0,6],[6,2],[4,7],[2,7],[8,7],[8,6],[5,3],[2,3],[3,5],[3,1],[0,2],[8,8],[6,4],[0,1],[0,4],[7,5],[3,0]])
    print(result)
    print(f"expected: \n{[1,2,3,4,5,6,7,8,9,10,10,11,12,11,11,12,12,13,13,13,13,13,13,13,13]}")

