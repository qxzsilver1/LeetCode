class Solution:
    def maxProbability(self, n: int, edges: list[list[int]], succProb: list[float], start_node: int, end_node: int) -> float:
        adj_list = defaultdict(list)

        for i in range(len(edges)):
            src, dst = edges[i]
            adj_list[src].append([dst, succProb[i]])
            adj_list[dst].append([src, succProb[i]])
        
        pq = [(-1, start_node)]

        max_prob = [0] * n
        max_prob[start_node] = 1

        while pq:
            prob, curr_node = heapq.heappop(pq)
            prob *= -1

            if curr_node == end_node:
                return prob
            
            if prob < max_prob[curr_node]:
                continue
            
            for nei, edge_prob in adj_list[curr_node]:
                new_prob = prob * edge_prob

                if new_prob > max_prob[nei]:
                    max_prob[nei] = new_prob
                    heapq.heappush(pq, (- new_prob, nei))
        
        return 0
