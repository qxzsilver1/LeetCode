class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)

        dp = [0] * (n + 1)
        next_dp = [0] * (n + 1)

        dp[n] = next_dp[n] = 1
        
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                next_dp[j] = dp[j]

                if s[i] == t[j]:
                    next_dp[j] += dp[j + 1]
                
            dp = next_dp[:]
        
        return dp[0]
