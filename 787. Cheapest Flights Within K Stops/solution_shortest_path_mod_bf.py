class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float('inf')] * n
        prices[src] = 0

        adj_list = [[] for _ in range(n)]

        for s, t, cost in flights:
            adj_list[s].append([t, cost])
        
        q = deque([(0, src, 0)])

        while q:
            cost, node, stops = q.popleft()

            if stops > k:
                continue
            
            for neighbor, p in adj_list[node]:
                next_cost = cost + p

                if next_cost < prices[neighbor]:
                    prices[neighbor] = next_cost
                    q.append((next_cost, neighbor, stops + 1))
        
        return -1 if prices[dst] == float('inf') else prices[dst]
