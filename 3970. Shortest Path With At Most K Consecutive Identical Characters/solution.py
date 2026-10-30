class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        graph = [[] for _ in range(n)]

        for u, v, w in edges:
            graph[u].append((v, w))
        
        dist = [[2 ** 31 - 1] * (k + 1) for _ in range(n)]

        # (shortest path length, node idx, num consecutive identical letters at the end)
        pq = []

        dist[0][1] = 0
        heappush(pq, (0, 0, 1))

        while pq:
            d, node, cnt = heappop(pq)

            if d > dist[node][cnt]:
                continue
            
            if node == n - 1:
                return d
            
            for v, w in graph[node]:
                new_cnt = cnt + 1 if labels[node] == labels[v] else 1

                if new_cnt > k:
                    continue
                
                new_d = d + w

                if new_d < dist[v][new_cnt]:
                    dist[v][new_cnt] = new_d
                    heappush(pq, (new_d, v, new_cnt))
        
        return -1
