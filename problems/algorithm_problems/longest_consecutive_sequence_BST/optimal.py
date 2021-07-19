from problems.algorithm_problems.longest_consecutive_sequence_BST.tree_builder import construct_tree_from_nodes, print_level_order


class Solution:

    def __init__(self):
        self.max_length: int = 0

    # Definition for a binary tree node.
    class TreeNode:
        def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right

    def longestConsecutive(self, root: TreeNode) -> int:
        self.max_length = 0
        self.dfs(root, None, 0)
        return self.max_length

    def dfs(self, current_node: TreeNode, parent: any, length: int):
        if current_node is None:
            return
        if parent is not None and parent.val + 1 == current_node.val:
            length += 1
        else:
            length = 1
        self.max_length = max(self.max_length, length)
        self.dfs(current_node.left, current_node, length)
        self.dfs(current_node.right, current_node, length)


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

