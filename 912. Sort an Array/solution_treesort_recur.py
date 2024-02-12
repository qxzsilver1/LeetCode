class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        output = []

        root = TreeNode()

        def insert(val): 
            nonlocal root 
            root = insertRecur(root, val) 

        def insertRecur(node, val):
            if not node:
                return TreeNode(val)
            
            if val <= node.val:
                node.left = insertRecur(node.left, val)
            else:
                node.right = insertRecur(node.right, val)
            
            return node

        for i in range(len(nums)):
            insert(nums[i])
        
        def inorder(node):
            if not node:
                return
            
            if node == root:
                inorder(node.left)
                inorder(node.right)
            else:
                inorder(node.left)
                output.append(node.val)
                inorder(node.right)
        
        inorder(root)

        return output
