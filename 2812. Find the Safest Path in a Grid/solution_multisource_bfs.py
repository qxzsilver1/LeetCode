class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
        min_dist = grid
        dirs = [0, 1, 0, -1, 0]

        q = deque()

        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    q.append(r * n + c)
                    min_dist[r][c] = 0
                else:
                    min_dist[r][c] = -1

        while q:
            node = q.popleft()
            r, c = divmod(node, n)

            for i in range(4):
                n_r, n_c = r + dirs[i], c + dirs[i + 1]
                if 0 <= n_r < n and 0 <= n_c < n and min_dist[n_r][n_c] == -1:
                    min_dist[n_r][n_c] = min_dist[r][c] + 1
                    q.append(n_r * n + n_c)

        max_heap = [(-min_dist[0][0], 0)]

        safe_factor = [0] * (n ** 2)
        safe_factor[0] = min_dist[0][0]

        while max_heap:
            dist, node = heapq.heappop(max_heap)
            dist = -dist

            r, c = divmod(node, n)

            if r == n - 1 and c == n - 1:
                return dist
            
            if safe_factor[node] > dist:
                continue

            for i in range(4):
                n_r, n_c = r + dirs[i], c + dirs[i + 1]
                new_node = n_r * n + n_c

                if 0 <= n_r < n and 0 <= n_c < n:
                    new_dist = min(dist, min_dist[n_r][n_c])

                    if new_dist > safe_factor[new_node]:
                        safe_factor[new_node] = new_dist
                        heapq.heappush(max_heap, (-new_dist, new_node))

        return 0
