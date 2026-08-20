class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)

        visited = [[False] * n for _ in range(n)]

        min_h = max_h = grid[0][0]

        for row in range(n):
            max_h = max(max_h, max(grid[row]))
            min_h = min(min_h, min(grid[row]))
        
        def dfs(node, t):
            r, c = node

            if min(r, c) < 0 or max(r, c) >= n or visited[r][c] or grid[r][c] > t:
                return False
            
            if r == n-1 and c == n-1:
                return True
            
            visited[r][c] = True

            return dfs((r+1, c), t) or dfs((r-1, c), t) or dfs((r, c+1), t) or dfs((r, c-1), t)

        l, r = min_h, max_h

        while l < r:
            m = l + (r - l) // 2

            if dfs((0, 0), m):
                r = m
            else:
                l = m + 1
            
            for row in range(n):
                for col in range(n):
                    visited[row][col] = False
        
        return r
