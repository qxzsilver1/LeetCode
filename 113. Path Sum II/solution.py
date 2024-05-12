# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []

        if not root:
            return res

        def dfs(node, path, remaining_sum):
            remaining_sum -= node.val
            tmp = path + [node.val]

            if node.left:
                dfs(node.left, tmp, remaining_sum)
            if node.right:
                dfs(node.right, tmp, remaining_sum)
            
            if not node.left and not node.right and remaining_sum == 0:
                res.append(tmp)
        
        dfs(root, [], targetSum)

        return res
