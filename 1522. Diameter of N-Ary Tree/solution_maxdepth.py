"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def diameter(self, root: 'Node') -> int:
        """
        :type root: 'Node'
        :rtype: int
        """
        diameter = 0

        def maxDepth(node, curr_depth):
            nonlocal diameter

            if len(node.children) == 0:
                return curr_depth
            
            max_depth1, max_depth2 = curr_depth, 0

            for child in node.children:
                depth = maxDepth(child, curr_depth + 1)

                if depth > max_depth1:
                    max_depth1, max_depth2 = depth, max_depth1
                elif depth > max_depth2:
                    max_depth2 = depth
            
            dist = max_depth1 + max_depth2 - 2 * curr_depth
            diameter = max(diameter, dist)

            return max_depth1
        
        maxDepth(root, 0)

        return diameter
