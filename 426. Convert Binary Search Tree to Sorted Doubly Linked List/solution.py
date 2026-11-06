"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None
        
        first, last = None, None

        def inorder(node):
            nonlocal last, first

            if node:
                inorder(node.left)

                if last:
                    last.right = node
                    node.left = last
                else:
                    first = node
                last = node

                inorder(node.right)
        
        inorder(root)

        last.right = first
        first.left = last

        return first
        
