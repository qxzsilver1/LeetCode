class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0

        while j < len(t) and i < len(s):
            if s[i] == t[j]:
                i += 1
            
            if i == len(s):
                return True
            
            j += 1
        
        return i == len(s)
            
