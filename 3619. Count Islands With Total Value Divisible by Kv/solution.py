class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        dirs = [0, 1, 0, -1, 0]

        def dfs(r, c):
            total = grid[r][c]
            grid[r][c] = 0

            for d in range(4):
                x, y = r + dirs[d], c + dirs[d + 1]

                if 0 <= x < ROWS and 0 <= y < COLS and grid[x][y] > 0:
                    total += dfs(x, y)
            
            return total
        
        return sum(grid[r][c] > 0 and dfs(r, c) % k == 0 for r in range(ROWS) for c in range(COLS))
