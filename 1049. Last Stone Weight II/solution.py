class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        stones_sum = sum(stones)
        target = ceil(stones_sum / 2)

        dp = {}

        def dfs(i, total):
            if total >= target or i == len(stones):
                return abs(total - (stones_sum - total))
            
            if (i, total) in dp:
                return dp[(i, total)]
            
            dp[(i, total)] = min(dfs(i + 1, total), dfs(i + 1, total + stones[i]))
            
            return dp[(i, total)]
        
        return dfs(0, 0)
