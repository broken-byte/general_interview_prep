

class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        """
        Time Complexity: O(2n)
        Space Complexity: O(1)
        Algorithm: Sliding Window
        """
        longest_sequence = 0
        left, right = 0, 0
        num_zeroes = 0
        while right < len(nums):  # while our window is in bounds
            if nums[right] == 0:  # add the right most element into our window
                num_zeroes += 1
            while num_zeroes == 2:  # if our window is invalid, contract our window
                if nums[left] == 0:
                    num_zeroes -= 1
                left += 1
            length_of_current_window = right - left + 1
            longest_sequence = max(longest_sequence, length_of_current_window)
            right += 1  # expand our window
        return longest_sequence


if __name__ == '__main__':
    solution = Solution()
    print(solution.findMaxConsecutiveOnes(nums=[1, 0, 1, 1, 0]))
    print(solution.findMaxConsecutiveOnes(nums=[1, 0, 1, 1, 0, 1]))
