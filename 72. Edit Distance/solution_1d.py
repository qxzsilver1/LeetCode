class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)

        if m < n:
            m, n = n, m
            word1, word2 = word2, word1

        dp = [0] * (n + 1)
        next_dp = [0] * (n + 1)

        for j in range(n + 1):
            dp[j] = n - j
        
        for i in range(m - 1, -1, -1):
            next_dp[n] = m - i

            for j in range(n - 1, -1, -1):
                if word1[i] == word2[j]:
                    next_dp[j] = dp[j + 1]
                else:
                    next_dp[j] = 1 + min(dp[j], next_dp[j + 1], dp[j + 1])
            
            dp = next_dp[:]
        
        return dp[0]
