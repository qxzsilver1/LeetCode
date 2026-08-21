# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        
        def solve(node):
            if not node:
                return 0, 0, float('inf')
            
            left = solve(node.left)
            right = solve(node.right)

            dp_strict_subtree_only = left[1] + right[1] # index 0 - all nodes below current node is covered but not this node
            dp_subtree = min(left[2] + min(right[1:]), right[2] + min(left[1:])) # index 1 - all nodes (including current node) are covered but no camera is placed at this node
            dp_camera_placed = 1 + min(left) + min(right) # index 2 - camera is placed at this node

            return dp_strict_subtree_only, dp_subtree, dp_camera_placed
        
        return min(solve(root)[1:])
