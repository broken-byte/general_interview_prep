

class Solution:
    """
    Time Complexity: O(N^2)
    Space Complexity: O(1)
    """
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        n = len(nums)
        if n == 3:
            return sum(nums)
        nums.sort()
        closest_triplet_sum_so_far: int = nums[0] + nums[1] + nums[2]
        for index in range(n):
            left = index + 1
            right = n - 1
            while left < right:
                triplet_sum: int = nums[index] + nums[left] + nums[right]
                if triplet_sum == target:
                    return triplet_sum
                if triplet_sum < target:
                    left += 1
                else:
                    right -= 1
                if difference_between(triplet_sum, target) < difference_between(closest_triplet_sum_so_far, target):
                    closest_triplet_sum_so_far = triplet_sum

        return closest_triplet_sum_so_far


def difference_between(a: int, b: int) -> int:
    return abs(a - b)


if __name__ == '__main__':
    solution = Solution()
    print(solution.threeSumClosest(nums=[-1, 2, 1, -4], target=1))
    print(solution.threeSumClosest(nums=[0, 0, 0], target=1))
    print(solution.threeSumClosest(nums=[1, 1, 1, 0], target=-100))
    print(solution.threeSumClosest(nums=[1, 1, 1, 1], target=4))
    print(solution.threeSumClosest(nums=[0, 2, 1, -3], target=1))

