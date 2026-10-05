class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        res, bal = 0, 0

        for i, c in enumerate(s):
            if c == '(':
                bal += 1
            else:
                bal -= 1
                
                if s[i - 1] == '(':
                    res += 1 << bal
        
        return res
