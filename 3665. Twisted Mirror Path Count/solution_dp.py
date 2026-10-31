class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        MOD = 10 ** 9 + 7
        ROWS, COLS = len(grid), len(grid[0])

        # f[i][j][0] means arriving to coordinate (i, j) by moving down
        # f[i][j][1] means arriving to coordinate (i, j) by moving right
        f = [[[0, 0] for _ in range(COLS)] for _ in range(ROWS)]
        f[0][0][0] = 1

        for i in range(ROWS):
            for j in range(COLS):
                if i > 0:
                    if grid[i - 1][j] == 0:
                        f[i][j][0] = f[i - 1][j][0] + f[i - 1][j][1]
                    else:
                        f[i][j][0] = f[i - 1][j][1]
                    f[i][j][0] %= MOD
                
                if j > 0:
                    if grid[i][j - 1] == 0:
                        f[i][j][1] = f[i][j - 1][0] + f[i][j - 1][1]
                    else:
                        f[i][j][1] = f[i][j - 1][0]
                    f[i][j][1] %= MOD
        
        return (f[ROWS - 1][COLS - 1][0] + f[ROWS - 1][COLS - 1][1]) % MOD
