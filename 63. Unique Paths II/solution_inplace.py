class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        M, N = len(obstacleGrid), len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1 or obstacleGrid[M - 1][N - 1] == 1:
            return 0

        obstacleGrid[M - 1][N - 1] = 1

        for r in range(M - 1, -1, -1):
            for c in range(N - 1, -1, -1):
                if r == M - 1 and c == N - 1:
                    continue

                if obstacleGrid[r][c] == 1:
                    obstacleGrid[r][c] = 0
                else:
                    down = obstacleGrid[r + 1][c] if r + 1 < M else 0
                    right = obstacleGrid[r][c + 1] if c + 1 < N else 0
                    obstacleGrid[r][c] = down + right

        return obstacleGrid[0][0]
