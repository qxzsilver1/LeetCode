# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot: # check if t is empty - always True
            return True
        
        if not root: # if t is non-empty (from above) but s is empty, always False
            return False
        
        if self.sameTree(root, subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)


    def sameTree(self, s, t):
        if not s and not t:
            return True
        
        if not s or not t:
            return False
        
        if s.val != t.val:
            return False
        
        return self.sameTree(s.left, t.left) and self.sameTree(s.right, t.right)
