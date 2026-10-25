class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()

        def dfs(r, c):
            if r < 0 or c < 0 or r == ROWS or c == COLS:
                return 0
            
            if grid[r][c] == 1 or (r, c) in visited:
                return 1
            
            visited.add((r, c))

            return min(dfs(r + 1, c), dfs(r - 1, c), dfs(r, c + 1), dfs(r, c - 1))
        
        count_closed_islands = 0
        
        for r in range(ROWS):
            for c in range(COLS):
                if not grid[r][c] and (r, c) not in visited:
                    count_closed_islands += dfs(r, c)
        
        return count_closed_islands
