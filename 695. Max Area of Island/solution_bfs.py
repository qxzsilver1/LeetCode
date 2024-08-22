class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        ROWS, COLS = len(grid), len(grid[0])

        visited = set()
        max_island_area = 0

        def bfs(r, c):
            q = collections.deque()

            area = 1 if grid[r][c] else 0

            visited.add((r, c))
            q.append((r, c))

            while q:
                row, col = q.popleft()
                directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if r in range(ROWS) and c in range(COLS) and grid[r][c] == 1 and (r, c) not in visited:
                        q.append((r, c))
                        visited.add((r, c))
                        area += 1
            
            return area
            

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r, c) not in visited:
                    area = bfs(r, c)

                    max_island_area = max(max_island_area, area)
        
        return max_island_area
