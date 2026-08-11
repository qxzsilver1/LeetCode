class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        m, n = len(grid), len(grid[0])

        dist = [[-1] * n for _ in range(m)]
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        min_heap = [ (grid[0][0], 0, 0) ]

        while min_heap:
            cost, x, y = heapq.heappop(min_heap)

            if dist[x][y] >= 0:
                continue
            
            dist[x][y] = cost

            for dx, dy in dirs:
                nx, ny = x + dx, y + dy

                if 0 <= nx < m and 0 <= ny < n and dist[nx][ny] == -1:
                    heapq.heappush(min_heap, (cost + grid[nx][ny], nx, ny))
        
        return dist[m-1][n-1] < health
