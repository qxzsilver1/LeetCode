"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def findRoot(self, tree: List['Node']) -> 'Node':
        val_sum = 0

        for node in tree:
            val_sum += node.val
            
            for child in node.children:
                val_sum -= child.val
        
        for node in tree:
            if node.val == val_sum:
                return node
