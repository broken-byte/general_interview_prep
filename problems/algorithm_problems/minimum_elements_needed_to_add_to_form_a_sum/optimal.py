import math


class Solution:
    def minElements(self, nums: list[int], limit: int, goal: int) -> int:
        difference = sum(nums) - goal
        number_of_elements_to_add: float = abs(difference) / limit
        return math.ceil(number_of_elements_to_add)


if __name__ == '__main__':
    solution = Solution()
    print(solution.minElements(nums=[1, -1, 1], limit=3, goal=-4))
    print(solution.minElements(nums=[1, -10, 9, 1], limit=100, goal=0))
