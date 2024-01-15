class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        vertex_degrees = { i: 0 for i in range(1, n+1) }

        for i, j in trust:
            vertex_degrees[i] -= 1
            vertex_degrees[j] += 1

        for v, deg in vertex_degrees.items():
            if deg == n - 1:
                return v
        
        return -1
