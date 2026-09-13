class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        ROWS, COLS = len(heights), len(heights[0])

        min_heap = [[0, 0, 0]] # [diff, row, col]
        visited = set()

        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        while min_heap:
            diff, r, c = heapq.heappop(min_heap)

            if (r, c) in visited:
                continue
            
            visited.add((r, c))

            if (r, c) == (ROWS - 1, COLS - 1):
                return diff
            
            for dr, dc in dirs:
                new_r, new_c = r + dr, c + dc

                if new_r < 0 or new_r >= ROWS or new_c < 0 or new_c >= COLS or (new_r, new_c) in visited:
                    continue
                
                new_diff = max(diff, abs(heights[new_r][new_c] - heights[r][c]))
                heapq.heappush(min_heap, [new_diff, new_r, new_c])
        
        return 0
