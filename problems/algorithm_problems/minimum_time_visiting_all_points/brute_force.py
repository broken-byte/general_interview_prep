

class Solution:
    """
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    class Point:
        def __init__(self, point_raw: list[int]):
            self.x = point_raw[0]
            self.y = point_raw[1]

    def minTimeToVisitAllPoints(self, points: list[list[int]]) -> int:
        n = len(points)
        min_time = 0
        for index in range(n - 1):
            current_point = Solution.Point(points[index])
            next_point = Solution.Point(points[index + 1])
            min_time += self._number_of_diagonal_moves(current_point, next_point) \
                + self._number_of_non_diagonal_moves(current_point, next_point)
        return min_time

    @staticmethod
    def _number_of_diagonal_moves(p1: Point, p2: Point) -> int:
        delta_x: int = abs(p1.x - p2.x)
        delta_y: int = abs(p1.y - p2.y)
        return min(delta_x, delta_y)

    @staticmethod
    def _number_of_non_diagonal_moves(p1: Point, p2: Point) -> int:
        delta_x: int = abs(p1.x - p2.x)
        delta_y: int = abs(p1.y - p2.y)
        return abs(delta_x - delta_y)


if __name__ == '__main__':
    solution = Solution()
    print(solution.minTimeToVisitAllPoints([[1, 1], [3, 4], [-1, 0]]))
