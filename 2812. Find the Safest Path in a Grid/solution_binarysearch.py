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

        def canReach(threshold):
            q = deque([0])

            visited = [False] * (n ** 2)
            visited[0] = True

            while q:
                node = q.popleft()
                r, c = divmod(node, n)

                if r == n - 1 and c == n - 1:
                    return True
                
                for i in range(4):
                    n_r, n_c = r + dirs[i], c + dirs[i + 1]
                    new_node = n_r * n + n_c

                    if (0 <= n_r < n and 0 <= n_c < n and not visited[new_node] and min_dist[n_r][n_c] >= threshold):
                        visited[new_node] = True
                        q.append(new_node)
            
            return False
        
        l, r = 0, min(min_dist[0][0], min_dist[n-1][n-1])

        while l <= r:
            m = (l + r) // 2

            if canReach(m):
                l = m + 1
            else:
                r = m - 1
        
        return l - 1
