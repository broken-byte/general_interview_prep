from typing import List
from collections import defaultdict


class Solution:
    def __init__(self):
        self.coordinate_to_uf_map = defaultdict(int)
        self.union_find: UnionFind
        self.result = []
        self.rows = 0
        self.cols = 0

    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        self.rows = m
        self.cols = n
        self.create_coordinate_to_union_find_map()
        self.union_find = UnionFind(m*n, empty_graph=True)
        for position in positions:
            self.add_land(*position)
            num_islands: int = self.get_number_of_islands()
            self.result.append(num_islands)
        return self.result

    def create_coordinate_to_union_find_map(self):
        union_find_index: int = 0
        for row in range(self.rows):
            for col in range(self.cols):
                coordinate: tuple = (row, col)
                self.coordinate_to_uf_map[coordinate] = union_find_index
                union_find_index += 1

    def add_land(self, row: int, col: int):
        self.add_coordinate_to_union_find(row, col)
        neighboring_islands = self.get_neighboring_islands(row, col)
        self.merge_neighboring_islands(neighboring_islands, current_island=(row, col))

    def add_coordinate_to_union_find(self, row: int, col: int):
        corresponding_uf_node: int = self.get_union_find_node_from_coordinate(row, col)
        if self.union_find.is_empty_node(corresponding_uf_node):
            self.union_find.add_node(corresponding_uf_node)

    def get_union_find_node_from_coordinate(self, row: int, col: int) -> int:
        coordinate: tuple = (row, col)
        corresponding_node: int = self.coordinate_to_uf_map[coordinate]
        return corresponding_node

    def get_neighboring_islands(self, row, col) -> list:
        directions: dict = {
            "UP": (-1, 0),
            "DOWN": (1, 0),
            "LEFT": (0, -1),
            "RIGHT": (0, 1)
        }
        neighboring_islands: list = []
        for v_row, v_col in directions.values():
            neighbor_row = row + v_row
            neighbor_col = col + v_col
            if 0 <= neighbor_row < self.rows and \
               0 <= neighbor_col < self.cols and \
               self.is_land(neighbor_row, neighbor_col):
                neighbor_island = (neighbor_row, neighbor_col)
                neighboring_islands.append(neighbor_island)
        return neighboring_islands

    def is_land(self, row, col):
        corresponding_uf_node: int = self.get_union_find_node_from_coordinate(row, col)
        return not self.union_find.is_empty_node(corresponding_uf_node)

    def merge_neighboring_islands(self, neighboring_islands: list, current_island: tuple):
        for island in neighboring_islands:
            self.merge_two_islands(island, current_island)

    def merge_two_islands(self, island: tuple, neighboring_island: tuple):
        island_node: int = self.get_union_find_node_from_coordinate(*island)
        neighboring_island_node: int = self.get_union_find_node_from_coordinate(*neighboring_island)
        self.union_find.union(island_node, neighboring_island_node)

    def get_number_of_islands(self) -> int:
        return self.union_find.get_number_of_connected_components()


class UnionFind:

    def __init__(self, number_of_nodes: int, empty_graph=False):
        if not empty_graph:
            self._roots: list = [i for i in range(number_of_nodes)]  # O(n)
        else:
            self._roots: list = [-1 for _ in range(number_of_nodes)]  # O(n)

        self._tree_sizes: list = [1 for _ in range(number_of_nodes)]  # O(n)

    def is_empty_node(self, node: int) -> bool:
        return self._roots[node] == -1

    def add_node(self, node: int):
        self._roots[node] = node

    def get_number_of_connected_components(self):  # O(n)
        connected_components: set = set()
        for node in self._roots:
            if node != -1:
                root = self.__get_root(node)
                connected_components.add(root)
        return len(connected_components)

    def connected(self, p: int, q: int) -> bool:  # O(log(n))
        return self.__get_root(p) == self.__get_root(q)

    def union(self, p: int, q: int) -> None:   # O(log(n))
        root_of_p: int = self.__get_root(p)  # O(log(n))
        root_of_q: int = self.__get_root(q)  # O(log(n))
        if root_of_p == root_of_q:
            return
        if self._tree_sizes[root_of_p] < self._tree_sizes[root_of_q]:  # O(1)
            self._roots[root_of_p] = root_of_q
            self._tree_sizes[root_of_q] += self._tree_sizes[root_of_p]
        else:   # O(1)
            self._roots[root_of_q] = root_of_p
            self._tree_sizes[root_of_p] += self._tree_sizes[root_of_p]

    def __get_root(self, node: int):  # O(log(n))
        while node != self._roots[node]:
            self.__compress_path(node)
            node = self._roots[node]
        return node

    def __compress_path(self, node: int):  # Set node to point to it's grandparent
        self._roots[node] = self._roots[self._roots[node]]

    def __log_union_state(self, p: int, q: int):
        print(f"union({p}, {q})")
        print([index for index in range(len(self._roots))])
        print(self._roots)

    def __log_connected_state(self, p: int, q: int):
        print(f"connected({p}, {q})")
        print(self._roots[p] == self._roots[q])


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

    new_new_solution = Solution()
    result = new_new_solution.numIslands2(3, 3,
                                          positions=[[0,1],[1,2],[2,1],[1,0],[0,2],[0,0],[1,1]])
    print(result)
    print(f"expected: \n{[1,2,3,4,3,2,1]}")
