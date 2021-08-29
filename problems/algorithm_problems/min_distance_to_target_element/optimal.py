

class Solution:
    def getMinDistance(self, nums: list[int], target: int, start: int) -> int:
        """
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        min_distance_to_target = len(nums)  # max possible value + 1
        for index, number in enumerate(nums):
            if number == target:
                current_distance: int = abs(index - start)
                min_distance_to_target = min(
                    current_distance,
                    min_distance_to_target
                )
        return min_distance_to_target


if __name__ == '__main__':
    solution = Solution()
    print(solution.getMinDistance(nums=[1, 2, 3, 4, 5], target=5, start=3))
    print(solution.getMinDistance(nums=[1], target=1, start=0))
    print(solution.getMinDistance(nums=[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], target=1, start=0))
