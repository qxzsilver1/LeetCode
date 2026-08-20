class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        node = 0

        visited = [False] * n
        dist = [10000000] * n
        edges = 0

        total_cost = 0

        while edges < n-1:
            visited[node] = True
            next_node = -1

            for i in range(n):
                if visited[i]:
                    continue
                
                curr_dist = abs(points[i][0] - points[node][0]) + abs(points[i][1] - points[node][1])
                dist[i] = min(dist[i], curr_dist)

                if next_node == -1 or dist[i] < dist[next_node]:
                    next_node = i
            
            total_cost += dist[next_node]
            node = next_node
            edges += 1
        
        return total_cost
