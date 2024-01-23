# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        max_dist = 0
        
        def dfs(root, start):
            nonlocal max_dist

            dist = 0
            if not root:
                return dist
            
            left = dfs(root.left, start)
            right = dfs(root.right, start)

            if root.val == start:
                max_dist = max(left, right)
                dist = -1
            elif left >= 0 and right >= 0:
                dist = max(left, right) + 1
            else:
                max_dist = max(max_dist, abs(left) + abs(right))
                dist = min(left, right) - 1
            
            return dist
        
        dfs(root, start)

        return max_dist
