class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        max_heap = []

        stations.append((target, float('inf')))

        res = prev = 0

        for location, capacity in stations:
            startFuel -= location - prev

            while max_heap and startFuel < 0:
                startFuel += - heapq.heappop(max_heap)
                res += 1
            
            if startFuel < 0:
                return -1
            
            heapq.heappush(max_heap, - capacity)
            prev = location
        
        return res
