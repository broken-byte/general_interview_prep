from test_utilities.leetcode_tree_builder import build_tree


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        """
        n = number of nodes in tree
        Time Complexity: O(n) or ~2(n)
        Space Complexity: O(n) or ~2(n)
        """
        in_order_node_values: list = get_in_order_traversal_iteratively(root)
        result_root = TreeNode(in_order_node_values[0])
        current_node = result_root
        for index in range(1, len(in_order_node_values)):
            current_node.right = TreeNode(in_order_node_values[index])
            current_node = current_node.right
        return result_root


def get_in_order_traversal_iteratively(root: TreeNode) -> list[int]:
    in_order_values = []
    stack: list[TreeNode] = []
    current: TreeNode = root
    while len(stack) > 0 or current is not None:
        if current is not None:
            stack.append(current)
            current: TreeNode = current.left
        else:
            current: TreeNode = stack.pop()
            in_order_values.append(current.val)
            current: TreeNode = current.right
    return in_order_values


if __name__ == '__main__':
    solution = Solution()
    root_1 = build_tree('[5,3,6,2,4,null,8,1,null,null,null,7,9]')
    result_root_check = solution.increasingBST(root_1)
    print(result_root_check)



