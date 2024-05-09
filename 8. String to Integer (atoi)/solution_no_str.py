class Solution:
    def myAtoi(self, s: str) -> int:
        
        def stripWhitespace(s):
            whitespace = 0

            while whitespace < len(s) and s[whitespace] == ' ':
                whitespace += 1
            
            return s[whitespace:]

        s = stripWhitespace(s)
        
        res = 0

        if not s:
            return res
        
        sign = -1 if s[0] == '-' else 1
        i = 1 if s[0] == '-' or s[0] == '+' else 0

        if i < len(s) and (s[i] < '0' or s[i] > '9'):
            return res
        
        for c in s[i:]:
            if c >= '0' and c <= '9':
                res *= 10
                res += ord(c) - ord('0')
            
                if sign < 0 and res >= 2147483648:
                    return -2147483648
                
                if sign > 0 and res >= 2147483647:
                    return 2147483647
            else:
                return sign * res
        
        return res * sign
