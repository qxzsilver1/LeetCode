class Solution:
    def maxProbability(self, n: int, edges: list[list[int]], succProb: list[float], start_node: int, end_node: int) -> float:
        adj = [[] for _ in range(n)]
        
        for i in range(len(edges)):
            src, dst = edges[i]
            adj[src].append((dst, succProb[i]))
            adj[dst].append((src, succProb[i]))

        maxProb = [0.0] * n
        maxProb[start_node] = 1.0
        q = deque([start_node])

        while q:
            node = q.popleft()

            for nei, edge_prob in adj[node]:
                new_prob = maxProb[node] * edge_prob
                if new_prob > maxProb[nei]:
                    maxProb[nei] = new_prob
                    q.append(nei)

        return maxProb[end_node]
