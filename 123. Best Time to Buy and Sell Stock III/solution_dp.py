class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        
        dp = [0] * len(prices)

        for t in range(1, 3): # since there are two transactions at most

            pos = -prices[0]
            profit = 0

            for i in range(1, len(prices)):
                pos = max(pos, dp[i]-prices[i])
                profit = max(profit, prices[i] + pos)
                dp[i] = profit
        
        return profit
