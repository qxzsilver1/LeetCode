class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_to_t = {}
        i, n = 0, len(s)

        for i in range(n):
            if s[i] not in s_to_t:
                s_to_t[s[i]] = t[i]
            elif s_to_t[s[i]] != t[i]:
                return False
        
        return True
