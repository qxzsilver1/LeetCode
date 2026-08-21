class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)

        def isInBounds(r, c):
            return min(r, c) >= 0 and max(r, c) < n

        def precompute():
            q = deque()
            min_dist = {}

            for r in range(n):
                for c in range(n):
                    if grid[r][c]:
                        q.append([r, c, 0])
                        min_dist[(r, c)] = 0
            
            while q:
                r, c, dist = q.popleft()
                nei = [[r+1, c], [r-1, c], [r, c+1], [r, c-1]]

                for n_r, n_c in nei:
                    if isInBounds(n_r, n_c) and (n_r, n_c) not in min_dist:
                        min_dist[(n_r, n_c)] = dist + 1
                        q.append([n_r, n_c, dist + 1])
            
            return min_dist
        
        min_distances = precompute()

        max_heap = [(- min_distances[(0, 0)], 0, 0)] # dist, r, c triple

        visited = set()
        visited.add((0, 0))

        while max_heap:
            dist, r, c = heapq.heappop(max_heap)
            dist = - dist

            if (r, c) == (n-1, n-1):
                return dist
            
            nei = [[r+1, c], [r-1, c], [r, c+1], [r, c-1]]

            for n_r, n_c in nei:
                if isInBounds(n_r, n_c) and (n_r, n_c) not in visited:
                    visited.add((n_r, n_c))
                    nei_min_dist = min(dist, min_distances[(n_r, n_c)])
                    heapq.heappush(max_heap, (- nei_min_dist , n_r, n_c))
