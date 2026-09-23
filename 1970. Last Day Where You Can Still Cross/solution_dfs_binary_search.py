class Solution:
    def latestDayToCross(self, row: int, col: int, cells: list[list[int]]) -> int:
        def canCross(day):
            grid = [[0] * col for _ in range(row)]

            dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

            for r, c in cells[:day]:
                grid[r - 1][c - 1] = 1
            
            def dfs(r, c):
                if r < 0 or r >= row or c < 0 or c >= col or grid[r][c] != 0:
                    return False
                
                if r == row - 1:
                    return True
                
                grid[r][c] = -1

                for dr, dc in dirs:
                    if dfs(r + dr, c + dc):
                        return True
                
                return False
            
            for i in range(col):
                if grid[0][i] == 0 and dfs(0, i):
                    return True
            
            return False
        
        l, r = 1, row * col

        while l < r:
            m = r - (r - l) // 2

            if canCross(m):
                l = m
            else:
                r = m - 1

        return l
