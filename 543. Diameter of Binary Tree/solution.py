# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        output = [0]

        def dfs(root):
            if not root:
                return -1
            
            left = dfs(root.left)
            right = dfs(root.right)

            diameter = 2 + left + right

            output[0] = max(output[0], diameter)

            return 1 + max(left, right)
        
        dfs(root)

        return output[0]
