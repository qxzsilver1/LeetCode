class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [0, 1, 0, -1, 0]

        def dfs(r, c):
            if r < 0 or c < 0 or r == ROWS or c == COLS or grid[r][c] == 1:
                return
            grid[r][c] = 1
            for d in range(4):
                dfs(r + directions[d], c + directions[d + 1])

        for r in range(ROWS):
            dfs(r, 0)
            dfs(r, COLS - 1)
        for c in range(COLS):
            dfs(0, c)
            dfs(ROWS - 1, c)

        res = 0
        for r in range(1, ROWS - 1):
            for c in range(1, COLS - 1):
                if grid[r][c] == 0:
                    dfs(r, c)
                    res += 1
        return res
