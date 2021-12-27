

class Solution:
    """
    Time Complexity: O(N)
    Space Complexity: O(1)
    """
    def removeDuplicates(self, nums: list[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        replacement_index = 1
        buffer = nums[0]
        for index in range(1, len(nums)):
            if nums[index] != buffer:
                buffer = nums[index]
                nums[replacement_index] = buffer
                replacement_index += 1
        return replacement_index
