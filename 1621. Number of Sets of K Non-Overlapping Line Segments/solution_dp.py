class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        M = 10 ** 9 + 7
        
        dp = [1] * n

        prefix_sum = [0] * (n + 1)

        for j in range(n):
            prefix_sum[j + 1] = (prefix_sum[j] + dp[j]) % M
        
        for _ in range(k):
            dp[0] = 0

            for j in range(1, n):
                dp[j] = (dp[j - 1] + prefix_sum[j]) % M
            
            for j in range(n):
                prefix_sum[j + 1] = (prefix_sum[j] + dp[j]) % M
        
        return dp[n - 1]
