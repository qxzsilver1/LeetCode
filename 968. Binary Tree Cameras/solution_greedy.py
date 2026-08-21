# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        res = [0]

        covered = set([None])

        def dfs(node, parent = None):
            if node:
                dfs(node.left, node)
                dfs(node.right, node)

                if (parent is None and node not in covered or node.left not in covered or node.right not in covered):
                    res[0] += 1
                    covered.update({node, parent, node.left, node.right})
        
        dfs(root)

        return res[0]
