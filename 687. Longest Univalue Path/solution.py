# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        res = [0]

        def solveTree(root, parent):
            if not root:
                return 0
            
            l, r = solveTree(root.left, root.val), solveTree(root.right, root.val)

            res[0] = max(res[0], l + r)

            return max(l, r) + 1 if root.val == parent else 0

        solveTree(root, -1)

        return res[0]
