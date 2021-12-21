

class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        start, end = 0, len(nums) - 1
        while start <= end:
            if nums[start] == val:
                swap(nums, start, end)
                end -= 1
            else:
                start += 1
        return start


def swap(nums: list[int], i: int, j: int) -> None:
    nums[i], nums[j] = nums[j], nums[i]


if __name__ == '__main__':
    solution = Solution()
    print(solution.removeElement([3, 2, 2, 3], 3))
