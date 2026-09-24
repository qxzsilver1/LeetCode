class Solution:
    def trapRainWater(self, heightMap: list[list[int]]) -> int:
        ROWS, COLS = len(heightMap), len(heightMap[0])

        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        min_heap = []

        for r in range(ROWS):
            for c in range(COLS):
                if r in [0, ROWS - 1] or c in [0, COLS - 1]:
                    heapq.heappush(min_heap, (heightMap[r][c], r, c))
                    heightMap[r][c] = -1
        
        res = 0

        max_h = -1

        while min_heap:
            h, r, c = heapq.heappop(min_heap)
            max_h = max(max_h, h)

            res += max_h - h

            for dr, dc in dirs:
                nr, nc = r + dr, c + dc

                if nr < 0 or nr == ROWS or nc < 0 or nc == COLS or heightMap[nr][nc] == -1:
                    continue
                
                heapq.heappush(min_heap, (heightMap[nr][nc], nr, nc))
                heightMap[nr][nc] = -1
        
        return res

