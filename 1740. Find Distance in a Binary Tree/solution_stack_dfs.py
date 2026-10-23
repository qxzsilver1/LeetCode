# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDistance(self, root: Optional[TreeNode], p: int, q: int) -> int:
        parent = {root.val: -1}
        stack = [root]
        
        while stack:
            node = stack.pop()
            
            for child in (node.left, node.right):
                if child:
                    parent[child.val] = node.val
                    stack.append(child)
        
        ancestors = {}
        v = p
        
        while v != -1:
            ancestors[v] = len(ancestors)
            v = parent[v]
        
        v, distance = q, 0
        
        while v not in ancestors:
            distance += 1
            v = parent[v]
        return distance + ancestors[v]
