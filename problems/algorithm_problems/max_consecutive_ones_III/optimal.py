

class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        """
        Time Complexity: O(N)
        Space Complexity: O(1)
        Algorithm: Sliding Window
        ---------------------------
        Our sliding window length represents the longest valid sub array length we
        have encountered so far in the iteration (valid meaning consecutive ones plus max flipped ones if needed).
        We always increase the right side of the window, and move the left side if we run out of k.
        We decrement k if we encounter a zero, and increment k if we run out of k and remove a zero from our
        window when we move the left side of the window.

        After iterating through the entire array, we return the sliding window length! :)
        """
        left, right = 0, 0
        n = len(nums)
        for right in range(n):
            if nums[right] == 0:
                k -= 1
            if k < 0 and nums[left] == 0:
                k += 1
                left += 1
            elif k < 0 and nums[left] == 1:
                left += 1
            # print(left, right, nums[left:right + 1], f'Max length: {right - left + 1}, k: {k}')
        final_window_length = right - left + 1
        return final_window_length


if __name__ == '__main__':
    solution = Solution()
    print(solution.longestOnes(nums=[1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], k=2))
    print(solution.longestOnes(nums=[0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], k=3))
