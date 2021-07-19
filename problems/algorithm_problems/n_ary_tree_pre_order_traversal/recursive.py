

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def preorder(self, root: 'Node') -> list[int]:
        if root is None:
            return []
        elif root.children is None:
            return [root.val]
        traversal_path = [root.val]
        for child in root.children:
            child_traversal: list[int] = self.preorder(child)
            traversal_path.extend(child_traversal)
        return traversal_path


