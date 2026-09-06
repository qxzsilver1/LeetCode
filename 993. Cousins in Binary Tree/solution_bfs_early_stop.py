# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        q = deque([root])

        while q:
            siblings, cousins = False, False

            nodes_at_depth = len(q)

            for _ in range(nodes_at_depth):
                node = q.popleft()

                if node is None:
                    siblings = False
                else:
                    if node.val == x or node.val == y:
                        if not cousins:
                            siblings, cousins = True, True
                        else:
                            return not siblings
                    
                    q.append(node.left) if node.left else None
                    q.append(node.right) if node.right else None
                    q.append(None)
            if cousins:
                return False
        
        return False
