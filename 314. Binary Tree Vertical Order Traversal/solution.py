# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        col_coord_nodes_dict = defaultdict(list)

        min_x, max_x = float('inf'), float('-inf')
        
        q = deque([(0, root)])

        res = []

        while q:
            x, node = q.popleft()
            
            col_coord_nodes_dict[x].append(node.val)

            min_x = min(min_x, x)
            max_x = max(max_x, x)

            if node.left:
                q.append((x-1, node.left))
            
            if node.right:
                q.append((x+1, node.right))
        
        for col in range(min_x, max_x + 1):
            res.append(col_coord_nodes_dict[col])
        
        return res
