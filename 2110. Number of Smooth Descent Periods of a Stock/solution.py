class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        res = 0

        for i, p in enumerate(prices):
            if i == 0 or prices[i-1] - 1 != p:
                count = 0
            
            count += 1

            res += count
        
        return res
            
