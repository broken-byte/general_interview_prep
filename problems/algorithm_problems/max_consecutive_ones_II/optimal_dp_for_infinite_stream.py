

class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        """
        Time Complexity: O(n)
        Space Complexity: O(1)
        Algorithm: Dynamic Programming

        Assumptions: max_if_flipped will
        always be greater than or equal to
        max_if_not_flipped
        """
        max_all = 0
        max_if_flipped = 0
        max_if_not_flipped = 0
        for val in nums:
            if val == 1:
                max_if_flipped += 1
                max_if_not_flipped += 1
                max_all = max(max_all, max_if_flipped)
            else:
                max_if_flipped = max_if_not_flipped + 1
                max_if_not_flipped = 0
                max_all = max(max_all, max_if_flipped)
        return max_all
