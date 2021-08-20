import heapq


class Solution:
    def smallestDistancePair(self, nums: list[int], k: int) -> int:
        """
        Time Complexity: O(N^2 + Nlog(N)) -> O(N^2)
        Space Complexity: O(N)
        """
        distances: list[int] = []
        n: int = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                first, second = nums[i], nums[j]
                distance: int = abs(second - first)
                distances.append(distance)
        return sorted(distances)[k - 1]


if __name__ == '__main__':
    solution = Solution()
    print(solution.smallestDistancePair(nums=[1, 3, 1], k=1))
    print(solution.smallestDistancePair(nums=[1, 1, 1], k=2))
    print(solution.smallestDistancePair(nums=[1, 6, 1], k=3))
