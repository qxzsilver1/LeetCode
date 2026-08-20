class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)

        adj_list = { i: [] for i in range(n) } # i: list of [cost, node index]

        for i in range(n):
            x1, y1 = points[i]

            for j in range(i+1, n):
                x2, y2 = points[j]

                man_dist = abs(x1-x2) + abs(y1-y2)

                adj_list[i].append([man_dist, j])
                adj_list[j].append([man_dist, i])

        total_cost = 0
        visited = set()
        min_heap = [[0, 0]] # [cost, point index] pair

        while len(visited) < n:
            cost, i = heapq.heappop(min_heap)

            if i in visited:
                continue
            
            total_cost += cost
            visited.add(i)

            for neighborCost, nei in adj_list[i]:
                if nei not in visited:
                    heapq.heappush(min_heap, [neighborCost, nei])
        
        return total_cost
