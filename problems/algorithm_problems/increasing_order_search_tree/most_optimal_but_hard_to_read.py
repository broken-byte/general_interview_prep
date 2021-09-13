from typing import Optional

from test_utilities.leetcode_tree_builder import build_tree


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def increasingBST(self, root: Optional[TreeNode], next_node=None) -> Optional[TreeNode]:
        """
        n = number of nodes in tree
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        if root is None:
            return root
        head = self.increasingBST(root.left, root) if root.left is not None else root
        root.left = None
        root.right = self.increasingBST(root.right, next_node) if root.right is not None else next_node
        return head


if __name__ == '__main__':
    solution = Solution()
    root_1 = build_tree('[5,3,6,2,4,null,8,1,null,null,null,7,9]')
    result_root_check = solution.increasingBST(root_1)
