"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        left_most = root

        while left_most:
            curr = left_most
            left_most, prev = None, None

            while curr:
                if curr.left:
                    if not left_most:
                        left_most = curr.left
                    
                    if prev:
                        prev.next = curr.left
                    
                    prev = curr.left
                
                if curr.right:
                    if not left_most:
                        left_most = curr.right
                    
                    if prev:
                        prev.next = curr.right
                    
                    prev = curr.right
                curr = curr.next
        
        return root
