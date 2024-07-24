class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for i, t in enumerate(tasks):
            t.append(i)

        tasks.sort(key= lambda t: t[0])

        res = []
        min_heap = []

        i, time = 0, tasks[0][0]

        while min_heap or i < len(tasks):
            while i < len(tasks) and time >= tasks[i][0]:
                heapq.heappush(min_heap, [tasks[i][1], tasks[i][2]])
                i += 1
            
            if not min_heap:
                time = tasks[i][0]
            else:
                proc_time, idx = heapq.heappop(min_heap)
                time += proc_time
                res.append(idx)
        
        return res
