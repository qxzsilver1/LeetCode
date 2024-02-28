class Solution:
    def numTilings(self, n: int) -> int:
        if n == 1:
            return 1
        
        dp = [[0] * n for i in range(3)]

        dp[0][0] = 1
        dp[0][1] = 2
        dp[1][1] = 1
        dp[2][1] = 1

        for i in range(2, n):
            dp[0][i] = dp[0][i-1] + dp[1][i-1] + dp[2][i-1] + dp[0][i-2]
            dp[1][i] = dp[2][i-1] + dp[0][i-2]
            dp[2][i] = dp[1][i-1] + dp[0][i-2]
        
        return dp[0][-1] % (10 ** 9 + 7)
