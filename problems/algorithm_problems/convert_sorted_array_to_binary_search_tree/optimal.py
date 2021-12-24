from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Time Complexity: O(N)
    Space Complexity: O(N)
    """
    def sortedArrayToBST(self, nums) -> Optional[TreeNode]:

        def convert(left: int, right: int) -> Optional[TreeNode]:
            if left > right:
                return None
            mid = (left + right) // 2
            parent = TreeNode(nums[mid])
            parent.left = convert(left, mid - 1)
            parent.right = convert(mid + 1, right)
            return parent
        return convert(0, len(nums) - 1)


if __name__ == '__main__':
    solution = Solution()
    # root_0 = solution.sortedArrayToBST(nums=[1, 3])
    # root_1 = solution.sortedArrayToBST(nums=[-10, -3, 0, 5, 9])
    root_2 = solution.sortedArrayToBST(
        nums=[-10, -3, 0, 1, 2, 4, 8, 9, 12])
    print(root_2)
