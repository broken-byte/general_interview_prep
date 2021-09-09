from typing import Optional

from test_utilities.leetcode_tree_builder import build_tree


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        """
        Time Complexity: O(n)
        Space Complexity: O(n)

        So, my guess was that if
        you took the pre order traversal from the
        left half, and the post order traversal from the right half,
        and compared the two, that symmetry would be determined
        by whether they were equal in traversal path output.
        Turns out that was wrong but it was a good guess! (IMO)

        """
        pre_order_left_path: list[Optional[int]] = pre_order_traversal(root.left)
        print(pre_order_left_path)
        post_order_right_path: list[Optional[int]] = post_order_traversal(root.right)
        print(post_order_right_path)
        return pre_order_left_path == post_order_right_path


def pre_order_traversal(current_node: Optional[TreeNode]) -> [Optional[int]]:
    if current_node is None:
        return [None]
    if is_leaf(current_node):
        return [current_node.val]
    pre_order_traversal_path: list[Optional[int]] = []
    left_path: list[Optional[int]] = pre_order_traversal(current_node.left)
    pre_order_traversal_path.extend(left_path)
    pre_order_traversal_path.append(current_node.val)
    right_path: list[Optional[int]] = pre_order_traversal(current_node.right)
    pre_order_traversal_path.extend(right_path)
    return pre_order_traversal_path


def post_order_traversal(current_node: Optional[TreeNode]) -> [Optional[int]]:
    if current_node is None:
        return [None]
    if is_leaf(current_node):
        return [current_node.val]
    post_order_traversal_path: list[Optional[int]] = []
    right_path: list[Optional[int]] = post_order_traversal(current_node.right)
    post_order_traversal_path.extend(right_path)
    post_order_traversal_path.append(current_node.val)
    left_path: list[Optional[int]] = post_order_traversal(current_node.left)
    post_order_traversal_path.extend(left_path)
    return post_order_traversal_path


def is_leaf(node: TreeNode) -> bool:
    return node.left is None and node.right is None


if __name__ == '__main__':
    build_tree('[5,4,1,null,1,null,4,2,null,2,null]')
