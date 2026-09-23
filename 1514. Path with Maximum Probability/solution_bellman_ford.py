class Solution:
    def maxProbability(self, n: int, edges: list[list[int]], succProb: list[float], start_node: int, end_node: int) -> float:
        maxProb = [0.0] * n
        maxProb[start_node] = 1.0

        for i in range(n):
            updated = False
            
            for j in range(len(edges)):
                src, dst = edges[j]
                if maxProb[src] * succProb[j] > maxProb[dst]:
                    maxProb[dst] = maxProb[src] * succProb[j]
                    updated = True

                if maxProb[dst] * succProb[j] > maxProb[src]:
                    maxProb[src] = maxProb[dst] * succProb[j]
                    updated = True

            if not updated:
                break

        return maxProb[end_node]
