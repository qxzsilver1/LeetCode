class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])

        row_ct, col_ct = [0]*m, [0]*n

        diff = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                row_ct[i] += grid[i][j]
                col_ct[j] += grid[i][j]

        for i in range(m):
            for j in range(n):
                diff[i][j] = 2 * row_ct[i] + 2 * col_ct[j] - m - n
        
        return diff
