from typing import Optional

from test_utilities.leetcode_tree_builder import build_tree


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def __init__(self):
        self.current_node = None

    def increasingBST(self, root):
        """
        n = number of nodes in tree
        Time Complexity: O(n)
        Space Complexity: O(height of tree)
        """

        def inorder(node: Optional[TreeNode]):
            if node is not None:
                inorder(node.left)
                node.left = None
                self.current_node.right = node
                self.current_node = node
                inorder(node.right)

        super_root = TreeNode(val=-1)
        self.current_node = super_root
        inorder(root)
        return super_root.right


if __name__ == '__main__':
    solution = Solution()
    root_1 = build_tree('[5,3,6,2,4,null,8,1,null,null,null,7,9]')
    result_root_check = solution.increasingBST(root_1)
    print(result_root_check)



