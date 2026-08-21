class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        events_list = []

        for idx, (start, end) in enumerate(intervals):
            events_list.append((start, 0, end - start + 1, idx))
            events_list.append((end, 2, end - start + 1, idx))
        
        for i, q in enumerate(queries):
            events_list.append((q, 1, i))
        
        events_list.sort(key= lambda x: (x[0], x[1]))

        min_heap = []

        res = [-1] * len(queries)
        is_inactive = [False] * len(intervals)

        for time, event_type, *rest in events_list:
            if event_type == 0:
                interval_size, idx = rest
                heapq.heappush(min_heap, (interval_size, idx))
            elif event_type == 2:
                idx = rest[1]
                is_inactive[idx] = True
            else:
                query_idx = rest[0]

                while min_heap and is_inactive[min_heap[0][1]]:
                    heapq.heappop(min_heap)
                
                if min_heap:
                    res[query_idx] = min_heap[0][0]
        
        return res
