class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        
        buy_sell_k = [float('-inf')] * (2*k)
        buy_sell_k[0] = -prices[0]

        for p in prices:
            for i in range(len(buy_sell_k)):
                if i == 0:
                    buy_sell_k[i] = max(buy_sell_k[i], -p)
                else:
                    negate = 1 if (i % 2) else -1
                    buy_sell_k[i] = max(buy_sell_k[i], buy_sell_k[i-1] + negate * p)
        
        return max(buy_sell_k[2*k-1], 0)
