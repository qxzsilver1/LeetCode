class DSU:
    def __init__(self, n):
        self.parent = list(range(n + 1))
        self.size = [1] * (n + 1)

    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, u, v):
        pu = self.find(u)
        pv = self.find(v)
        
        if pu == pv:
            return False
        if self.size[pu] < self.size[pv]:
            pu, pv = pv, pu
        
        self.size[pu] += self.size[pv]
        self.parent[pv] = pu
        
        return True

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        ROWS, COLS = len(heights), len(heights[0])

        edges = []
        for r in range(ROWS):
            for c in range(COLS):
                if r + 1 < ROWS:
                    edges.append((abs(heights[r][c] - heights[r + 1][c]), r * COLS + c, (r + 1) * COLS + c))
                if c + 1 < COLS:
                    edges.append((abs(heights[r][c] - heights[r][c + 1]), r * COLS + c, r * COLS + c + 1))

        edges.sort()
        dsu = DSU(ROWS * COLS)
        for weight, u, v in edges:
            dsu.union(u, v)
            if dsu.find(0) == dsu.find(ROWS * COLS - 1):
                return weight
        return 0
