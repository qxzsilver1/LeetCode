class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        people = sorted((p, i) for i, p in enumerate(people))

        res = [0] * len(people)

        cnt = 0

        start = [f[0] for f in flowers]
        end = [f[1] for f in flowers]

        heapq.heapify(start)
        heapq.heapify(end)

        for p, i in people:
            while start and start[0] <= p:
                heapq.heappop(start)
                cnt += 1
            
            while end and end[0] < p:
                heapq.heappop(end)
                cnt -= 1
            
            res[i] = cnt
        
        return res
