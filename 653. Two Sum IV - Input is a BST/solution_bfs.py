# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        diff_set = set()

        q = deque()
        q.append(root)

        while q:
            if q[0]:
                node = q.popleft()
                
                if k - node.val in diff_set:
                    return True
                
                diff_set.add(node.val)
                q.append(node.right)
                q.append(node.left)
            else:
                q.popleft()
        
        return False


