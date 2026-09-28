class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        i = 0
        j = 1
        res = 1

        while j < len(s) and i < len(s):
            while j < len(s) and (ord(s[j]) - ord(s[j-1]) == 1):
                j += 1
            res = max(res, j - i)

            j += 1
            i = j - 1
        
        return res
            
