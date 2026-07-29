class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        routes = collections.defaultdict(dict)

        for s, t, p in flights:
            routes[s][t] = p
        
        pq = [(0, src, k + 1)]

        while pq:
            price, i, num_stops = heapq.heappop(pq)

            if i == dst:
                return price
            
            if num_stops > 0:
                for j in routes[i]:
                    heapq.heappush(pq, (price + routes[i][j], j, num_stops - 1))
        
        return -1
