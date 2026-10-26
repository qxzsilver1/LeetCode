class DSU:
    def __init__(self, n):
        self.Parent = list(range(n + 1))
        self.Size = [1] * (n + 1)

    def find(self, node):
        if self.Parent[node] != node:
            self.Parent[node] = self.find(self.Parent[node])
        return self.Parent[node]

    def union(self, u, v):
        pu, pv = self.find(u), self.find(v)
        if pu == pv:
            return False
        if self.Size[pu] >= self.Size[pv]:
            self.Size[pu] += self.Size[pv]
            self.Parent[pv] = pu
        else:
            self.Size[pv] += self.Size[pu]
            self.Parent[pu] = pv
        return True

class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        N = ROWS * COLS
        
        def indexConvert(r, c):
            return r * COLS + c

        dsu = DSU(N)
        directions = [0, 1, 0, -1, 0]
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    for d in range(4):
                        nr, nc = r + directions[d], c + directions[d + 1]
                        if min(nr, nc) < 0 or nr == ROWS or nc == COLS:
                            dsu.union(N, indexConvert(r, c))
                        elif grid[nr][nc] == 0:
                            dsu.union(indexConvert(r, c), indexConvert(nr, nc))

        res = 0
        rootN = dsu.find(N)
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    continue
                node = indexConvert(r, c)
                root = dsu.find(node)
                if root == node and root != rootN:
                    res += 1
        return res
