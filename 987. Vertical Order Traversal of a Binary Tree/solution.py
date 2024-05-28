# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        col_coord_nodes_dict = defaultdict(list)

        min_col, max_col = float('inf'), float('-inf')
        
        q = deque([(0, 0, root)])

        res = []

        while q:
            row, col, node = q.popleft()

            col_coord_nodes_dict[col].append((node.val, row))

            min_col = min(min_col, col)
            max_col = max(max_col, col)

            if node.left:
                q.append((row+1, col-1, node.left))
            
            if node.right:
                q.append((row+1, col+1, node.right))

        for col in range(min_col, max_col + 1):
            vals_list = col_coord_nodes_dict[col]

            vals_list.sort(key=lambda x: (x[1], x[0]))
            res.append([val for val, _ in vals_list])
        
        return res
