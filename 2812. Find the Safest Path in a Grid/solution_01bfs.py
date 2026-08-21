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

        safe_factor = [-1] * (n * n)

        res = safe_factor[0] = min(min_dist[n - 1][n - 1], min_dist[0][0])
        q.append(0)

        while q:
            node = q.popleft()
            r, c = divmod(node, n)

            res = min(res, safe_factor[node])

            if r == n - 1 and c == n - 1:
                break

            for i in range(4):
                n_r, n_c = r + dirs[i], c + dirs[i + 1]
                new_node = n_r * n + n_c

                if 0 <= n_r < n and 0 <= n_c < n and safe_factor[new_node] == -1:
                    safe_factor[new_node] = min(safe_factor[node], min_dist[n_r][n_c])

                    if safe_factor[new_node] < res:
                        q.append(new_node)
                    else:
                        q.appendleft(new_node)

        return res
