class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        m, n = len(grid), len(grid[0])
        sorted_q = sorted(enumerate(queries), key=lambda x: x[1])
        
        min_heap = [(grid[0][0], 0, 0)]
        visited = [[False] * n for _ in range(m)]
        visited[0][0] = True
        
        count = 0
        res = [0] * len(queries)
        
        for idx, q in sorted_q:
            while min_heap and min_heap[0][0] < q:
                val, r, c = heapq.heappop(min_heap)
                count += 1
                for dr, dc in ((0,1),(0,-1),(1,0),(-1,0)):
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n and not visited[nr][nc]:
                        visited[nr][nc] = True
                        heapq.heappush(min_heap, (grid[nr][nc], nr, nc))
            res[idx] = count
        return res
