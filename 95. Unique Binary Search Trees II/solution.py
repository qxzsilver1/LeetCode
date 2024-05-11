# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        dp = {}
        
        def generate(left_bd, right_bd):
            if left_bd > right_bd:
                return [None]
            
            if (left_bd, right_bd) in dp:
                return dp[(left_bd, right_bd)]
            
            res = []

            for val in range(left_bd, right_bd + 1):                
                for left_tree in generate(left_bd, val - 1):
                    for right_tree in generate(val + 1, right_bd):
                        root = TreeNode(val, left_tree, right_tree)
                        res.append(root)
            
            dp[(left_bd, right_bd)] = res

            return res
        
        return generate(1, n)
