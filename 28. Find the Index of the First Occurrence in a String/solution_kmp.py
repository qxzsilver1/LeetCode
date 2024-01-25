class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == '':
            return 0
        
        m = len(haystack)
        n = len(needle)

        lps = [0] * n

        prev_lps, i = 0, 1

        while i < n:
            if needle[i] == needle[prev_lps]:
                lps[i] = prev_lps + 1
                prev_lps += 1
                i += 1
            elif prev_lps == 0:
                lps[i] = 0
                i += 1
            else:
                prev_lps = lps[prev_lps - 1]
        
        i, j = 0, 0

        while i < m:
            if haystack[i] == needle[j]:
                i += 1
                j += 1
            else:
                if j == 0:
                    i += 1
                else:
                    j = lps[j - 1] 
            
            if j == n:
                return i - n 
        
        return -1
