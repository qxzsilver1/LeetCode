# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            return TreeNode(val, left= root)
        
        curr_depth = 1

        q = deque([root])

        while q:
            if curr_depth == depth - 1:
                break
            
            n = len(q)

            for i in range(n):
                node = q.popleft()

                if node.left:
                    q.append(node.left)
                
                if node.right:
                    q.append(node.right)
            
            curr_depth += 1
        
        for node in q:
            curr_left, curr_right = node.left, node.right
            node.left = TreeNode(val, curr_left)
            node.right = TreeNode(val, None, curr_right)
        
        return root
                
