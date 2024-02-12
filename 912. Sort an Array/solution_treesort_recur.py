class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        output = []

        def insert(node, val):
            if not node:
                return TreeNode(val)
            
            if val <= node.val:
                node.left = insert(node.left, val)
            else:
                node.right = insert(node.right, val)
            
            return node

        root = TreeNode(nums[0])
        
        for i in range(1, len(nums)):
            root = insert(root, nums[i])
        
        def inorder(root):
            if not root:
                return
            
            inorder(root.left)
            output.append(root.val)
            inorder(root.right)
        
        inorder(root)

        return output
