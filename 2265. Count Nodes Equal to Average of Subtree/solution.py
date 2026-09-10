# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        num_nodes = 0
        
        def dfs(root):
            nonlocal num_nodes
            
            if not root:
                return 0, 0
            
            left_val, left_cnt = dfs(root.left)
            right_val, right_cnt = dfs(root.right)

            node_sum = left_val + right_val + root.val
            node_cnt = left_cnt + right_cnt + 1

            if root.val == node_sum // node_cnt:
                num_nodes += 1
            
            return node_sum, node_cnt
        
        dfs(root)

        return num_nodes
