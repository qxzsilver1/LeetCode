class DisjointSetUnion:
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

    def connected(self, u, v):
        return self.find(u) == self.find(v)

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)

        dsu = DisjointSetUnion(n*n)

        positions = sorted((grid[r][c], r, c) for r in range(n) for c in range(n))

        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        for t, r, c in positions:
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc

                if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] <= t:
                    dsu.union(r * n + c, nr * n + nc)
                
                if dsu.connected(0, n*n - 1):
                    return t
