

class Solution:
    def minStartValue(self, nums: list[int]) -> int:
        """
        Time Complexity: O(N)
        Space Complexity: O(1)
        """
        initial_value = 1
        step_by_step_sum = initial_value
        for num in nums:
            step_by_step_sum += num
            if step_by_step_sum < 1:
                difference = 1 - step_by_step_sum
                initial_value += difference
                step_by_step_sum = 1
        return initial_value


if __name__ == '__main__':
    solution = Solution()
    print(solution.minStartValue(nums=[-3, 2, -3, 4, 2]))
