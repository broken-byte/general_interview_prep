from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    N = number of nodes
    Time Complexity: O(N)
    Space Complexity: O(N)
    """
    def isSymmetric(self, root):
        if root is None:
            return True
        return is_symmetric(root.left, root.right)


def is_symmetric(left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
    if left is None and right is None:
        return True
    if left is None or right is None:
        return False

    if left.val == right.val:
        out_pair_is_symmetric: bool = is_symmetric(left.left, right.right)
        in_pair_is_symmetric: bool = is_symmetric(left.right, right.left)
        return out_pair_is_symmetric and in_pair_is_symmetric
    return False

