# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        num_paths = 0
        lookup = defaultdict(int)
        lookup[targetSum] = 1
        
        def dfs(node, root_sum):
            nonlocal num_paths
            
            if not node:
                return
            
            root_sum += node.val
            num_paths += lookup[root_sum]
            
            lookup[root_sum + targetSum] += 1

            dfs(node.left, root_sum)
            dfs(node.right, root_sum)

            lookup[root_sum + targetSum] -= 1
        
        dfs(root, 0)

        return num_paths
