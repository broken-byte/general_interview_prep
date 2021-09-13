from typing import Optional

from test_utilities.leetcode_tree_builder import build_tree


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def increasingBST(self, root):

        def in_order_generator(node: Optional[TreeNode]):
            if node is not None:
                yield from in_order_generator(node.left)
                yield node.val
                yield from in_order_generator(node.right)

        super_root = TreeNode(val=-1)
        current = super_root
        for in_order_node_value in in_order_generator(root):
            current.right = TreeNode(in_order_node_value)
            current = current.right
        return super_root.right


if __name__ == '__main__':
    solution = Solution()
    root_1 = build_tree('[5,3,6,2,4,null,8,1,null,null,null,7,9]')
    result_root_check = solution.increasingBST(root_1)
    print(result_root_check)
