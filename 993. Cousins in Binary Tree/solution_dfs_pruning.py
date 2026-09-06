# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        self.recorded_depth = None
        is_cousin = [False]
        
        def dfs(node, depth, x, y):
            if not node:
                return False
            
            if self.recorded_depth and depth > self.recorded_depth:
                return False
            
            if node.val == x or node.val == y:
                if not self.recorded_depth:
                    self.recorded_depth = depth
                
                return self.recorded_depth == depth
            
            left = dfs(node.left, depth + 1, x, y)
            right = dfs(node.right, depth + 1, x, y)

            if left and right and self.recorded_depth != depth + 1:
                is_cousin[0] = True
            
            return left or right
        
        dfs(root, 0, x, y)

        return is_cousin[0]
