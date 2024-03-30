class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        s = s + s
        alt_str1, alt_str2 = '', ''

        for i in range(2*n):
            alt_str1 += '0' if i % 2 else '1'
            alt_str2 += '1' if i % 2 else '0'

        res = 2*n

        diff1, diff2 = 0, 0
        l = 0

        for r in range(2*n):
            if s[r] != alt_str1[r]:
                diff1 += 1
            
            if s[r] != alt_str2[r]:
                diff2 += 1
            
            if r - l + 1 > n:
                if s[l] != alt_str1[l]:
                    diff1 -= 1
                
                if s[l] != alt_str2[l]:
                    diff2 -= 1
                
                l += 1
            
            if (r - l + 1) == n:
                res = min(res, diff1, diff2)


        return res
