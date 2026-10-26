class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        visit = set()
        res = 0

        def bfs(r, c):
            q = deque([(r, c)])
            visit.add((r, c))
            is_closed = True

            while q:
                x, y = q.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if nx < 0 or ny < 0 or nx >= ROWS or ny >= COLS:
                        is_closed = False
                        continue
                    if grid[nx][ny] == 1 or (nx, ny) in visit:
                        continue
                    visit.add((nx, ny))
                    q.append((nx, ny))

            return is_closed

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0 and (r, c) not in visit:
                    res += bfs(r, c)

        return res
