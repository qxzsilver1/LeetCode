"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        p_copy = p
        q_copy = q

        while p_copy != q_copy:
            q_copy = q_copy.parent if q_copy else p
            p_copy = p_copy.parent if p_copy else q
        
        return p_copy
