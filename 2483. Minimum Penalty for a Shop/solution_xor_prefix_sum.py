class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers)
        dp = [[0] * (n+1) for _ in range(2)]
        prefix_sums = [[0] * (n+1) for _ in range(2)]
        min_penalty, earliest_idx = float('inf'), 0

        for i in range(1, n+1):
            dp[0][i], dp[1][i] = int(customers[i-1] == 'Y'), int(customers[i-1] == 'N')
        
        for i in range(n+1):
            prefix_sums[0][i] = prefix_sums[0][i-1] + dp[0][i] if i > 0 else dp[0][0]
            prefix_sums[1][i] = prefix_sums[1][i-1] + dp[1][i] if i > 0 else dp[1][0]
        
        penalty = 0
        for i in range(n+1):
            penalty = prefix_sums[0][n] - prefix_sums[0][i] + prefix_sums[1][i]

            if penalty < min_penalty:
                earliest_idx = i
                min_penalty = penalty
        
        return earliest_idx
