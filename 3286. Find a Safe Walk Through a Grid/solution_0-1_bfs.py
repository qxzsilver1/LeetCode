class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        m, n = len(grid), len(grid[0])

        dist = [[float('inf')] * n for _ in range(m)]
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        q = deque()
        q.appendleft((0, 0))
        dist[0][0] = grid[0][0]

        while q:
            x, y = q.popleft()

            if x == m - 1 and y == n - 1:
                return True
            
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy

                if nx < 0 or nx >= m or ny < 0 or ny >= n:
                    continue
                
                cost = dist[x][y] + grid[nx][ny]

                if cost >= health:
                    continue
                
                if cost < dist[nx][ny]:
                    dist[nx][ny] = cost

                    if grid[nx][ny] == 0:
                        q.appendleft((nx, ny))
                    else:
                        q.append((nx, ny))
        
        return False
