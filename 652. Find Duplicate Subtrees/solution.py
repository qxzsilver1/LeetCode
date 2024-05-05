# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        subtrees_dict = defaultdict(list)

        def preorder(node):
            if not node:
                return 'None'
            
            s = ','.join([str(node.val), preorder(node.left), preorder(node.right)])

            if len(subtrees_dict[s]) == 1:
                res.append(node)
            
            subtrees_dict[s].append(node)

            return s
        
        res = []
        
        preorder(root)

        return res
