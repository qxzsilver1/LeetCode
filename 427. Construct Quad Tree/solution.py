"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        
        def dfs(n, top_left_row, top_left_col):
            all_same = True

            for i in range(n):
                for j in range(n):
                    if grid[top_left_row][top_left_col] != grid[top_left_row + i][top_left_col + j]:
                        all_same = False
                        break
            
            if all_same:
                return Node(grid[top_left_row][top_left_col], True, None)
            
            n = n // 2

            top_left = dfs(n, top_left_row, top_left_col)
            top_right = dfs(n, top_left_row, top_left_col + n)
            bottom_left = dfs(n, top_left_row + n, top_left_col)
            bottom_right = dfs(n, top_left_row + n, top_left_col + n)

            return Node(0, False, top_left, top_right, bottom_left, bottom_right)
        
        return dfs(len(grid), 0, 0)
