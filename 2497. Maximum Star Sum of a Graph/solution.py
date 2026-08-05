class Solution:
    def maxStarSum(self, vals: List[int], edges: List[List[int]], k: int) -> int:
        node_heap_map = defaultdict(list)

        for s, t in edges:
            if vals[t] > 0:
                heapq.heappush(node_heap_map[s], vals[t])

                if len(node_heap_map[s]) > k:
                    heapq.heappop(node_heap_map[s])
            
            if vals[s] > 0:
                heapq.heappush(node_heap_map[t], vals[s])

                if len(node_heap_map[t]) > k:
                    heapq.heappop(node_heap_map[t])
        
        res = float('-inf')

        for i in range(len(vals)):
            total = vals[i]

            for nei_val in node_heap_map[i]:
                total += nei_val
            
            res = max(res, total)
        
        return res
