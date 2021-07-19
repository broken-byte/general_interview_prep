from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def construct_tree_from_nodes(tree_nodes: list) -> any:
    if not tree_nodes:
        return None
    root = None if tree_nodes[0] is None else TreeNode(tree_nodes[0])
    queue = deque()
    queue.append(root)
    i = 1
    while queue and i < len(tree_nodes):
        t1 = queue.popleft()
        if t1 is not None:
            t1.left = None if tree_nodes[i] is None else TreeNode(tree_nodes[i])
            queue.append(t1.left)
            i += 1
            if i >= len(tree_nodes): break
            t1.right = None if tree_nodes[i] is None else TreeNode(tree_nodes[i])
            queue.append(t1.right)
            i += 1
    return root


def print_level_order(root: TreeNode):
    queue = deque()
    queue.append(root)
    s = []
    while queue:
        node = queue.popleft()
        s.append("None" if node is None else node.val)
        if node is not None:
            queue.append(node.left)
            queue.append(node.right)
    print(", ".join(str(part) for part in s))
