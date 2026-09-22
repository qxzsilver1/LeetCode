class Solution:
    def integerBreak(self, n: int) -> int:
        
        def dfs(num):
            if num == 1:
                return num
            
            res = 0 if num == n else num

            for i in range(1, num):
                val = dfs(i) * dfs(num - i)
                res = max(res, val)
            
            return res
        
        return dfs(n)
