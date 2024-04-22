class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        m, n = len(str1), len(str2)

        def isDivisor(l):
            if m % l or n %l:
                return False
            
            factor1, factor2 = m // l, n // l
            
            return str1[:l] * factor1 == str1 and str1[:l] * factor2 == str2
        
        for l in range(min(m, n), 0, -1):
            if isDivisor(l):
                return str1[:l]
        
        return ''
