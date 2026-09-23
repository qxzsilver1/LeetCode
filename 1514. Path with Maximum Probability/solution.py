class Solution:
    def maxProbability(self, n: int, edges: list[list[int]], succProb: list[float], start_node: int, end_node: int) -> float:
        adj_list = defaultdict(list)

        for i in range(len(edges)):
            src, dst = edges[i]
            adj_list[src].append([dst, succProb[i]])
            adj_list[dst].append([src, succProb[i]])
        
        pq = [(-1, start_node)]

        visited = set()

        while pq:
            prob, curr_node = heapq.heappop(pq)
            visited.add(curr_node)

            if curr_node == end_node:
                return prob * -1
            
            for nei, edge_prob in adj_list[curr_node]:
                if nei not in visited:
                    heapq.heappush(pq, (prob * edge_prob, nei))
        
        return 0
