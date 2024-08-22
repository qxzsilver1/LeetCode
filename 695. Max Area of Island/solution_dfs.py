class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        ROWS, COLS = len(grid), len(grid[0])

        visited = set()
        max_island_area = 0

        def dfs(r, c):
            if r < 0 or r == ROWS or c < 0 or c == COLS or not grid[r][c] or (r, c) in visited:
                return 0

            visited.add((r, c))

            return 1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)
            

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r, c) not in visited:
                    area = dfs(r, c)

                    max_island_area = max(max_island_area, area)
        
        return max_island_area
