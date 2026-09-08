class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        ROWS, COLS = len(grid), len(grid[0])

        q = [(n, i) for i, n in enumerate(queries)]
        q.sort()

        min_heap = [(grid[0][0], 0, 0)]

        res = [0] * len(queries)

        visited = set([(0, 0)])

        points = 0

        for limit, idx in q:
            while min_heap and min_heap[0][0] < limit:
                val, r, c = heapq.heappop(min_heap)
                points += 1
                neis = [[r + 1, c], [r - 1, c], [r, c + 1], [r, c - 1]]

                for nr, nc in neis:
                    if 0 <= nr < ROWS and 0 <= nc < COLS and (nr, nc) not in visited:
                        heapq.heappush(min_heap, [grid[nr][nc], nr, nc])
                        visited.add((nr, nc))
            res[idx] = points
        
        return res
