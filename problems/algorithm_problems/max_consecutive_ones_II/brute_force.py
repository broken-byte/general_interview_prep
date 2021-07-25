
class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        """
        Time Complexity: O(N^2)
        Space Complexity: O(1)
        """
        max_consecutive_ones, n = 0, len(nums)
        for start in range(n):
            consecutive_count = get_consecutive_count_from_start(start, nums)
            max_consecutive_ones = max(max_consecutive_ones, consecutive_count)
        return max_consecutive_ones


def get_consecutive_count_from_start(start: int, nums: list[int]) -> int:
    did_flip_zero, n = False, len(nums)
    consecutive_count = 0
    for i in range(start, n):
        current = nums[i]
        if current == 1:
            consecutive_count += 1
        elif current != 1 and not did_flip_zero:
            consecutive_count += 1
            did_flip_zero = True
        elif current != 1 and did_flip_zero:
            break
    return consecutive_count


if __name__ == '__main__':
    solution = Solution()
    print(solution.findMaxConsecutiveOnes(nums=[1, 0, 1, 1, 0]))
    print(solution.findMaxConsecutiveOnes(nums=[1, 0, 1, 1, 0, 1]))



