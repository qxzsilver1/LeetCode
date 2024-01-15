# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        depth = 1
        q = deque([root])

        while q:

            for i in range(len(q)):
                root = q.popleft()

                if not root.left and not root.right:
                    return depth
                
                if root.left:
                    q.append(root.left)
                
                if root.right:
                    q.append(root.right)
            
            depth += 1
