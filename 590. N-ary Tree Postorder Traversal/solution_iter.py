"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        res = []

        if not root:
            return res

        stack = [(root, False)]

        while stack:
            node, visited = stack.pop()
            
            if visited:
                res.append(node.val)
            else:
                stack.append((node, True))

                for c in node.children[::-1]:
                    stack.append((c, False))
        
        return res
