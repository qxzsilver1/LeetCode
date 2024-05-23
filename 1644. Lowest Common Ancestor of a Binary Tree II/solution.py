# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        p_exists, q_exists = False, False

        def dfs(node):
            nonlocal p_exists, q_exists

            if not node:
                return None
            
            left, right = dfs(node.left), dfs(node.right)

            if node == p or node == q:
                if node == p:
                    p_exists = True
                
                if node == q:
                    q_exists = True

                return node
            
            if left and right:
                return node
            else:
                return left or right

        res = dfs(root)

        return res if p_exists and q_exists else None
