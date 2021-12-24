from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Time Complexity: O(Nlog(N))
    Space Complexity: O(N)
    """
    def sortedArrayToBST(self, nums: list[int]) -> Optional[TreeNode]:
        if len(nums) == 0:
            return None
        median_index = len(nums) // 2
        left_nums = nums[:median_index]  # O(N)
        right_nums = nums[median_index + 1:]  # O(N)
        parent = TreeNode(
            val=nums[median_index],
            left=self.sortedArrayToBST(left_nums),
            right=self.sortedArrayToBST(right_nums)
        )
        return parent


if __name__ == '__main__':
    solution = Solution()
    # root_0 = solution.sortedArrayToBST(nums=[1, 3])
    # root_1 = solution.sortedArrayToBST(nums=[-10, -3, 0, 5, 9])
    root_2 = solution.sortedArrayToBST(
        nums=[-10, -3, 0, 1, 2, 4, 8, 9, 12]
    )
    print(root_2)
