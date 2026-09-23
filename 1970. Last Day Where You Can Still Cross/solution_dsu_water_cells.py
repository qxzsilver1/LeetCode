class DSU:
    def __init__(self, n):
        self.root = list(range(n))
        self.size = [1] * n

    def find(self, x):
        if self.root[x] != x:
            self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return
        
        if self.size[root_x] > self.size[root_y]:
            root_x, root_y = root_y, root_x
        self.root[root_x] = root_y
        self.size[root_y] += self.size[root_x]

class Solution:
    def latestDayToCross(self, row: int, col: int, cells: list[list[int]]) -> int:
        grid = [[0] * col for _ in range(row)]

        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]

        dsu = DSU(row * col + 2)

        for i in range(row * col):
            r, c = cells[i][0] - 1, cells[i][1] - 1
            grid[r][c] = 1
            idx1 = r * col + c + 1

            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                idx2 = nr * col + nc + 1

                if 0 <= nr < row and 0 <= nc < col and grid[nr][nc] == 1:
                    dsu.union(idx1, idx2)
            
            if c == 0:
                dsu.union(0, idx1)
            
            if c == col - 1:
                dsu.union(row * col + 1, idx1)
            
            if dsu.find(0) == dsu.find(row * col + 1):
                return i
