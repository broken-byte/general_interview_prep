from collections import deque

from problems.longest_consecutive_sequence_BST.tree_builder import construct_tree_from_nodes, print_level_order


class Solution:

    # Definition for a binary tree node.
    class TreeNode:
        def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right

    def longestConsecutive(self, root: TreeNode) -> int:
        pass


if __name__ == '__main__':
    tree_nodes: list = [1, None, 3, 2, 4, None, None, None, 5]
    solution: Solution = Solution()
    root_node = construct_tree_from_nodes(tree_nodes)
    print_level_order(root_node)
    print(solution.longestConsecutive(root_node))

    tree_nodes = [2,None,3,2,None,1]
    root_node = construct_tree_from_nodes(tree_nodes)
    print_level_order(root_node)
    print(solution.longestConsecutive(root_node))

