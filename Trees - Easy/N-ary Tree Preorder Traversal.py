"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        output = []
        if root is not None:
            output.append(root.val)
            for child in root.children:
                output.extend(self.preorder(child))
        return output