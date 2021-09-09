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
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        stack: list[tuple[Optional[TreeNode], Optional[TreeNode]]] = [(root.left, root.right)]
        while len(stack) > 0:
            left, right = stack.pop()
            if left is None and right is None:
                continue
            if left is None or right is None:
                return False
            if left.val == right.val:
                stack.append((left.left, right.right))
                stack.append((left.right, right.left))
            else:
                return False
        return True
