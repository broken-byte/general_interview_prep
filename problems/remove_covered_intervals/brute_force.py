

class Solution:
    def removeCoveredIntervals(self, intervals: list[list[int]]) -> int:
        """
        Compare all intervals to every other interval, subtract overlapping from initial length
        Time Complexity: O(n^2)
        Space Complexity: O(n)
        """
        interval_count: int = len(intervals)
        deleted_indices = set()
        for i, first_interval in enumerate(intervals):
            for j, second_interval in enumerate(intervals):
                if i == j or i in deleted_indices or j in deleted_indices:
                    continue
                if first_is_covered(first_interval, second_interval):
                    interval_count -= 1
                    deleted_indices.add(i)

        return interval_count


def first_is_covered(first_interval: list[int], second_interval: list[int]) -> bool:
    a, b = first_interval
    c, d = second_interval
    return c <= a and b <= d


if __name__ == '__main__':
    solution = Solution()
    print(f'expected: 2, actual: {solution.removeCoveredIntervals([[1,4],[3,6],[2,8]])}')
    print(f'expected: 1, actual: {solution.removeCoveredIntervals([[1,4],[2,3]])}')
    print(f'expected: 2, actual: {solution.removeCoveredIntervals([[0,10],[5,12]])}')
    print(f'expected: 2 actual: {solution.removeCoveredIntervals([[3,10],[4,10],[5,11]])}')
    print(f'expected: 1, actual: {solution.removeCoveredIntervals([[1,2],[1,4],[3,4]])}')
    print(f'expected: 2 actual: {solution.removeCoveredIntervals([[34335,39239],[15875,91969],[29673,66453],[53548,69161],[40618,93111]])}')
