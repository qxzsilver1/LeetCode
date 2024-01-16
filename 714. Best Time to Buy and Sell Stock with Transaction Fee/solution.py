class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)

        buy_cache, sell_cache = [(False, None)] * n, [(False, None)] * n

        def buy(day):
            if day == n:
                return 0
            
            if buy_cache[day][0]:
                return buy_cache[day][1]
            
            buy_profit = sell(day + 1) - (prices[day] + fee)
            not_buy_profit = buy(day + 1)

            buy_cache[day] = (True, max(buy_profit, not_buy_profit))

            return max(buy_profit, not_buy_profit)
        
        def sell(day):
            if day == n:
                return 0
            
            if sell_cache[day][0]:
                return sell_cache[day][1]
            
            sell_profit = buy(day + 1) + prices[day]
            not_sell_profit = sell(day + 1)

            sell_cache[day] = (True, max(sell_profit, not_sell_profit))

            return max(sell_profit, not_sell_profit)
        
        return buy(0)
