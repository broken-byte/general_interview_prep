import unittest

from leetcode_tree_builder import TreeNode, build_tree


class TestTreeBuilder(unittest.TestCase):

    def test_that_tree_builder_can_build_tree_from_valid_input(self):
        leet_code_tree_input = '[5,3,6,2,4,null,8,1,null,null,null,7,9]'
        result_root: TreeNode = build_tree(leet_code_tree_input)
        expected_in_order_traversal = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        actual_in_order_traversal: list = self.get_in_order_traversal_given_root(result_root)
        self.assertEqual(expected_in_order_traversal, actual_in_order_traversal)

    def test_that_tree_builder_can_return_none_from_empty_input(self):
        leet_code_tree_input = ''
        result = build_tree(leet_code_tree_input)
        expected = None
        self.assertEqual(expected, result)

    def get_in_order_traversal_given_root(self, root: TreeNode) -> list:
        if root is None:
            return []
        if is_leaf(root):
            return [root.val]
        in_order_traversal_path: list[int] = []
        left_path: list[int] = self.get_in_order_traversal_given_root(root.left)
        in_order_traversal_path.extend(left_path)
        in_order_traversal_path.append(root.val)
        right_path: list[int] = self.get_in_order_traversal_given_root(root.right)
        in_order_traversal_path.extend(right_path)
        return in_order_traversal_path


def is_leaf(node: TreeNode) -> bool:
    return node.left is None and node.right is None


