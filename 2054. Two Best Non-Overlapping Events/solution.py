class Solution:
    def maxTwoEvents(self, events: list[list[int]]) -> int:
        min_heap = []

        events.sort(key= lambda x: x[0])

        max_val = 0
        res = 0

        for e in events:
            while min_heap and min_heap[0][0] < e[0]:
                max_val = max(max_val, min_heap[0][1])
                heapq.heappop(min_heap)
            
            res = max(res, max_val + e[2])

            heapq.heappush(min_heap, (e[1], e[2]))
        
        return res
