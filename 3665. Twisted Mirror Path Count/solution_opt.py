class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        MOD = 10 ** 9 + 7
        ROWS, COLS = len(grid), len(grid[0])

        # f[i][j][0] means arriving to coordinate (i, j) by moving down
        # f[i][j][1] means arriving to coordinate (i, j) by moving right
        f = [[0, 0] for _ in range(COLS)]
        f[0][0] = 1

        for i in range(ROWS):
            for j in range(COLS):
                if i > 0:
                    if grid[i - 1][j] == 0:
                        f[j][0] = (f[j][0] + f[j][1]) % MOD
                    else:
                        f[j][0] = f[j][1]
                
                if j > 0:
                    if grid[i][j - 1] == 0:
                        f[j][1] = (f[j - 1][0] + f[j - 1][1]) % MOD
                    else:
                        f[j][1] = f[j - 1][0]
        
        return (f[-1][0] + f[-1][1]) % MOD
