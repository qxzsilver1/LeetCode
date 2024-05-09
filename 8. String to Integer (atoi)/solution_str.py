class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        MAX_INT = 2 ** 31 - 1
        MIN_INT = - 2 ** 31

        if not s:
            return 0
        
        sign = -1 if s[0] == '-' else 1
        i = 1 if s[0] == '+' or s[0] == '-' else 0

        res = 0

        if i < len(s) and not s[i].isdigit():
            return res

        while i < len(s):
            tmp = s[i]

            if not tmp.isdigit():
                break
            
            res *= 10
            res += int(tmp)

            i += 1
        
        res *= sign

        res = min(MAX_INT, res)
        res = max(res, MIN_INT)

        return res
        
