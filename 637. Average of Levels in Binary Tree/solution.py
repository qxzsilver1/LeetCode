# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        q = deque([root])

        output = []

        while q:
            n = len(q)
            curr_sum = 0
            for i in range(n):
                node = q.popleft()

                curr_sum += node.val

                if node.left:
                    q.append(node.left)
                
                if node.right:
                    q.append(node.right)
            
            output.append(curr_sum / n)
        
        return output
