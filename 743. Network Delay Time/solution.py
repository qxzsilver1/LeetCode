class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = defaultdict(list)

        for u, v, w in times:
            edges[u].append((v, w))
        
        min_heap = [(0, k)]

        visited = set()
        t = 0

        while min_heap:
            w1, n1 = heapq.heappop(min_heap)

            if n1 in visited:
                continue
            
            visited.add(n1)
            t = max(t, w1)

            for nei, wei in edges[n1]:
                if nei not in visited:
                    heapq.heappush(min_heap, (wei + w1, nei))
        
        return t if len(visited) == n else -1
