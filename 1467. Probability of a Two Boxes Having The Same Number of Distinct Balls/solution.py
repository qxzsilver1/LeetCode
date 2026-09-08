class Solution:
    def getProbability(self, balls: List[int]) -> float:
        k = len(balls)
        total = sum(balls)
        half = total // 2
        total_ways = comb(total, half)
        
        def dfs(idx, n1, n2, d1, d2):
            if n1 > half or n2 > half:
                return 0
            if idx == k:
                if n1 == half and d1 == d2:
                    return 1
                return 0
            res = 0
            
            for i in range(balls[idx] + 1):
                j = balls[idx] - i
                c1 = 1 if i > 0 else 0
                c2 = 1 if j > 0 else 0
                ways = comb(balls[idx], i)
                res += ways * dfs(idx+1, n1+i, n2+j, d1+c1, d2+c2)
            return res
        
        return dfs(0, 0, 0, 0, 0) / total_ways
