class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        
        for i, edge in enumerate(edges):
            edge.append(i)

        adj = defaultdict(list)
        for u, v, w, idx in edges:
            adj[u].append((v, w, idx))
            adj[v].append((u, w, idx))

        def minimax(src, dst, exclude_idx):
            dist = [float('inf')] * n
            dist[src] = 0
            pq = [(0, src)]

            while pq:
                max_w, u = heapq.heappop(pq)
                if u == dst:
                    return max_w

                for v, weight, edge_idx in adj[u]:
                    if edge_idx == exclude_idx:
                        continue
                    new_w = max(max_w, weight)
                    if new_w < dist[v]:
                        dist[v] = new_w
                        heapq.heappush(pq, (new_w, v))

            return float('inf')

        critical, pseudo = [], []
        for i, (u, v, w, idx) in enumerate(edges):
            if w < minimax(u, v, idx):
                critical.append(idx)
            elif w == minimax(u, v, -1):
                pseudo.append(idx)

        return [critical, pseudo]
