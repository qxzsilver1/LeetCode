# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        res = None
        max_depth = -1

        def dfs(node, depth):
            nonlocal max_depth, res

            if not node:
                return -1
            
            if not node.left and not node.right:
                if depth > max_depth:
                    res = node
                    max_depth = depth
                
                return depth
            
            left_depth = dfs(node.left, depth + 1)
            right_depth = dfs(node.right, depth + 1)

            if left_depth == right_depth == max_depth:
                res = node
            
            return max(left_depth, right_depth)

        dfs(root, 0)

        return res
