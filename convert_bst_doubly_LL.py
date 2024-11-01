"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def __init__(self):
        self.prev = None
        self.head = None
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None
        def generate(node):
            if not node:
                return
            generate(node.left)
            if not self.prev:
                self.head = node
            else:
                self.prev.right = node
                node.left = self.prev
            self.prev = node
            generate(node.right)
        generate(root)
        self.prev.right = self.head
        self.head.left = self.prev

        return self.head