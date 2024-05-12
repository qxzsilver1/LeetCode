# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:

        def dfs(l, r):
            if l > r:
                return None
            
            val = max(nums[l:r+1])
            idx = nums.index(val)

            node = TreeNode(val)
            left = dfs(l, idx-1)
            right = dfs(idx+1, r)

            node.left = left
            node.right = right

            return node
        
        return dfs(0, len(nums)-1)
