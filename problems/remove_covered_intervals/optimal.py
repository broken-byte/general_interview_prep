

class Solution:
    def removeCoveredIntervals(self, intervals: list[list[int]]) -> int:
        """
        Sort intervals by start values, do a linear search and count non covered intervals
        Time Complexity: O(nlog(n)) # sorting cost
        Space Complexity: O(1)
        """
        # sort by start, unless starts are equal, in which case sort by end
        intervals.sort(key=lambda x: (x[0], -x[1]))
        prev_end = 0
        count_of_non_covered_intervals = 0
        for _, end in intervals:
            if not_covered(end, prev_end):
                count_of_non_covered_intervals += 1
                prev_end = end
        return count_of_non_covered_intervals


def not_covered(end: int, previous_end: int) -> bool:
    return end > previous_end


if __name__ == '__main__':
    solution = Solution()
    print(f'expected: 2, actual: {solution.removeCoveredIntervals([[1,4],[3,6],[2,8]])}')
    print(f'expected: 1, actual: {solution.removeCoveredIntervals([[1,4],[2,3]])}')
    print(f'expected: 2, actual: {solution.removeCoveredIntervals([[0,10],[5,12]])}')
    print(f'expected: 2 actual: {solution.removeCoveredIntervals([[3,10],[4,10],[5,11]])}')
    print(f'expected: 1, actual: {solution.removeCoveredIntervals([[1,2],[1,4],[3,4]])}')
    print(f'expected: 2 actual: {solution.removeCoveredIntervals([[34335,39239],[15875,91969],[29673,66453],[53548,69161],[40618,93111]])}')