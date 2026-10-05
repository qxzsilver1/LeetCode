class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        def divideConquer(i, j):
            res, bal = 0, 0

            for k in range(i, j):
                bal += 1 if s[k] == '(' else -1

                if bal == 0:
                    if k - i == 1:
                        res += 1
                    else:
                        res += 2 * divideConquer(i + 1, k)
                    
                    i = k + 1
            
            return res
        
        return divideConquer(0, len(s))
        
        return res
