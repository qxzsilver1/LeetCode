class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        res = [0] * len(tasks)

        # available = (weight, idx)
        available = [(servers[i], i) for i in range(len(servers))]
        heapq.heapify(available)

        # unavailable = (timeServerFreed, weight, idx)
        unavailable = []

        t = 0

        for j in range(len(tasks)):
            t = max(t, j)

            if not len(available):
                t = unavailable[0][0]
            
            while unavailable and t >= unavailable[0][0]:
                timeServerFreed, weight, idx = heapq.heappop(unavailable)
                heapq.heappush(available, (weight, idx))
            
            weight, idx = heapq.heappop(available)

            res[j] = idx

            heapq.heappush(unavailable, (t + tasks[j], weight, idx))
        
        return res
