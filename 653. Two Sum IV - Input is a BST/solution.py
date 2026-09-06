# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        
        def inorder(root, sorted_list):
            if not root:
                return
            
            inorder(root.left, sorted_list)
            sorted_list.append(root.val)
            inorder(root.right, sorted_list)
        
        inorder_list = []

        inorder(root, inorder_list)

        l, r = 0, len(inorder_list) - 1

        while l < r:
            curr_sum = inorder_list[l] + inorder_list[r]

            if curr_sum == k:
                return True
            
            if curr_sum < k:
                l += 1
            else:
                r -= 1
        
        return False
