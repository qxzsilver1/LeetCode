class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        ROWS, COLS = len(heights), len(heights[0])

        dist = [float('inf')] * (ROWS * COLS)
        dist[0] = 0
        
        in_queue = [False] * (ROWS * COLS)

        def index(r, c):
            return r * COLS + c

        queue = deque([0])
        in_queue[0] = True
        
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        while queue:
            u = queue.popleft()
            in_queue[u] = False
            r, c = divmod(u, COLS)

            for dr, dc in dirs:
                new_r, new_c = r + dr, c + dc
                
                if 0 <= new_r < ROWS and 0 <= new_c < COLS:
                    v = index(new_r, new_c)
                    weight = abs(heights[r][c] - heights[new_r][new_c])
                    new_dist = max(dist[u], weight)
                    
                    if new_dist < dist[v]:
                        dist[v] = new_dist
                        if not in_queue[v]:
                            queue.append(v)
                            in_queue[v] = True

        return dist[ROWS * COLS - 1]
