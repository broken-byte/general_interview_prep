

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def preorder(self, root: 'Node') -> list[int]:
        if root is None:
            return []
        stack: list['Node'] = [root]
        output: list[int] = []
        while len(stack) != 0:
            root = stack.pop()
            output.append(root.val)
            stack.extend(reversed(root.children))
        return output
