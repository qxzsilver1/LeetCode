class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        res = []

        def backtrack(num, combo):
            if combo:
                res.append(combo + [num])
            
            for i in range(2, int(sqrt(num)) + 1):
                if num % i:
                    continue
                
                if not combo or i >= combo[-1]:
                    backtrack(num // i, combo + [i])

        
        backtrack(n, [])

        return res
