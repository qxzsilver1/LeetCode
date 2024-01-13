# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def createTree(l, r):
            if l > r:
                return None
            m = l + (r - l) // 2

            curr_tree_node = TreeNode(nums[m])
            curr_tree_node.left = createTree(l, m-1)
            curr_tree_node.right = createTree(m+1, r)

            return curr_tree_node
        
        l, r = 0, len(nums) - 1
        
        return createTree(l, r)
